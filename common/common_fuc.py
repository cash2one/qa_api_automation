#!/usr/bin/env python
#-*- encoding: utf-8 -*-
'''
Created on 2017年3月15日

@author: sunying
'''
import os
from xlrd import open_workbook
from xml.etree import ElementTree as ElementTree
# from Log import MyLog as Log
# from configHttp import ConfigHttp
# localConfigHttp = ConfigHttp()
# log = Log.get_log()
# logger = log.get_logger()
#         项目路径
proDir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
# 从excel文件中读取测试用例
def get_xls(xls_name, sheet_name):
    cls = []
    # get xls file's path
#         testFile目录路径   
    xlsFile = os.path.join(proDir, "testFile", xls_name)
    print xlsFile
    # open xls file
    file = open_workbook(xlsFile)
    # get sheet by name
    sheet = file.sheet_by_name(sheet_name)
    # get one sheet's rows
    #获取行数
    nrows = sheet.nrows
    #循环获取每行中的数据
    for i in range(nrows):
        if sheet.row_values(i)[0] != u'case_name':
            cls.append(sheet.row_values(i))
    print cls
    print cls[0][0]
    return cls

# 从xml文件中读取sql语句
database = {}
def set_xml():
    if len(database) == 0:
        sql_path = os.path.join(proDir, "testFile", "SQL.xml")
        tree = ElementTree.parse(sql_path)
        for db in tree.findall("database"):
            db_name = db.get("name")
            # print(db_name)
            table = {}
            for tb in db.getchildren():
                table_name = tb.get("name")
                # print(table_name)
                sql = {}
                for data in tb.getchildren():
                    sql_id = data.get("id")
                    # print(sql_id)
                    sql[sql_id] = data.text
                table[table_name] = sql
            database[db_name] = table

def get_xml_dict(database_name, table_name):
    set_xml()
    database_dict = database.get(database_name).get(table_name)
    return database_dict

def get_sql(database_name, table_name, sql_id):
    db = get_xml_dict(database_name, table_name)
    sql = db.get(sql_id)
    return sql
if __name__ == '__main__':
    get_xls("token_data.xlsx", "site_create")