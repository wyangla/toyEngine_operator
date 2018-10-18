# -*- coding:utf-8 -*-
'''
Created on 18 Oct 2018

@author: wyan2
'''
import json



class Post_unit():
    
    def __init__(self, term = 'a', currentId = -1, nextId = -1, previousId = -1, uProp = {}, docId = 'f', status = 1):
        self.term = term
        self.currentId = currentId
        self.nextId = nextId
        self.previousId = previousId
        self.uProp = uProp
        self.docId = docId
        self.status = status


    def flatten(self):
        # currentId, nextId, previousId, uPropJson, docId, status
        flatUnit = "%s %s %s %s %s %s %s"%(self.term, self.currentId, self.nextId, self.previousId, json.dumps(self.uProp), self.docId, self.status)
        flatUnit = flatUnit.replace(": ", ":") # as the {} cannot contain the space inside, contract
        flatUnit = flatUnit.replace(", ", ",")
        return flatUnit
    
    
    @classmethod
    def deflatten(cls, flatUnit):
        pUnit = cls()
        unitFields = flatUnit.split(" ")
        
        pUnit.term = unitFields[0]
        pUnit.currentId = int(unitFields[1])
        pUnit.nextId = int(unitFields[2])
        pUnit.previousId = int(unitFields[3])
        pUnit.uProp = json.loads(unitFields[4])
        pUnit.docId = unitFields[5]
        pUnit.status = int(unitFields[6])
        
        return pUnit
        
        
        
if __name__ == '__main__':    
    pUnit = Post_unit.deflatten('1 -1 -1 -1 {"tf":1,"oh":1} /test_1/JCna3sfrjqtnsG7l-pSs-A 1')
    print(pUnit.__dict__)
    print(pUnit.flatten())
        
        
        
        