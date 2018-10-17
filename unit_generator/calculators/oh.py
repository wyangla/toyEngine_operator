# -*- coding:utf-8 -*-
'''
Created on 17 Oct 2018

@author: wyan2
'''


import sys
sys.path.append('..')

from processors.Doc_processor_tf import Doc_processor_tf



# TODO: add a abstract class
class oh():
    
    def __init__(self):
        self.doc_processor = Doc_processor_tf()
    
    # generator return the 
    def cal(self, docPath):
        docName, termCounter = self.doc_processor.process(docPath)
        for term in termCounter:
            yield docName, term, {'oh':1}
            
            
        
def getIns():
    return oh()


