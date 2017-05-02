#!/usr/bin/env python
#-*- encoding: utf-8 -*-
'''
Created on 2017年3月15日

@author: sunying
用于读取config配置文件中的内容
'''
import os
import codecs
import ConfigParser

# 取的是被初始执行脚本所在的目录
proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "api_auth_data.ini")

class ReadConfig:
    def __init__(self):
        fd = open(configPath)
        data = fd.read()

        #  remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = ConfigParser()
        self.cf.read(configPath)

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_http(self, env,name):
        value = self.cf.get(env, name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value