#!/usr/bin/env python
#-*- encoding: utf-8 -*-
'''
Created on 2017年3月15日

@author: sunying
'''

import xlrd
from xlrd import open_workbook
from xlutils.copy import copy
import xlwt
import json,os
import sys
class Get_excel:
    def get_xls(self,env,xls_name):
        #         项目路径
        proDir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        # 从excel文件中读取测试用例
        cls = []
        #         testFile目录路径   
        xlsFile = os.path.join(proDir, "testFile", xls_name)
        print xlsFile
#         open xls file
        workbook = open_workbook(xlsFile)
#         workbook = open_workbook(xlsFile,formatting_info=True)
#qa环境数据
        if "qa"  in env :
            sheet = workbook.sheets()[0]
            return sheet
# beta环境数据
        elif "beta"  in env :
            sheet = workbook.sheets()[1]
            return sheet
# prod环境数据
        else:
            sheet = workbook.sheets()[2]
            return sheet
#     #获取sheet
#     def open_excel(self,path):
#         workbook = xlrd.open_workbook(path)
#         table = workbook.sheets()[0]
#         return table

     #获取行号
    def get_nrows(self,sheet):
         nrows = sheet.nrows
         return nrows
 
    def testname(self,table,nrows):
         TestName = []
         for i in range(1,nrows):
             TestName.append(table.cell(i,0).value)
#          print TestName
         return TestName
     #获取用例name
     
     #获取data接口参数
    def testdata(self,table,nrows):
        TestData = []
        for i in range(1,nrows):
            if table.cell(i,1).value == '':
                TestData.append('')
            else:
                data = json.loads(table.cell(i,1).value)
                TestData.append(data)
#         print TestData
        return TestData
 # actual值写excel
    def writeExcel_actual(self,env,xls_name,table,nrows,actual_str):  
#         项目路径
        proDir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
#         testFile目录路径   
        xlsFile = os.path.join(proDir, "testFile", xls_name)
        xlsFile1 = os.path.join(proDir, "testFile", "1.xls")
#         print xlsFile
#         open xls file

        print '写入开始。。。。。。。。。'
        rb = xlrd.open_workbook(xlsFile)
        wb = copy(rb)  
        print '写入开始1。。。。。。。。。'
# qa环境数据
        if "qa"  in env :
            ws = wb.get_sheet(0)  
# beta环境数据
        elif "beta"  in env :
            ws = wb.get_sheet(1)  
# prod环境数据
        else:
            ws = wb.get_sheet(2)  
        print ws
        print '写入开始2。。。。。。。。。'
#         print actual_str
#         actual = actual_str.decode('unicode_escape').encode('utf-8')
        actual_str = str(actual_str).replace('u\'','\'')  
#         s = s.decode("unicode-escape")  
        print type(actual_str),actual_str
        print actual_str
        ws.write(nrows, 3, actual_str) 
        print '写入开始3。。。。。。。。。'
        wb.save(xlsFile)  
        print '写入结束。。。。。。。。。'
# 测试是否通过（result）值写excel
    def writeExcel_result(self,env,xls_name,table,nrows,assert_result):  
        #         项目路径
        proDir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
#         testFile目录路径   
        xlsFile = os.path.join(proDir, "testFile", xls_name)
        xlsFile1 = os.path.join(proDir, "testFile", "1.xls")
#         print xlsFile
#         open xls file

        print '写入开始。。。。。。。。。'
        rb = xlrd.open_workbook(xlsFile)
        wb = copy(rb)  
                
        style = xlwt.easyxf(
    "font: name Arial;"
    "pattern: pattern solid, fore_colour red;"
    )
        print '写入开始1。。。。。。。。。'
# qa环境数据
        if "qa"  in env :
            ws = wb.get_sheet(0)  
# beta环境数据
        elif "beta"  in env :
            ws = wb.get_sheet(1)  
# prod环境数据
        else:
            ws = wb.get_sheet(2)  
        print ws
        print '写入开始2。。。。。。。。。'
#         print actual_str
#         actual = assert_result.decode('unicode_escape').encode('utf-8')
        print assert_result
        ws.write(nrows, 4, assert_result,style) 
        print '写入开始3。。。。。。。。。'
        wb.save(xlsFile)  
        print '写入结束。。。。。。。。。'

#  获取expect值
    def testexpect(self,table,nrows):
        TesteExpect = []
        for i in range(1,nrows):
            if table.cell(i,2).value == '':
                TesteExpect.append('')
            else:
                data = json.loads(table.cell(i,2).value)
                TesteExpect.append(data)
#         print TesteExpect
        return TesteExpect            
           

#     expect_key =  fd.keys()
#     print expect_key
#     return dict2
        return TesteExpect
     #获取用例期望的运行结果
 
if __name__ == "__main__":
    pass
#      Create_excel''()