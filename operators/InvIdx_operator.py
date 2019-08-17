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
from logger import Logger
from traceback import format_exc
from processors import Doc_processor
from utils import *
from multiprocessing import Pool



class InvIdx_operators():
    
    def __init__(self, logger = None):
        self.lg = logger or Logger.get_logger('InvIdx_operators')
        self.gateWay = JavaGateway(gateway_parameters = GatewayParameters(auto_convert = True)) # automatically convert python object to java object
        self.engine = self.gateWay.entry_point
        self.unitGenerator = Unit_generator()
        self.docProcessor = Doc_processor()
        
    
#     def add_doc(self, docPath):
#         try:
#             self.lg.debug('adding doc: %s'%docPath)
#             units = self.unitGenerator.units(docPath)
#             for unit in units:
#                 # self.lg.debug('  adding unit: %s'%unit.flatten())
#                 self.engine.add_posting_unit(unit.flatten())
#         except:
#             self.lg.warn(format_exc())
                
                
    def add_doc(self, docPathList):
        self._add_doc(docPathList)
                
                
    @classmethod
    def _add_doc(cls, docPathList):
        self = cls()
        # compatible with the previous single doc name input
        if type(docPathList) == type(""):
            docPathList = [docPathList]
            
        for docPath in docPathList:
            try:
                docName = self.docProcessor.getDocName(docPath)    # full docName, e.g. /test_1/EKAN4jw3LsE3631feSaA_g
                if not cfg.processedDocNamePrefix in docName:
                    
                    self.lg.debug('adding doc: %s'%docPath)
                    units = self.unitGenerator.units(docPath)
                    
                    persistedUnits = []
                    for unit in units:
                        persistedUnits.append(unit.flatten())
                    
                    # print(persistedUnits)    # TODO: test
                    self.engine.add_doc(persistedUnits, docName)
                    
                else:
                    pass    # processed file
            except Exception as e:
                self.lg.warn(format_exc())

    
    # add all docs from one source (docs in one sub directory of /corpus)
    # TODO: change to multi-processing, need the logic of dividing the work load
    def add_source(self, sourcePath):
        docPathList = []
        
        for docPathInfo in os.walk(sourcePath):
            mainPath = docPathInfo[0]
            docNameList = docPathInfo[-1]
            for docName in docNameList:
                docPathList.append(os.path.join(mainPath, docName))
                
        workloads = Task_spliter.get_workLoads_terms(cfg.cpuNum, docPathList)
        p = Pool(cfg.cpuNum)
        
        for workload in workloads:
            print('-->')
            print(workload)
            p.apply_async(func=InvIdx_operators._add_doc, args = (workload,))
        
        p.close()
        p.join()

#         for docPath in docPathList:
#             self.add_doc(docPath)
        
        self.lg.info('source added: %s'%sourcePath)
        
        
    # add all available sources into the inverted index
    def add_all(self):
        for sourceName in cfg.sourceList:
            sourcePath = os.path.join(cfg.corpusPath, sourceName)
            self.add_source(sourcePath)
        
    
    # TODO: change
    def delete_doc(self, docPath):
        # only setting the status in the mem, not persisted
         
        affectedUnits = []
        try:
            self.lg.debug('deleting doc: %s'%docPath)
            docName = self.docProcessor.getDocName(docPath)    # docName with source
            
            if not cfg.processedDocNamePrefix in docName:    # delete also make use of the original name, the __proc__ should be transparent to the user
                
                subDocName = self.docProcessor.getSubDocNameDirPath(docPath)    # only the lowest layer, no source dir path
                processedDocPath = docPath.replace(subDocName, cfg.processedDocNamePrefix + subDocName)
                with open(processedDocPath, 'r') as f:
                    targetTerms = f.read().split(' ')    # get target terms from the processed files instead of process them again
                
                affectedUnits = list(self.engine.delete_doc(targetTerms, docName))
                
            else:
                pass
        except:
            self.lg.warn(format_exc())
         
     
        return affectedUnits

#     def delete_doc(self, docPath):
#         # only setting the status in the mem, not persisted
#         
#         affectedUnits = []
#         try:
#             self.lg.debug('deleting doc: %s'%docPath)
#             docName = self.docProcessor.getDocName(docPath)
#             affectedUnits = list(self.engine.delete_doc(docName))
#         except:
#             self.lg.warn(format_exc())
#         
#     
#         return affectedUnits
    
    
    # delete all docs from one source (docs in one sub directory of /corpus)
    # TODO: change to multi-processing, need the logic of dividing the work load
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
    
    
    # search without further ranking
    def search(self, queryTerms = []):
        relatedDocumentScores = dict(self.engine.search(queryTerms))
        for doc, score in relatedDocumentScores.items():
            print(doc + '\t' + str(score))
        
    
    def show(self):
        print(self.engine.show())
        
    def persist_index(self):
        self.engine.persist_index()
    
    
    
if __name__ == '__main__':
#     print(type(Unit_generator))
    
    invIdxOp = InvIdx_operators()
    
    # test add_doc
    # and cal_termIdf
    invIdxOp.add_doc(os.path.join(cfg.testCorpusPath, 'test_doc_len_1'))
    invIdxOp.add_doc(os.path.join(cfg.testCorpusPath, 'test_doc_len_2'))
    invIdxOp.add_doc(os.path.join(cfg.testCorpusPath, 'test_doc_len_3'))
    
    
    # test add_source
#     sourcePath = os.path.join(cfg.corpusPath, 'test_3')
#     invIdxOp.add_source(sourcePath)

    # test add_all
#     invIdxOp.add_all()
    invIdxOp.persist_index()
    
    # test delete_doc
#     print(invIdxOp.delete_doc(cfg.corpusPath + "/test_1/EKAN4jw3LsE3631feSaA_g"))
#     print(invIdxOp.delete_doc(cfg.corpusPath + "/test_2/lsoSqIrrDbQvWpMvsSj2xw"))   # term_max_tf of "wanted" 2 -> 1

    
    # test search
#     import time
#     t1 = time.time()
#     invIdxOp.search(["wanted", "tasty", "asdfasdfa"]) # 51TLGhFncBnppaBN5vHlcw; wanted tf 1 df 6; N 100; tfidf 2.4507285734080293
#     t2 = time.time()
#     invIdxOp.lg.info("searching takes: %ss"%(str(t2 - t1)))
    
    # test delete_source
#     import time
#     t1 = time.time()
#     invIdxOp.del_source(cfg.corpusPath + "/test_1")
#     invIdxOp.del_source(cfg.corpusPath + "/test_2")
#     t2 = time.time()
#     invIdxOp.lg.info("deleting takes: %ss"%(str(t2 - t1)))
#     invIdxOp.engine.reload_index()
      