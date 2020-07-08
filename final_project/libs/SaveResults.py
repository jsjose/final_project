# Save Results method

#from url_data import urlObject

import sqlite3

from sqlite3 import Error

def SaveResults2File(urlObj):
    '''
    Inefficient method to do this, first attempt
    Save urlObj to local defined file
    '''
    nFile = "Data\\DomainChecked"
    nFile = "DomainChecked.txt"
    f = open (nFile,'a',encoding='utf-8')
    f.seek(0,2)
    if urlObj.status_code <= 0:
        f.write(
            urlObj.datetime+','+
            str(urlObj.status_code)+','+
            urlObj.urlTested+','+
           '\n')
    else:
        f.write(
            urlObj.datetime+','+
            #urlObj.scheme+','+
            #urlObj.netloc+','+
            urlObj.path+','+
            #urlObj.params+','+
            #urlObj.fragment+','+
            str(urlObj.status_code)+','+
            urlObj.urlTested+','+
            str(urlObj.headers)+'\n')
    f.close()
    return

def SaveResults2DB(urlObj,conn):
    '''
    using slqite
    '''
    
    cursorObj = conn.cursor()
    
    entitiesUrl = (urlObj.datetime, urlObj.path)
    entitiesUrlTested = (urlObj.datetime, urlObj.path, urlObj.status_code, urlObj.urlTested, str(urlObj.headers))

    try:
        cursorObj.execute('INSERT INTO url(datetime, path) VALUES(?, ?)', entitiesUrl)
    except sqlite3.IntegrityError:
        print(urlObj.path +' exists')
    
    cursorObj.execute('INSERT INTO urlTested(datetime, path, status_code, urlTested, headers) VALUES(?, ?, ?, ?, ?)', entitiesUrlTested)
    #cursorObj.execute('UPDATE url SET datetime = ?, status_code = ?, urlTested = ?, headers = ? WHERE path == ?', entitiesE)

    conn.commit()
    
    return