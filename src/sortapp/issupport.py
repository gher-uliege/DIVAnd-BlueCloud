#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @author: Giancarlo Panichi
#
# Created on 2018/06/15 
# 
import requests
from xml.etree import ElementTree

class ISSupport: 

    def __init__(self): 
        # dev
        #self.serviceUrl = "https://node10-d-d4s.d4science.org"
        # prod
        self.serviceUrl = "http://registry.d4science.org"
        self.storageHubServiceClass = "DataAccess"
        self.storageHubServiceName = "StorageHub"
        
    def discoverStorageHub(self,gcubeToken):
        print("Discover StorageHub")
        urlString = self.serviceUrl + "/icproxy/gcube/service/GCoreEndpoint/" + self.storageHubServiceClass + "/" + self.storageHubServiceName + "?gcube-token=" + gcubeToken
        r = requests.get(urlString)
        print(r.status_code)
        print(r.text)
        if r.status_code!=200:
            print("Error discovering StorageHub: "+r.status_code)
            raise Exception("Error retrieving StorageHub url info: "+r.status_code)
        else:
            root = ElementTree.fromstring(r.text)
            print(root)
            gcoreEndpoint=root.findall("Result/Resource/Profile/AccessPoint/RunningInstanceInterfaces/Endpoint")
            print(gcoreEndpoint)
            for child in gcoreEndpoint:
                print(child.tag, child.attrib)
                if child.attrib["EntryName"]=="org.gcube.data.access.storagehub.StorageHub":
                    print("Endpoint Found")
                    print(child.text)
                    return child.text
                
        print("Error discovering StorageHub url not found")
        raise Exception("Error retrieving StorageHub url not found!")       
        
    def __str__(self): 
        return 'ISSupport[serviceUrl=' + str(self.serviceUrl) + ']' 
