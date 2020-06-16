import requests
import time
load = []
url = 'https://frontend-git-resolve-262.serlo.now.sh'
UrL = 'https://de.serlo-staging.dev' # bn = serloteam, pw serloteam autorizaiton (blitter)  integral
anhang = '/api/frontend'
cookie = {'useFrontend':"0"}
URL = UrL + "/mathe"
print(URL)
for i in range(50):
    tic = time.time()
    payload = {'Authorization':'Basic c2VybG90ZWFtOnNlcmxvdGVhbQ=='}
    r = requests.get(URL, cookies=cookie, headers=payload)
    print(time.time()-tic, r.headers['x-vercel-cache'],r.status_code)
