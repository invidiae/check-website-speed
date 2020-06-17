import csv
import time
import requests
URLs = ["/1595", "/74829", "/16043", "/75678", "/40786"]
cookie = {'useFrontend':'0'}
wo_cache = {'Authorization':'0'}
anmeldung = {'Authorization': 'Basic c3VybG90ZWFtOnNlcmxvdGVhbQ=='}
csv_header = ["URL", "Loading_Time", "Cache", "Mode"]
def A(URL):
    FullURL = "https://frontend-git-resolve-262.serlo.now.sh"+URL
    for i in range(10):
        tic = time.time()
        r = requests.get(FullURL, cookies=cookie)
        toc = time.time()
        writer.writerow([FullURL, toc-tic, r.headers['x-vercel-cache'], "A"])
def B(URL):
    FullURL = "https://frontend-git-resolve-262.serlo.now.sh/api/frontend"+URL
    for i in range(10):
        tic = time.time()
        r = requests.get(FullURL, cookies=cookie, headers=wo_cache)
        toc = time.time()
        writer.writerow([FullURL, toc-tic, r.headers['x-vercel-cache'], "B"])
def C(URL):
    FullURL = "https://frontend-git-resolve-262.serlo.now.sh/api/frontend"+URL
    for i in range(10):
        tic = time.time()
        r = requests.get(FullURL, cookies=cookie)
        toc = time.time()
        writer.writerow([FullURL, toc-tic, r.headers['x-vercel-cache'], "C"])


def D(URL):
    FullURL = "https://de.serlo-staging.dev"+URL
    for i in range(10):
        tic = time.time()
        r = requests.get(FullURL,cookies=cookie, headers=anmeldung)
        toc = time.time()
        writer.writerow([FullURL, toc-tic, r.headers['x-vercel-cache'], "D"])
def E(URL):
    FullURL = "https://de.serlo-staging.dev/api/frontend"+URL
    for i in range(3):
        tic = time.time()
        r = requests.get(FullURL, cookies=cookie, headers=anmeldung)
        toc = time.time()
        writer.writerow([FullURL, toc-tic, r.headers['x-vercel-cache'], "E"])

with open("loadtimes.csv", "w", newline='') as loadtimes:
    writer = csv.writer(loadtimes, delimiter=',')
    writer.writerow(csv_header)
    for URL in URLs:
        A(URL)
        print("1/5 done")
        B(URL)
        print("2/5 done")
        C(URL)
        print("3/5 done")
        D(URL)
        print("4/5 done")
        E(URL)