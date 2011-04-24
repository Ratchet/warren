import urllib2
import os.path

def checkFileForInsert(mimeData):
    try:
        for format in mimeData.formats():
            if format == "text/uri-list":
                url = str(mimeData.urls()[0].toString()) # only use the first one
                u = urllib2.urlopen(url)
                for header in u.headers.items():
                    if header[0] == 'content-type':
                        u.close()
                        return (url, header[1])
        return False
    except: # TODO make this nicer
        return False
