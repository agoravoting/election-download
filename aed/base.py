class BaseDownloader:
    def __init__(self, config):
        raise NotImplementedError

    def download(self):
        raise NotImplementedError
