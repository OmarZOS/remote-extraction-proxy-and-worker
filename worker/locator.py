import json
import os
import xmlrpc.client

from publisherImplementation import publisherImplementation
from constants import *

class locator(object):
    
    # services = {}
    # services["Twitter-service1"] = TwitterExtractor
    publisher = publisherImplementation(RMQ_EXCHANGE,user=RMQ_USER,password=RMQ_PASSWORD)

    with open("extractors.json") as f:
        availableServices = json.load(f)
    
    # Eager init, unglaublisch.. :'(
    @staticmethod
    def getPublisher(self):
        return self.publisher
    
    @staticmethod
    def setService(self,service_name,instance):
        self.availableServices[service_name] = instance
    
    @staticmethod
    def getService(self,service_name):
        return self.availableServices[service_name]
