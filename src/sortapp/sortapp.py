#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @author: Giancarlo Panichi
#
# Created on 2020/06/12 
# 
import sys
from .issupport import ISSupport
from .storagehub.storagehubcommanditemdownload import StorageHubCommandItemDownload
from .storagehub.storagehubcommanditemupload import StorageHubCommandItemUpload


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
        
        cmdItemDownload = StorageHubCommandItemDownload(self.gcubeToken, self.storageHubUrl,
                                                        self.fileItemId, self.destinationFile)
        cmdItemDownload.execute()
        
        with open(self.destinationFile, 'r') as f:
            elementsList = [line.strip() for line in f]
        
        print ("Elements found: ")
        print(*elementsList, sep="\n") 
        
        #if self.elementsOrder and self.elementsOrder == 'Desc':
        #    elementsList.sort(reverse=True)
        #else:
        elementsList.sort(reverse=False)
            
        print ("Elements sorted: ")
        print(*elementsList, sep="\n") 
        
        with open(self.destinationFile, 'w') as out_file:
            out_file.write('\n'.join(elementsList))
        
        print("Elements saved in file: " + self.destinationFile)
           
        cmdItemUpload = StorageHubCommandItemUpload(self.gcubeToken, self.storageHubUrl, self.tempFolderItemId,
                                                   self.destinationFile, self.destinationFile, self.destinationFile)
        cmdItemUpload.execute()
        
    def __str__(self): 
        return 'Sort App' 


def main():
    print('SortApp main()')
    sortApp = SortApp()
    sortApp.main()

    
main()

