# -*- coding:utf-8 -*-
'''
Created on 11 Jul 2019

@author: wyan2
'''
# TODO: language detection, the unified wrapper of different languages



import sys
sys.path.append('..')

from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import configs as cfg
import os
from data_structures import Doc
import importlib



# process the document and provide the term frequency information
class Doc_processor():
    def __init__(self):
        self._tokenizer = None    # dynamically get from plugin s
        self._removeTerms = None
        
        
    def _tokenize(self, doc):
        terms = self._tokenizer.tokenize(doc)
        terms = list(map(lambda string : string.lower(), terms))
        for t in terms:
            if t in self._removeTerms: # remove the stop words
                terms.remove(t)
        return terms


    def getDocName(self, docPath = ""):    # full docName, i.e. with source path. e.g. /test_1/EKAN4jw3LsE3631feSaA_g
        docName = docPath.replace(cfg.corpusPath, '').replace(os.sep, '/') # manually change to linux style is for avoid \t in windows
        return docName
    
    
    def getSubDocNameDirPath(self, docPath = ""):
        docName = self.getDocName(docPath)
        sepIdx = docName.rfind('/')
        subDocName =  docName[sepIdx + 1:]    # not start with /
        return subDocName
    
     
    def _detect_language(self, doc):
        languageNam = 'English'
        return languageNam
     
     
    # store the doc processing result to the same directory as the raw document
    def _persist_processed(self, terms, docPath):
        processedDoc = ' '.join(terms)
        docFullName = self.getDocName(docPath)
        
        with open(cfg.cachedFilePath + os.sep + docFullName, 'w') as f:    # '__adfasfa'
            f.write(processedDoc)
        
     
    # root/corpus/source/docNames
    # the docName is the relative path
    # /source/name
    def process(self, docPath = ""):
        termCounter = Counter()
        with open(docPath, 'r') as f:
            doc = f.read()
            
        languageName = self._detect_language(doc)    # default to be English
        processorPluginPath = cfg.languageProcessorMap[languageName]
        processorPluginIns = importlib.import_module('.', processorPluginPath).getIns() # processor_plugin.en
        self._tokenizer = processorPluginIns._tokenizer
        self._removeTerms = processorPluginIns._removeTerms
        
        terms = self._tokenize(doc)
        self._persist_processed(terms, docPath)
        
        termCounter.update(terms) # ("/source/name", {"a":1, ..})
        docName = self.getDocName(docPath)
        
        doc = Doc(docName, termCounter);
        return doc
     
     
         
if __name__ == '__main__':
    # get the all the doc paths
    docPathList = []
    for docPathInfo in os.walk(cfg.corpusPath):
        mainPath = docPathInfo[0]
        docNameList = docPathInfo[-1]
        for docName in docNameList:
            docPathList.append(os.path.join(mainPath, docName))
            
            
    # process 10 docs for illustration
    dp = Doc_processor()
    cnt = 0
    for docPath in docPathList:
        doc = dp.process(docPath)
        docName = doc.getDocName()
        counterTemp = doc.getTermCounter() 
        print(docName)
        print(counterTemp)
        print()
        
        cnt += 1
        if cnt == 10:
            break
    