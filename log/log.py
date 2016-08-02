# -*- coding: utf-8 -*- 
'''
Created on 16/7/28

@author: leng

'''

import logging


class Log():
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s %(threadName)s [%(levelname)s] %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename='TestJDRegister.log',
                            filemode='a')  # 设置日志格式

        console = logging.StreamHandler()  # 设置日志同步输出到控制台
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s %(filename)s %(threadName)s [%(levelname)s] %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)

    def loginfo(self, msg):
        logging.info(msg)

    def logerror(self, msg):
        logging.error(msg)
