import csv
import time
import requests
URLs = ["/115915", "/16043", "/27023", ""]
cookie = {'useFrontend':'0'}
wo_cache = {'Authorization':'0'}
anmeldung = {'Authorization': 'Basic c2VybG90ZWFtOnNlcmxvdGVhbQ=='}
csv_header = ["URL", "Loading_Time", "Cache"]
def A(URL):
    FullURL = "http://frontend-git-resolve-262.serlo.now.sh"+URL
    for i in range(7):
        tic = time.time()
        r = requests.get(FullURL, cookies=cookie)
        toc = time.time()
        writer.writerow([FullURL, toc-tic, r.headers['x-vercel-cache']])
def B(URL):
    FullURL = "http://frontend-git-resolve-262.serlo.now.sh/api/frontend"+URL
    for i in range(7):
        tic = time.time()
        r = requests.get(FullURL, cookies=cookie, headers=wo_cache)
        toc = time.time()
        writer.writerow([FullURL, toc-tic, r.headers['x-vercel-cache']])
def C(URL):
    FullURL = "http://frontend-git-resolve-262.serlo.now.sh/api/frontend"+URL
    for i in range(7):
        tic = time.time()
        r = requests.get(FullURL, cookies=cookie)
        toc = time.time()
        writer.writerow([FullURL, toc-tic, r.headers['x-vercel-cache']])


def D(URL):
    FullURL = "http://de.serlo-staging.dev"+URL
    for i in range(7):
        tic = time.time()
        r = requests.get(FullURL,cookies=cookie, headers=anmeldung)
        toc = time.time()
        writer.writerow([FullURL, toc-tic, r.headers['x-vercel-cache']])
def E(URL):
    FullURL = "http://de.serlo-staging.dev/api/frontend"+URL
    for i in range(7):
        tic = time.time()
        r = requests.get(FullURL, cookies=cookie, headers=anmeldung)
        toc = time.time()
        writer.writerow([FullURL, toc-tic, r.headers['x-vercel-cache']])

with open("loadtimes.csv", "a", newline='') as loadtimes:
    writer = csv.writer(loadtimes, delimiter=',')
  #  writer.writerow(csv_header)
    for URL in URLs:
        A(URL)
        B(URL)
        C(URL)
        B(URL)
        D(URL)
        E(URL)