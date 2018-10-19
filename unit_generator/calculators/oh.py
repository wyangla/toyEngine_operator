# -*- coding:utf-8 -*-
'''
Created on 17 Oct 2018

@author: wyan2
'''


import sys
sys.path.append('..')

from processors import Doc_processor_tf



# TODO: add a abstract class
class oh():
    
    def __init__(self):
        self.doc_processor = Doc_processor_tf()
    
    # generator return the 
    def cal(self, docPath):
        processedDoc = self.doc_processor.process(docPath)
        docName = processedDoc.getDocName() 
        termCounter = processedDoc.getTermCounter()
        
        for term in termCounter:
            yield docName, term, {'oh':1}
            
            
        
def getIns():
    return oh()


