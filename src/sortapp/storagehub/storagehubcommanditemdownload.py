#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @author: Giancarlo Panichi
#
# Created on 2018/06/15 
# 
import requests
from .storagehubcommand import StorageHubCommand


class StorageHubCommandItemDownload(StorageHubCommand):     

    def __init__(self, gcubeToken, storageHubUrl, itemId, destinationFile): 
        self.gcubeToken = gcubeToken
        self.storageHubUrl = storageHubUrl
        self.itemId = itemId
        self.destinationFile = destinationFile
        
    def execute(self):
        print("Execute StorageHubCommandItemDownload")
        print(self.storageHubUrl + "/items/" + self.itemId + "/download?");
        
        urlString = self.storageHubUrl + "/items/" + self.itemId + "/download?gcube-token=" + self.gcubeToken
        r = requests.get(urlString)
        print(r.status_code)
        if r.status_code != 200:
            print("Error in execute StorageHubCommandItemDownload: " + r.status_code)
            raise Exception("Error in execute StorageHubCommandItemDownload: " + r.status_code)
        with open(self.destinationFile, 'w') as file:
            file.write(r.text)

    def __str__(self): 
        return ('StorageHubCommandItemDownload[storageHubUrl=' + str(self.storageHubUrl) + 
                'itemId=' + self.itemId + 
                ', destinationFile=' + self.destinationFile + ']')
