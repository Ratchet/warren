import webbrowser

class Browser(object):

    def __init__(self, config):
        self.config = config

    def openKeyInBrowser(self,key):
        bcmd = self.config['warren']['browser_command']
        if bcmd:
            browser = webbrowser.get(using=bcmd)
        else:
            browser = webbrowser.get()

        proto = self.config['node'].as_bool('fproxy_ssl') and 'https' or 'http'
        url = proto+'://'+self.config['node']['host']+':'+str(self.config['node']['fproxy_port'])+'/'+key
        browser.open_new_tab(url)
