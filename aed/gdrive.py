from __future__ import print_function
'''
Google Drive Downloader
'''

from .base import BaseDownloader
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from .xlstotsv import xls_to_tsv


class Downloader(BaseDownloader):
    def __init__(self, config):
        self.folder = config.get('gdrive', 'folder')

    def download(self):
        print("downloading from gdrive: %s" % self.folder)

        gauth = GoogleAuth()
        drive = GoogleDrive(gauth)

        file_list = drive.ListFile({'q': "'%s' in parents and trashed=false and mimeType='application/vnd.google-apps.spreadsheet'" % self.folder}).GetList()
        for file1 in file_list:
          print('title: %s' % file1['title'])
          fname = 'dest/%s.xlsx' % file1['title']
          file1.GetContentFile(fname, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
          self.convert(fname)

    def convert(self, src):
        dst = "%s" % src[0:-5]
        xls_to_tsv(src, dst)
