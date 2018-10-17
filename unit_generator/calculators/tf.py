# -*- coding:utf-8 -*-
'''
Created on 17 Oct 2018

@author: wyan2
'''



import sys
sys.path.append('..')

from processors.Doc_processor_tf import Doc_processor_tf



# TODO: add a abstract class
class tf():
    
    def __init__(self):
        self.doc_processor = Doc_processor_tf()
    
    # generator return the 
    def cal(self, docPath):
        docName, termCounter = self.doc_processor.process(docPath)
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
    
    
    
    
    