# -*- coding:utf-8 -*-
'''
Created on 17 Oct 2018

@author: wyan2
'''


import sys
sys.path.append('..')

from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import configs as cfg
import os
from data_structures import Doc



# process the document and provide the term frequency information
class Doc_processor_tf():
    def __init__(self):
        self._tokenizer = RegexpTokenizer(r'\w+')
        self._removeTerms = stopwords.words('english')


    def _tokenize(self, doc):
        terms = self._tokenizer.tokenize(doc)
        terms = list(map(lambda string : string.lower(), terms))
        for t in terms:
            if t in self._removeTerms: # remove the stop words
                terms.remove(t)
        return terms


    def getDocName(self, docPath = ""):
        docName = docPath.replace(cfg.corpusPath, '').replace('\\', '/')
        return docName
     
     
    # root/corpus/source/docNames
    # the docName is the relative path
    # /source/name
    def process(self, docPath = ""):
        termCounter = Counter()
        with open(docPath, 'r') as f:
            doc = f.read()
        terms = self._tokenize(doc)
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
    dp = Doc_processor_tf()
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
    
    
    
    
    
    