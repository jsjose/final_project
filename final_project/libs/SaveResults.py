# Save Results method

#from url_data import urlObject

def SaveResults(urlObj):
    '''
    Inefficient method to do this, first attempt
    '''
    nFile = "Data\\DomainChecked"
    nFile = "DomainChecked.txt"
    f = open (nFile,'a',encoding='utf-8')
    f.seek(0,2)
    if urlObj.status_code <= 0:
        f.write(str(urlObj.status_code)+','+
            urlObj.urlTested+','+
           '\n')
    else:
        f.write(
            #urlObj.scheme+','+
            #urlObj.netloc+','+
            urlObj.path+','+
            #urlObj.params+','+
            #urlObj.fragment+','+
            str(urlObj.status_code)+','+
            urlObj.urlTested+','+
            str(urlObj.headers)+'\n')
    f.close()