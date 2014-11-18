from __future__ import print_function
'''
Google Drive Downloader
'''

from .base import BaseDownloader
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


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
          file1.GetContentFile('dest/%s.xlsx' % file1['title'], mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
