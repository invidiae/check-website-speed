import csv
import time
import requests
URLs = ["/48492", "/24706", "/1617", "/19882", "/18922"]
cookie = {'useFrontend': '0'}
wo_cache = {'Authorization': '0'}
anmeldung = {'Authorization': 'Basic c3VybG90ZWFtOnNlcmxvdGVhbQ=='}
csv_header = ["URL", "Loading_Time", "Cache", "Status-Code", "Mode"]

url = "frontend-git-update-readme.serlo.vercel.app"
url = "frontend.serlo.org"
anzahl = 50


def A(URL):
    FullURL = "https://" + url + URL
    for i in range(2):
        requests.get(FullURL)
    for i in range(anzahl):
        tic = time.time()
        r = requests.get(FullURL)
        toc = time.time()
        writer.writerow([URL, toc - tic, r.headers['x-vercel-cache'], r.status_code,"A"])


def B(URL):
    FullURL = "https://" + url + "/api/frontend"+ URL
    for i in range(anzahl):
        tic = time.time()
        r = requests.get(FullURL, headers=wo_cache)
        toc = time.time()
        writer.writerow([URL, toc - tic, r.headers['x-vercel-cache'], r.status_code,"B"])


def C(URL):
    FullURL = "https://" + url + "/api/frontend" + URL
    for i in range(2):      # Make sure URL is already cached
        requests.get(FullURL, cookies=cookie)
    for i in range(anzahl):
        tic = time.time()
        r = requests.get(FullURL, cookies=cookie)
        toc = time.time()
        writer.writerow([URL, toc - tic, r.headers['x-vercel-cache'],r.status_code, "C"])


def D(URL):             # Can't be cached because of Authentification
    FullURL = "https://de.serlo-staging.dev" + URL
    for i in range(anzahl):
        tic = time.time()
        r = requests.get(FullURL, cookies=cookie)
        toc = time.time()
        writer.writerow([URL, toc - tic, r.headers['x-vercel-cache'], r.status_code,"D"])


def E(URL):
    FullURL = "https://de.serlo-staging.dev/api/frontend" + URL
    for i in range(anzahl):
        tic = time.time()
        r = requests.get(FullURL, cookies=cookie, headers=wo_cache)
        toc = time.time()
        writer.writerow([URL, toc - tic, r.headers['x-vercel-cache'], r.status_code,"E"])


def F(URL):
    FullURL = "https://de.serlo-staging.dev/api/frontend" + URL
    for i in range(anzahl):
        tic = time.time()
        r = requests.get(FullURL, cookies=cookie)
        toc = time.time()
        writer.writerow([URL, toc - tic, r.headers['x-vercel-cache'], r.status_code,"F"])


with open("loadtimes.csv", "w+", newline='') as loadtimes:
    writer = csv.writer(loadtimes, delimiter=',')
    writer.writerow(csv_header)
    for index, URL in enumerate(URLs):
        A(URL)
        print(f"1/5 done of {index+1}/{len(URLs)}")
        B(URL)
        print(f"2/5 done of {index+1}/{len(URLs)}")
        C(URL)
        print(f"3/5 done of {index+1}/{len(URLs)}")
        D(URL)
        print(f"4/5 done of {index+1}/{len(URLs)}")
        E(URL)
        print(f"5/5 done of {index+1}/{len(URLs)}")
        F(URL)
