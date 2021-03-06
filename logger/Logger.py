# -*- coding:utf-8 -*-
'''
Created on 18 Oct 2018

@author: wyan2
'''


# import sys
# sys.path.append('..')
from logging import getLogger, Formatter
from logging import handlers, StreamHandler
import configs as cfg



class Logger():
    
    @classmethod
    def get_logger(self, name = 'test'):
        lg = getLogger(name)
        lg.setLevel(cfg.logLevel)
        
        if not lg.handlers:    # ref: https://stackoverflow.com/questions/6729268/log-messages-appearing-twice-with-python-logging
            fmt = Formatter('%(asctime)s [%(levelname)s] - %(filename)s:%(lineno)s %(message)s')
            
            fhandler = handlers.RotatingFileHandler('./' + name + '.log', mode = 'a', maxBytes = 1024 * 1024, backupCount = 3)
            fhandler.setFormatter(fmt)
            
            shandler = StreamHandler()
            shandler.setFormatter(fmt)
            
            lg.addHandler(fhandler)
            lg.addHandler(shandler)
        
        return lg
    
    
    
if __name__ == '__main__':
    lg = Logger.get_logger('test_1')
    lg.info('test logger')
    
    