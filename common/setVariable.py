#!/usr/bin/python
 #-*-coding:utf-8-*-  
'''
Created on 2017年2月10日

@author: sunying
'''
import time
class LocalTime:
    def getLocalTime(self):
        localTime = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
#         print localTime
        return  localTime
if __name__ == "__main__":
    a =LocalTime()
    a.getLocalTime()
         