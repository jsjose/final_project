# final work for course Complete Python Bootcamp by Udemy

import sys
import os
import datetime

# final_project modules
from libs.url_data import urlObject
from libs.SaveResults import SaveResults2File
from libs.SaveResults import SaveResults2DB
from libs.test_db import testDB

def run_project(args):
    
    domainsFile ="data\\domains1"
    
    with open(domainsFile, 'r', encoding='utf-8') as file:
        file = file.read().splitlines()
    
    # create DB object
    dbName = '.\\data\\testdb.db'
    mydb = testDB(dbName)

    #processess urls
    listaURL = list()
    for url in file:
        urlObj = urlObject(url)
        listaURL.append(urlObj)
        while urlObj.status_code == 301 or urlObj.status_code == 302:
            #print('url - '+url)
            urlObj = urlObject(urlObj.url,True)
            listaURL.append(urlObj)
            SaveResults2DB(urlObj, mydb.conn)

    # close db
    mydb.close()

    # Save results
    for urlObj2Save in listaURL:
        print('urltested ' + urlObj2Save.urlTested)
        SaveResults2File(urlObj2Save)
    
if __name__ == '__main__':
    #print(os.getcwd())
    print('Final project for course Complete Python Bootcamp')
    run_project(sys.argv)