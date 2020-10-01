#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @author: Giancarlo Panichi
#
# Created on 2018/06/15 
# 
import requests
from .storagehubcommand import StorageHubCommand


class StorageHubCommandItemUpload(StorageHubCommand):     

    def __init__(self, gcubeToken, storageHubUrl, folderItemId, file, filename, fileDescription): 
        self.gcubeToken = gcubeToken
        self.folderItemId = folderItemId
        self.storageHubUrl = storageHubUrl
        self.file = file
        self.filename = filename
        self.fileDescription = fileDescription
        
    def execute(self):
        print("Execute StorageHubCommandItemUpload")
        print(self.storageHubUrl + "/items/" + self.folderItemId + "/create/FILE?");
            
        filedata = {'name': self.filename, 'description': self.fileDescription, "file": ("file", open(self.file, "rb"))}
        
        urlString = self.storageHubUrl + "/items/" + self.folderItemId + "/create/FILE?gcube-token=" + self.gcubeToken
        r = requests.post(urlString, files=filedata)
        print(r)
        print(r.status_code)
        if r.status_code != 200:
            print("Error in execute StorageHubCommandItemUpload: " + r.status_code)
            raise Exception("Error in execute StorageHubCommandItemUpload: " + r.status_code)
        print(str(r.text))
        return r.text

    def __str__(self): 
        return ('StorageHubCommandItemUpload[itemId=' + self.folderItemId + 
                ', storageHubUrl=' + str(self.storageHubUrl) + 
                ', folderItemId=' + str(self.folderItemId) + 
                ', filename=' + str(self.filename) + 
                ', fileDescription=' + str(self.fileDescription) + ']') 
