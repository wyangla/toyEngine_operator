# -*- coding:utf-8 -*-
'''
Created on 17 Oct 2018

@author: wyan2
'''


import sys
sys.path.append('..')

from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer


class Processor_plugin_en():
    def __init__(self):
        self._tokenizer = RegexpTokenizer(r'\w+')
        self._removeTerms = stopwords.words('english')
    
    
def getIns():
    return Processor_plugin_en()