import sys, os, os.path
from configobj import ConfigObj

CONFIG_DEFAULTS = {'node':{'host':'127.0.0.1','fcp_port':9481}}

class Config(ConfigObj):

    def __init__(self):
        ConfigObj.__init__(self)

        # wild os guessing :-)
        if "win32" in sys.platform.lower():
            dirname = "Warren"
        else:
            dirname = ".warren"

        filepath = os.path.join(os.path.expanduser("~"),dirname)
        self.filename = os.path.join(filepath,"settings.cfg")
        if not os.path.exists(filepath):
            os.makedirs(filepath)
            self.update(CONFIG_DEFAULTS )
            self.write()
        else:
            self.reload()
