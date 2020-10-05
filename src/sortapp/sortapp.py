#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @author: Giancarlo Panichi
#
# Created on 2020/06/12
#
import sys
import os
from .issupport import ISSupport
from .storagehub.storagehubcommanditemdownload import StorageHubCommandItemDownload
from .storagehub.storagehubcommanditemupload import StorageHubCommandItemUpload
import subprocess
import zipfile

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


class SortApp:

    def __init__(self):
        self.gcubeToken = sys.argv[1]
        self.fileItemId = sys.argv[2]
        self.tempFolderItemId = sys.argv[3]
        self.destinationFile = "elements.txt"
        self.storageHubUrl = None

    def main(self):
        print(self)
        issup = ISSupport()
        self.storageHubUrl = issup.discoverStorageHub(self.gcubeToken)
        self.executeSort()

    def executeSort(self):
        print("Execute Sort")
        print('gcubeToken: ' + self.gcubeToken)
        print('fileItemId: ' + self.fileItemId)

        if not self.gcubeToken:
            raise Exception('Error Token is null')

        if not self.fileItemId:
            raise Exception('Error File Item Id is null')


        # create a writable temporary directory
        workdir = '/tmp/DIVAnd'
        if not os.path.isdir(workdir):
            os.mkdir(workdir)
        os.chdir(workdir)

        cmdItemDownload = StorageHubCommandItemDownload(self.gcubeToken, self.storageHubUrl,
                                                        self.fileItemId, self.destinationFile)
        cmdItemDownload.execute()

        # name of the log file
        logfile  = 'DIVAnd.log'

        print("Run julia")
        with open(logfile, 'w') as f:
            # run julia with file downloaded file from StorageHub as argument and redirect stdout
            # and stderr to the log file
            process = subprocess.Popen(['julia', self.destinationFile], stdout=f,stderr=f)


        print("Create zip file")
        # zip all files un current directory including log file
        outputfile = "output.zip"
        zipf = zipfile.ZipFile(outputfile, 'w', zipfile.ZIP_DEFLATED)
        zipdir(workdir, zipf)
        zipf.close()

        print("Uploading results")
        # upload the zipped output file
        cmdItemUpload = StorageHubCommandItemUpload(self.gcubeToken, self.storageHubUrl, self.tempFolderItemId,
                                                    outputfile,outputfile,outputfile)
        cmdItemUpload.execute()
        print("Uploading finished")

    def __str__(self):
        return 'Sort App'


def main():
    print('SortApp main()')
    sortApp = SortApp()
    sortApp.main()


main()
