import csv
import time
import requests
URLs = ["/48492", "/24706", "/157600", "/19882", "/18922"]
cookie = {'useFrontend': '0'}
wo_cache = {'Authorization': '0'}
anmeldung = {'Authorization': 'Basic c3VybG90ZWFtOnNlcmxvdGVhbQ=='}
csv_header = ["URL", "Loading_Time", "Cache", "Mode"]


def A(URL):                 # HTML doesn't get cashed, except homepage
    FullURL = "https://frontend-git-resolve-262.serlo.now.sh" + URL
    for i in range(50):
        tic = time.time()
        r = requests.get(FullURL, cookies=cookie)
        toc = time.time()
        writer.writerow([URL, toc - tic, r.headers['x-vercel-cache'], "A"])


def B(URL):
    FullURL = "https://frontend-git-resolve-262.serlo.now.sh/api/frontend" + URL
    for i in range(50):
        tic = time.time()
        r = requests.get(FullURL, cookies=cookie, headers=wo_cache)
        toc = time.time()
        writer.writerow([URL, toc - tic, r.headers['x-vercel-cache'], "B"])


def C(URL):
    FullURL = "https://frontend-git-resolve-262.serlo.now.sh/api/frontend" + URL
    for i in range(2):      # Make sure URL is already cached
        requests.get(FullURL, cookies=cookie)
    for i in range(300):
        tic = time.time()
        r = requests.get(FullURL, cookies=cookie)
        toc = time.time()
        writer.writerow([URL, toc - tic, r.headers['x-vercel-cache'], "C"])


def D(URL):             # Can't be cached because of Authentification
    FullURL = "https://de.serlo-staging.dev" + URL
    for i in range(50):
        tic = time.time()
        r = requests.get(FullURL, cookies=cookie, headers=anmeldung)
        toc = time.time()
        writer.writerow([URL, toc - tic, r.headers['x-vercel-cache'], "D"])


def E(URL):
    FullURL = "https://de.serlo-staging.dev/api/frontend" + URL
    for i in range(50):
        tic = time.time()
        r = requests.get(FullURL, cookies=cookie, headers=anmeldung)
        toc = time.time()
        writer.writerow([URL, toc - tic, r.headers['x-vercel-cache'], "E"])


with open("loadtimes.csv", "a", newline='') as loadtimes:
    writer = csv.writer(loadtimes, delimiter=',')
    # writer.writerow(csv_header)
    for index, URL in enumerate(URLs):
        # A(URL)
        print(f"1/5 done of {index+1}/{len(URLs)}")
        # B(URL)
        print(f"2/5 done of {index+1}/{len(URLs)}")
        # C(URL)
        print(f"3/5 done of {index+1}/{len(URLs)}")
        # D(URL)
        print(f"4/5 done of {index+1}/{len(URLs)}")
        E(URL)
        print(f"5/5 done of {index+1}/{len(URLs)}")
