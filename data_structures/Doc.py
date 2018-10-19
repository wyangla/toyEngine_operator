# -*- coding:utf-8 -*-
'''
Created on 19 Oct 2018

@author: wyan2
'''
from collections import Counter


class Doc():
    
    def __init__(self, docName = " ", termCounter = Counter()):
        self._docName = docName
        self._termCounter = termCounter
        
    def getDocName(self):
        return self._docName
    
    def getTermCounter(self):
        return self._termCounter
    
    def getTerms(self):
        return list(self._termCounter.keys())
    
    
    
if __name__ == '__main__':
    d = Doc("d1")
    d._termCounter.update({"a":2, "b":3})
    
    print(d.getTermCounter())
    print(d.getTerms())
    
    
    
    