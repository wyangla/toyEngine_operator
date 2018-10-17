# -*- coding:utf-8 -*-
'''
Created on 17 Oct 2018

@author: wyan2
'''



from __future__ import absolute_import
import configs as cfg
import importlib
import json



# process the generation of Doc_processor
# to form the flatPostUnit string
class Unit_generator():
    
    def __init__(self):
        pass
    
    def pUnit_properties(self, docPath):
        docName = ""
        uProp4Terms = {}
        for propField in cfg.uPropFields:
            calculatorPath = cfg.uPropFields[propField] # 
            propCalculator = importlib.import_module('.', calculatorPath).getIns()
            propGenerator = propCalculator.cal(docPath) # generator
            
            for docName, term, propDict in propGenerator:
                if uProp4Terms.get(term) is None:
                    uProp4Terms[term] = propDict # the result of first property calculator
                else:
                    uProp4Terms[term].update(propDict) # merge the result of following property calculators
                     
        return docName, uProp4Terms 
            
            
    def flat_units(self, docPath):
        docName, uProp4Terms = self.pUnit_properties(docPath)
        for term in uProp4Terms:
            uPropJson = json.dumps(uProp4Terms[term])
            flatUnit = "%s %s %s %s %s %s %s"%(term, -1, -1, -1, uPropJson, docName, 1) # currentId, nextId, previousId, uPropJson, docId, status
            yield term, flatUnit # for the convenience of check the existance of term in inverted-index
        
        

if __name__ == '__main__':
    import os
    UProp_generatorIns = Unit_generator()
    docPath = os.path.join(cfg.testCorpusPath, '-Km-gkgaAJAx37yEHIERDg')
#     print(UProp_generatorIns.pUnit_properties(docPath))
    for i in UProp_generatorIns.flat_units(docPath):
        print(i)
    
    