# url_data
# https://docs.python.org/3/library/urllib.parse.html

import requests
from urllib.parse import urlparse

class urlObject:
    def __init__(self, url,AR=False):
        super().__init__()
        self.url = url

        '''
        Parse url, decomposing in elements, preparating for test
        '''
        results = urlparse(self.url)

        self.scheme = results.scheme
        self.netloc = results.netloc
        self.path = results.path
        self.params = results.params
        self.fragment = results.fragment
        
        '''
        Test URL, check if url is alive (200) or not, or redirect (301). Decomposing the url's information in
        fields returned 
        '''
        if self.scheme == '':
            url2Test = 'http://'+self.path
        else:
            url2Test = self.scheme+'://'+self.netloc
        
        try:
            r = requests.get(url2Test, allow_redirects=AR,timeout=1)
            #self.isAlive = True
            #self.is_permanent_redirect = r.is_permanent_redirect
            self.status_code = r.status_code
            self.urlTested = r.url
            self.headers = r.headers
        except TimeoutError:
            #self.isAlive = False
            print('Error Timeout:  '+url2Test)
            self.status_code = 0
            self.urlTested = url2Test
        except ConnectionError:
            #self.isAlive = False
            print('Error ConnectionError:  '+url2Test)
            self.status_code = -1
            self.urlTested = url2Test    
        #except TooManyRedirects:
            #self.isAlive = False
        #    print('Error TooManyRedirects:  '+url2Test)
        #    self.status_code = -2        
        except:
            print('Error:  '+url2Test)
            self.status_code = -2
            self.urlTested = url2Test
        
        print (self.url+' status code --'+str(self.status_code))