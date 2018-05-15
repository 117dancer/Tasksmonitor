# -*- coding: utf-8 -*- 
#__author__='fanweiming'
#__time__ ='2018/4/18 18:00'


def log1():
    import logging
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='myapp.log',
                    filemode='w')
    return logging
