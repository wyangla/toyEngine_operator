# -*- coding:utf-8 -*-
'''
Created on 17 Aug 2019

@author: wyan2
'''
import numpy as np
import traceback


class Task_spliter():
    def __init__(self):
        pass
    
    @classmethod
    def get_workLoads_terms(cls, chunkNum, targetList):
        workloads = []
        workloadNum = np.ceil(len(targetList) / chunkNum)
        targetIterator = iter(targetList)
        
        for _ in range(chunkNum):
            chunk = []
            
            while(True):
                try:
                    chunk.append(next(targetIterator))
                    if len(chunk) >= workloadNum:
                        break 
                    
                except StopIteration:
                    # print(traceback.format_exc())
                    break
                
            workloads.append(chunk)
                
        return workloads
    
    
    
    
if __name__ == "__main__":
    print(Task_spliter.get_workLoads_terms(3, [1,2,3,4,5]))
                
                
                
                
                
                
                
                
                
                