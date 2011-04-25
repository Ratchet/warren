from PyQt4.QtCore import QThread
import urllib2
import os.path

def buildOpener(url, proxy=None):
    if len(url)>=4 and url[:4]=='http' and proxy and proxy.get('host','') != '':
        proxies = {'http':'%s:%s' % (proxy['host'],proxy['port']),
                   'https':'%s:%s' % (proxy['host'],proxy['port']),}
        p = urllib2.ProxyHandler(proxies=proxies)
        opener = urllib2.build_opener(p)
    else:
        opener = urllib2.build_opener()
    return opener

def checkFileForInsert(mimeData, proxy=None):
    try:
        for format in mimeData.formats():
            if format == "text/uri-list":
                url = str(mimeData.urls()[0].toString()) # only use the first one
                opener = buildOpener(url, proxy)
                u = opener.open(url)
                for header in u.headers.items():
                    if header[0] == 'content-type':
                        u.close()
                        return (url, header[1])
        return False
    except: # TODO make this nicer
        return False


class FileInsert(QThread):

    def __init__(self, parent, url, mimeType, proxy=None):
        QThread.__init__(self, parent)
        self.nodeManager = parent
        self.url = url
        self.mimeType = mimeType
        self.proxy = proxy

    def run(self):
        opener = buildOpener(self.url, self.proxy)
        u = opener.open(self.url)
        filename = os.path.basename(self.url)
        data = u.read() # we have to make this streaming in the future (pyFreenet can't handle it atm)
        u.close()
        insert = self.putData(data, filename, self.mimeType)
        self.quit() # because we put everything on node's global queue, we are not interested in what happens after put()

    def putData(self, data, filename, mime_type):
        #TODO: first check with fcp put method "disk" to check if we're on same machine as node or if node
        #      has different permissions on selected file.
        #      only if node answer with error on method "disk", fall back to method "direct"
        #      AND WHY THE FUCK BLOCKS PYFREENET THE WHOLE PROGRAM WHILE UPLOADING EVEN IF IT RUNS IN THREAD???
        return self.nodeManager.node.put(uri='SSK@',data=data,async=True,name=filename,persistence='forever',Global=True,id='Fripe-'+filename,mimetype=mime_type,waituntilsent=True)
