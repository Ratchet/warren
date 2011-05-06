import sys, os, os.path
from configobj import ConfigObj

CONFIG_DEFAULTS = {'node' : {'host':'127.0.0.1','fcp_port':9481, 'fproxy_port':8888},
                   'proxy' : {'http':{'host':'','port':8118}},
                   'warren' : {'file_keytype':'SSK@', 'pastebin_keytype':'SSK@',
                               'browser_command' : '',
                               'max_clipboard_keys' : 5,
                               'start_on_top' : False,
                               'show_file_dropped_dialog':True},
                   }

#TODO options for priorities, separate for pastebin and file inserts

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
            self.update(CONFIG_DEFAULTS)
            self.write()
        else:
            self.reload()
            for section, value in CONFIG_DEFAULTS.iteritems():
                if not self.get(section):
                    self[section] = value
                    continue
                if type(value) == type(dict()):
                    for subsection, subvalue in value.iteritems():
                        if not self[section].get(subsection):
                            self[section][subsection] = subvalue


