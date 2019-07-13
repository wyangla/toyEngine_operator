# -*- coding:utf-8 -*-
'''
Created on 18 Oct 2018

@author: wyan2
'''
import json



class Post_unit():
    
    def __init__(self, term = 'a', currentId = -1, nextId = -1, previousId = -1, nextTermId = -1, previousTermId = -1, uProp = {}, docId = -1, status = 1):
        self.term = term
        self.currentId = currentId
        self.nextId = nextId
        self.previousId = previousId
        self.nextTermId = nextTermId
        self.previousTermId = previousTermId
        self.uProp = uProp
        self.docId = docId    # string -> long, will be filled dynamically by the engine
        self.status = status


    def flatten(self):
        # currentId, nextId, previousId, uPropJson, docId, status
        flatUnit = "%s %s %s %s %s %s %s %s %s"%(self.term, self.currentId, self.nextId, self.previousId, self.nextTermId, self.previousTermId, json.dumps(self.uProp), self.docId, self.status)
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
        pUnit.nextTermId = int(unitFields[4])
        pUnit.previousTermId = int(unitFields[5])
        pUnit.uProp = json.loads(unitFields[6])
        pUnit.docId = unitFields[7]
        pUnit.status = int(unitFields[8])
        
        return pUnit
        
        
        
if __name__ == '__main__':    
    pUnit = Post_unit.deflatten('1 -1 -1 -1 -1 -1 {"tf":1,"oh":1} -1 1')
    print(pUnit.__dict__)
    print(pUnit.flatten())
        
        
        
        