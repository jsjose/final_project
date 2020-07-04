# final work for course Complete Python Bootcamp by Udemy

import sys
import os

from libs.url_data import urlObject
from libs.SaveResults import SaveResults

def run_project(args):
    
    domainsFile ="data\\domains1"
    
    with open(domainsFile, 'r', encoding='utf-8') as file:
        file = file.read().splitlines()
    
    listaURL = list()
    for url in file:
        urlObj = urlObject(url)
        listaURL.append(urlObj)
        while urlObj.status_code == 301 or urlObj.status_code == 302:
            #print('url - '+url)
            urlObj = urlObject(urlObj.url,True)
            listaURL.append(urlObj)

    # Save results
    for urlObj2Save in listaURL:
        print('urltested ' + urlObj2Save.urlTested)
        SaveResults(urlObj2Save)
    
if __name__ == '__main__':
    #print(os.getcwd())
    print('Final project for course Complete Python Bootcamp')
    run_project(sys.argv)