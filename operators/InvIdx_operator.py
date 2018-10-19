# -*- coding:utf-8 -*-
'''
Created on 17 Oct 2018

@author: wyan2
'''

import sys
from data_structures.Post_unit import Post_unit
from distributed.profile import process
sys.path.append('..')

import configs as cfg
import os
from py4j.java_gateway import JavaGateway, GatewayParameters
from unit_generator import Unit_generator 
from logger import Logger
from traceback import format_exc
from processors import Doc_processor_tf



class InvIdx_operators():
    
    def __init__(self, logger = Logger.get_logger('InvIdx_operators')):
        self.lg = logger
        self.gateWay = JavaGateway(gateway_parameters = GatewayParameters(auto_convert = True)) # automatically convert python object to java object
        self.engine = self.gateWay.entry_point
        self.unitGenerator = Unit_generator()
        self.docProcessor = Doc_processor_tf()
        
    
    def add_doc(self, docPath):
        try:
            self.lg.debug('adding doc: %s'%docPath)
            units = self.unitGenerator.units(docPath)
            for unit in units:
                # self.lg.debug('  adding unit: %s'%unit.flatten())
                self.engine.add_posting_unit(unit.flatten())
        except:
            self.lg.warn(format_exc())
                
    
    # add all docs from one source (docs in one sub directory of /corpus)
    def add_source(self, sourcePath):
        docPathList = []
        
        for docPathInfo in os.walk(sourcePath):
            mainPath = docPathInfo[0]
            docNameList = docPathInfo[-1]
            for docName in docNameList:
                docPathList.append(os.path.join(mainPath, docName))
                
        for docPath in docPathList:
            self.add_doc(docPath)
        
        self.lg.info('source added: %s'%sourcePath)
        
        
    # add all available sources into the inverted index
    def add_all(self):
        for sourceName in cfg.sourceList:
            sourcePath = os.path.join(cfg.corpusPath, sourceName)
            self.add_source(sourcePath)
        
    
    def delete_doc(self, docPath):
        # only setting the status in the mem, not persisted
        
        affectedUnits = []
        try:
            self.lg.debug('deleting doc: %s'%docPath)
            processedDoc = self.docProcessor.process(docPath)
            
            targetTerms = processedDoc.getTerms()
            docName = processedDoc.getDocName()
            
            affectedUnits = list(self.engine.delete_doc(targetTerms, docName))
        except:
            self.lg.warn(format_exc())
        
    
        return affectedUnits
    
    
    # delete all docs from one source (docs in one sub directory of /corpus)
    def del_source(self, sourcePath):
        docPathList = []
        
        for docPathInfo in os.walk(sourcePath):
            mainPath = docPathInfo[0]
            docNameList = docPathInfo[-1]
            for docName in docNameList:
                docPathList.append(os.path.join(mainPath, docName))
                
        for docPath in docPathList:
            self.delete_doc(docPath)
        
        self.lg.info('source deleted: %s'%sourcePath)
    
    
    def search(self):
        pass
    
    
if __name__ == '__main__':
    print(type(Unit_generator))
    
    invIdxOp = InvIdx_operators()
    
    # test add_doc
#     invIdxOp.add_doc(os.path.join(cfg.testCorpusPath, '-Km-gkgaAJAx37yEHIERDg'))
    
    
    # test add_source
#     sourcePath = os.path.join(cfg.corpusPath, 'test_1')
#     invIdxOp.add_source(sourcePath)

    # test add_all
#     invIdxOp.add_all()

    # test delete_doc
    print(invIdxOp.delete_doc(cfg.corpusPath + "/test_1/EKAN4jw3LsE3631feSaA_g"))
    