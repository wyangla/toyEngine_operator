# -*- coding:utf-8 -*-
'''
Created on 11 Jul 2019

@author: wyan2
'''
# tokenizer and stopwords for Chinese documents


import sys
sys.path.append('..')

from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer


class Processor_plugin_ch():
    def __init__(self):
        self._tokenizer = None
        self._removeTerms = None
    
    
def getIns():
    return Processor_plugin_ch()