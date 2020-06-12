from selenium import webdriver
import time
URL = "https://frontend-git-resolve-262.serlo.now.sh/"
path = "/home/camillo/chromedriver"
links = []
load = {}
measured = []
driver = webdriver.Chrome(path)
driver.get(URL)
elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
    links.append(elem.get_attribute("href"))
for link in links:
    if link not in measured and link[0:len(URL)] == URL:
        tic = time.time()
        driver.get(link)
        toc = time.time()
        load[link] = toc-tic
        measured.append(link)
driver.close()
avgload = sum(load.values())/len(load.values())
slow = {}
for t in load:
    if load[t] > 2*avgload:
        slow[t] = load[t]
with open("results.txt", "w+") as results:
    results.write("average loading speed in seconds: \n")
    results.write(str(avgload))
    results.write("\n")
    results.write("sites with 100% more loading speed than average: \n")
    results.write(str(slow))
