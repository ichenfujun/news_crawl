#!/usr/local/bin/python2.7
'''
@author: rhc
'''

import logging,sys,time,os
import scrapy.cmdline

def main():
    
#     if len(sys.argv)==1:
#         raise Exception('argv error')
    
    name= 'ccgp' #sys.argv[1]
    
    log_path='%s%s'%('./logs/',name)
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    
    filename = '%s/%s.%s%s' % (log_path,name,time.strftime("%Y%m%d", time.localtime()),'.log')
    logging.basicConfig(filename=filename, format='[%(asctime)s]%(levelname)s:%(message)s', filemode='a')
    
#     scrapy.cmdline.execute(argv=['scrapy', 'crawl','Super', '-a','name=%s' % name])
    scrapy.cmdline.execute(argv=['scrapy', 'crawl','ccgp',])

if  __name__ =='__main__':
    main()
