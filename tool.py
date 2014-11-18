#!/usr/bin/env python

'''
Tool to use Agora Election Download from command line
'''

import argparse
from aed import get_downloader


def main():
    parser = argparse.ArgumentParser(
        description='Downloads Agora Election from diferent resources.')
    parser.add_argument('-c', '--config', dest='config', action='store',
                        default="settings.conf",
                        help='sets the config file to use (default: settings.conf)')

    args = parser.parse_args()
    downloader = get_downloader(args.config)
    downloader.download()


if __name__ == '__main__':
    main()
