import re
import importlib
import ConfigParser


def get_downloader(cfile):
    config = ConfigParser.ConfigParser()
    config.read(cfile)
    try:
        res = config.get('main', 'resource')
    except:
        raise Exception("Invalid configuration")

    if not re.match('^\w+$', res):
        raise Exception("Invalid configuration %s" % res)

    try:
        m = importlib.import_module('aed.%s' % res)
    except ImportError:
        raise Exception("Invalid resource %s" % res)

    return m.Downloader(config)
