# Save Results method

#from url_data import urlObject

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
    
    entities = (urlObj.datetime, urlObj.path, urlObj.status_code, urlObj.urlTested, str(urlObj.headers))

    cursorObj.execute('INSERT INTO url(datetime, path, status_code, urlTested, headers) VALUES(?, ?, ?, ?, ?)', entities)
    
    conn.commit()
    return