# -*- coding:utf-8 -*-
'''
Created on 17 Oct 2018

@author: wyan2
'''

import sys
sys.path.append('..')

import configs as cfg
import os
from py4j.java_gateway import JavaGateway, GatewayParameters
from unit_generator import Unit_generator 



class InvIdx_operators():
    
    def __init__(self):
        self.gateWay = JavaGateway(gateway_parameters = GatewayParameters(auto_convert = True)) # automatically convert python object to java object
        self.engine = self.gateWay.entry_point
        self.ug = Unit_generator()
        
        
    
    def add_doc(self, docPath):
        units = self.ug.flat_units(docPath)
        for term, unit in units:
            notExistanceFlag = self.engine.add_term(term)
            print(notExistanceFlag)
            self.engine.add_posting_unit(unit)
                
    
    # add all docs from one source (docs in one sub directory of /corpus)
    def add_source(self):
        pass
    
    
    def del_doc(self):
        pass
    
    
    # delete all docs from one source (docs in one sub directory of /corpus)
    def del_source(self):
        pass
    
    
    def search(self):
        pass
    
    
if __name__ == '__main__':
    import os
    
    print(type(Unit_generator))
    
    invIdxOp = InvIdx_operators()
    invIdxOp.add_doc(os.path.join(cfg.testCorpusPath, '-Km-gkgaAJAx37yEHIERDg'))
    