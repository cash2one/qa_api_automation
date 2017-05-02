#!/usr/bin/python
#-*- coding: utf-8  -*- 
#测试套件，可以加入多个测试集

import unittest,doctest,os
from datetime import datetime
from testCase import test_site_monitor
from common import HTMLTestRunner
import sys
reload(sys)
import shutil
# from sys import argv
# script,env1 = argv
# test_env = env1
# sys.setdefaultencoding('utf-8')
suite = doctest.DocTestSuite  
suite = unittest.TestSuite()  
# suite.addTest(unittest.makeSuite(test_site_monitor.TestSiteMonitorSmoke))#引入测试的类，测试用例就被包含在类中  
suite.addTest(unittest.makeSuite(test_site_monitor.TestSiteMonitorSmoke))
# suite.addTest(unittest.makeSuite(test_user_manage_demo. TestUserManageSmoke))
# suite.addTest(unittest.makeSuite(test_site_monitor_demo.TestSiteMonitorSmoke))
# suite.addTest(unittest.makeSuite(regWithDevice.testRegWithDevice))  
#unittest.TextTestRunner(verbosity=2).run(suite) #这是只运行，不生成报告的做法  
#         当前路径
proDir = os.getcwd()
#         report目录路径

reportPath = os.path.join(proDir, "report")
report_datePath = os.path.join(reportPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))
        # create test result file if it doesn't exist
if not os.path.exists(report_datePath):
            os.mkdir(report_datePath)
reportFile = os.path.join(report_datePath, "result.html")
fp = file(reportFile,'wb') #定义报告文件权限，wb，表示有读写权限  
runner = HTMLTestRunner.HTMLTestRunner(  
        stream = fp,  
        title ='接口测试报告',  
        description = '测试用例见下表：')  
  
runner.run(suite)#执行测试  
fp.close()#关闭文件，否则会无法生成文件 
shutil.copy(reportFile,reportPath)  