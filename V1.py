from selenium import webdriver
import time
import random
driver = webdriver.Chrome("/home/camillo/chromedriver")
URL = "https://frontend-git-resolve-262.serlo.now.sh"
driver.get(URL)
end_time = time.time()+60*0.15
links = []
load = {}
while end_time > time.time():
    wrong_link = False
    elems = driver.find_elements_by_xpath("//a[@href]")
    for elem in elems:
        links.append(elem.get_attribute("href")) # add some randomness (maybe 10% of sample)
    while not wrong_link:
        link = links[-1]
        if link in load or not link[0:len(URL)+6] == URL+"/mathe":
            print("falsch"+link)
            del links[-1]
        else:
            wrong_link = True
            link = links.pop(-1)
            print("richtig"+link)
    tic = time.time()
    driver.get(link)
    toc = time.time()
    load[link] = toc-tic

avgload = sum(load.values())/len(load)
slow = {}
for t in load:
    if load[t] > 2*avgload:
        slow[t] = load[t]
with open ("ergebnis.txt", "w+") as results:
    results.write("average loading speed in seconds: \n")
    results.write(str(avgload))
    results.write("sites with 100% more loading speed than average: \n")
    results.write(str(slow))

