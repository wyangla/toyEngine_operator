# -*- coding:utf-8 -*-
'''
Created on 17 Oct 2018

@author: wyan2
'''


import sys
sys.path.append('..')

from processors import Doc_processor



# TODO: add a abstract class
class tf():
    
    def __init__(self):
        self.doc_processor = Doc_processor()
    
    # generator return the 
    def cal(self, docPath):
        processedDoc = self.doc_processor.process(docPath)
        docName = processedDoc.getDocName() 
        termCounter = processedDoc.getTermCounter()
        
        for term in termCounter:
            tf = termCounter[term]
            yield docName, term, {'tf':tf}
            
            
            
def getIns():
    return tf()
            
            
            
if __name__ == '__main__':
    import configs as cfg
    import os
    
    tfIns = tf()
    tfInsGen = tfIns.cal(os.path.join(cfg.testCorpusPath, '-Km-gkgaAJAx37yEHIERDg'))
    for i in tfInsGen:
        print(i)
    
    
    
    
    