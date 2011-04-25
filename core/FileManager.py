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
        # Grade-A fugly workaround ahead! pyFreenet can't handle failing testDDARequests, because FCP doesn't work with Identifiers
        # in this request. So failing DDA jobs die. This is a trial-and-error workaround to see if we can upload the file from 
        # disk or if we have to send it over socket.
        # TODO GET RID OF PYFREENET or tell toad_ to fix testDDARequest!!!!!!
        testDDAResult = False
        if self.url[:4] == 'file':
            plainUrl = self.url[7:]
            try:
                directory = os.path.split(plainUrl)[0]
                testDDA = self.nodeManager.node.testDDA(async=False, Directory=directory, WantReadDirectory=True, timeout=5)
                if 'TestDDAComplete' in str(testDDA.items()):
                    testDDAResult = True
            except Exception, e:
                print e
                testDDAResult = False

            if testDDAResult:
                opener = buildOpener(self.url, self.proxy)
                u = opener.open(self.url)
                filename = os.path.basename(self.url)
                insert = self.putData(plainUrl, filename, self.mimeType, 'disk')
                QThread.msleep(5000)
                if insert.result is not None and 'ProtocolError' in str(insert.result):
                    testDDAResult = False
                    opener.close()

        if not testDDAResult:
            opener = buildOpener(self.url, self.proxy)
            u = opener.open(self.url)
            filename = os.path.basename(self.url)
            data = u.read() # we have to make this streaming in the future (pyFreenet can't handle it atm)
            u.close()
            insert = self.putData(data, filename, self.mimeType, 'data')
        self.quit() # because we put everything on node's global queue, we are not interested in what happens after put()

    def putData(self, data, filename, mime_type, method):
        #TODO: first check with fcp put method "disk" to check if we're on same machine as node or if node
        #      has different permissions on selected file.
        #      only if node answer with error on method "disk", fall back to method "direct"
        #      AND WHY THE FUCK BLOCKS PYFREENET THE WHOLE PROGRAM WHILE UPLOADING EVEN IF IT RUNS IN THREAD???
        if method == 'data':
            return self.nodeManager.node.put(uri='SSK@',data=data,async=True,name=filename,persistence='forever',Global=True,id='Fripe-'+filename,mimetype=mime_type,waituntilsent=True)
        if method == 'disk':
            return self.nodeManager.node.put(uri='SSK@',file=data,async=True,name=filename,persistence='forever',Global=True,id='Fripe-'+filename,mimetype=mime_type,waituntilsent=True)





