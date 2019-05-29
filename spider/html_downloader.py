## -*- coding: utf-8 -*-

# from urllib import request
#import urllib.request

import requests
from requests.packages import urllib3
class HtmlDownloader(object):
    

    def download(self, url):
#       ssl._create_default_https_context = ssl._create_stdlib_context
        print('inside downloader')
        print('enter download:',url)
        if url is None:
            return None
        # make authentication is ignored
        print('before disable warning')
        urllib3.disable_warnings()
        print('after disable,before verify')
        
        s = requests.Session()
        #request as a browser
        s.headers['User-Agent']='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2'
        response = s.get(url,verify=False)
        print('after verify')
        #check response state 
        print(response.status_code)
        if response.status_code!= 200:
            return None
        
        print('after get code before read')
       # print(response.content)

        return response.content
        # response = response.decode('utf-8')
