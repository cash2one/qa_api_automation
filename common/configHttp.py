#!/usr/bin/env python
#-*- encoding: utf-8 -*-
'''
Created on 2017年3月15日

@author: sunying
'''

import os,pycurl, urllib, json,sys
import requests
import re
import unittest
from excelOperation import Get_excel
import readConfig,token,expose
import assertion
import requests,os,json
#         项目路径
proDir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
confDir =  os.path.join(proDir, "config")
sys.path.append(confDir)
from requests import ConnectTimeout
try:
    from io import BytesIO
except ImportError:
    from StringIO import StringIO as BytesIO

# localReadConfig = readConfig.ReadConfig()
#         项目路径
proDir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
class ConfigHttp():

    def __init__(self):
        pass
#         global host, port, timeout
#         host = localReadConfig.get_http(env,"host")
# #         port = localReadConfig.get_http("port")
#         timeout = localReadConfig.get_http(env,"timeout")
#         self.log = Log.get_log()
#         self.logger = self.log.get_logger()
#         self.headers = {}

#         api = Testapi()
#         conf = ConfigHttp(env)
#         self.excel = Get_excel()
#         assert_test = assertion()
# 
# class Testapi():
#     def testapi_post(self,url,data):
#         results = requests.post(url,data)
#     def testapi_get(self,url,params):
#         results = requests.get(url,params)        
#         return results
class Testcase(unittest.TestCase):
    env = ""
    print env
    @classmethod
    def setUpClass(self):
#        env = sys.argv[-1]
#         print env
#         env = 'qa'
#         print env
        auth_dict = token.get_auth(Testcase.env)
        print auth_dict
        #auth_dict = token.get_auth('qa')
        self.url_prefix = auth_dict['host']
        self.auth_data = auth_dict['auth']
#         self.site_task_file = 'site_monitor_task.ini'
#         self.http_taskid = expose.obtain_task(Testcase.env, 'http', 'task_id', self.site_task_file)
#         self.http_modify_taskid = expose.obtain_task(Testcase.env, 'http_modify', 'task_id', self.site_task_file)
#         self.ent_group_id = expose.obtain_ent_group(Testcase.env, 'ent_group', 'ent_group_id', self.site_task_file)
#         self.mine_group_id = expose.obtain_mine_group(Testcase.env, 'mine_group', 'class_id', self.site_task_file)
#         self.httpId = getConfigParam.get_httpId(env)
#         self.serviceGroupId = getConfigParam.get_serviceId(env)
#         self.module_name = self.__module__
#         self.module_name = "test_site_monitor"
#         self.class_name = self.__name__
#         expose._makedirs(self.module_name, self.class_name)
#         self.test_003_create_site_monitor_task_http(self)
#         self().test_003_create_site_monitor_task_http()
        
        
    @classmethod
    def teardown_class(self):
        pass

    def setUp(self):
        print "接口测试开始"
        url_suffix = '/v2/oauth/token.json'
        self.access_token = token.get_access_token(self.url_prefix,url_suffix, self.auth_data)
        
#        self.test_003_create_site_monitor_task_http()
        
    def teardown(self):
        print "接口测试结束"
    
    def method_post(self,env,url_suffix,xls_name,assert_equal_method,get_actual_variable=''):
        global report
#         Testcase.env1 = env
#         print Testcase.env1
#         api = Testapi()
#         conf = ConfigHttp()
   
#         assert_test = assertion()
        excel = Get_excel()
        #         testFile目录路径   
        testpath = os.path.join(proDir, "testFile", xls_name)
#         print testpath
        
        testtable = excel.get_xls(env,xls_name)
#         testtable = excel.open_excel(testpath)
        testnrows = excel.get_nrows(testtable)
        for i in range(0,testnrows-1):
            testname = excel.testname(testtable,testnrows)[i]
            print '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
            print testname
            testdata = excel.testdata(testtable,testnrows)[i]
            print ' 测试数据------------'
            print type(testdata),testdata
            print ' -----------------------'
            testExpect = excel.testexpect(testtable,testnrows)[i]
            try:
                actual_result = token.pycurl_post(self.url_prefix, url_suffix, self.access_token, testdata)
                actual = expose.expose_data(actual_result)
                print '实际返回值：' 
#                 s = str(actual_result).replace('u\'','\'')  
#                 s = s.decode("unicode-escape")  
#                 print type(actual_result),actual_result
#                 print type(s),s
                print type(actual),actual
                excel.writeExcel_actual(env,xls_name,testtable,i+1,actual)
#                 testtable.write(i,3,actual)
#         locations = json.loads(expose.expose_data(actual)) 
#         for location in locations:
#                print location["task_id"]
                expect_result = testExpect
                expect = expose.expose_data(expect_result)
#                 print  expose,type(expose)
#                 print '预期返回值：' + expose
                print '预期返回值：' 
                print  type(expect_result),expect_result

#                 testActualResults = api.testapi_post(url,testdata,timeout=float(self.timeout))
                if assert_equal_method == "loose":
                    result = assertion.assert_loose_equal(actual_result, expect_result)
                    print "---------------"
                    print result
                    excel.writeExcel_result(env,xls_name,testtable,i+1,result)
                    
#                     testtable.write(i,4,result)
                else:
                    assertion.assert_strict_equal(actual_result, expect_result)
            except AttributeError,ConnectTimeout:
#                 self.logger.error("Time out!")
                return None
# 定义post方法，并提取变量
    def method_post_getVariable(self,env,url_suffix,xls_name,assert_equal_method,get_actual_variable=''):
        global report
#         Testcase.env1 = env
#         print Testcase.env1
#         api = Testapi()
#         conf = ConfigHttp()
   
#         assert_test = assertion()
        excel = Get_excel()
        #         testFile目录路径   
        testpath = os.path.join(proDir, "testFile", xls_name)
#         print testpath
        
        testtable = excel.get_xls(env,xls_name)
#         testtable = excel.open_excel(testpath)
        testnrows = excel.get_nrows(testtable)
        testnames = excel.testname(testtable,testnrows)
        print testnames
        for i in range(0,testnrows-1):
            for testname in testnames:
                testname[i]
                if testname[i] == 'get_actual_variable':
                    print testname[i]
                    print '++++++++++++++++'
                    testdata = excel.testdata(testtable,testnrows)[i]
                    print ' 测试数据------------'
                    print type(testdata),testdata
                    print ' -----------------------'
                    testExpect = excel.testexpect(testtable,testnrows)[i]
                    actual_result = token.pycurl_post(self.url_prefix, url_suffix, self.access_token, testdata)
                    print actual_result
                    actual_variable = actual_result[0]
#                     actual_variable = actual_result[0]['task_id']
#                     actual_variable = actual_result[0][get_actual_variable]
                    print actual_variable
                    print '++++++++++++++++'
                    return actual_variable
                else:
                    break
#         locations = json.loads(expose.expose_data(actual)) 
#         for location in locations:
#                print location["task_id"]


# 定义get方法
    def method_get(self,env,url_suffix,xls_name,assert_equal_method):
        print"get方法"
#         url_suffix = "/v2/site/lists.json"
#         url_params = "page=1"
#         global report
#         api = Testapi()
#         conf = ConfigHttp()
        excel = Get_excel()

#         assert_test = assertion()
        #         testFile目录路径   
        testpath = os.path.join(proDir, "testFile", xls_name)
        testtable = excel.get_xls(env,xls_name)
#         testtable = excel.open_excel(testpath)
        testnrows = excel.get_nrows(testtable)
        for i in range(0,testnrows-1):
            testname = excel.testname(testtable,testnrows)[i]
            testdata = excel.testdata(testtable,testnrows)[i]
            testExpect = excel.testexpect(testtable,testnrows)[i]
            print ' 测试数据------------'
            print testdata
            print ' -----------------------'
            try:
                actual_result = token.pycurl_get(self.url_prefix, url_suffix, self.access_token, testdata)
                actual = expose.expose_data(actual_result)
                print '实际返回值：' 
                s = str(actual_result).replace('u\'','\'')  
                s = s.decode("unicode-escape")
                print type(actual_result),actual_result
                print type(s),s
                print type(actual),actual
                excel.writeExcel_actual(env,xls_name,testtable,i+1,actual)
#         locations = json.loads(expose.expose_data(actual)) 
#         for location in locations:
#                print location["task_id"]
                expect_result = testExpect
                expect = expose.expose_data(expect_result)
#                 print  expose,type(expose)
#                 print '预期返回值：' + expose
                print '预期返回值：' 
                print  type(expect_result),expect_result
#                 testActualResults = api.testapi_get(url,testdata,timeout=float(self.timeout))
                if assert_equal_method == "loose":
                    assertion.assert_loose_equal(actual_result, expect_result)
                    result = assertion.assert_loose_equal(actual_result, expect_result)
                    print "---------------"
                    print result
                    excel.writeExcel_result(env,xls_name,testtable,i+1,result)
                else:
                    assertion.assert_strict_equal(actual_result, expect_result)
            except AttributeError,ConnectTimeout:
                self.logger.error("Time out!")
                return None

# 获取token方法
    def get_access_token(self,url_suffix, auth_data):
        buffer = BytesIO()
        header = BytesIO() 
#         url_suffix = '/v2/oauth/token.json'
        c = pycurl.Curl()
        c.setopt(c.URL, self.url_prefix + url_suffix)
    #c.setopt(c.VERBOSE, True)
    #c.setopt(c.POST, False)
        c.setopt(c.SSL_VERIFYPEER, False)
        c.setopt(c.POSTFIELDS, urllib.urlencode(auth_data))
        c.setopt(c.WRITEFUNCTION, buffer.write)
        c.setopt(c.HEADERFUNCTION, header.write)
        try:
            c.perform()
            result_str = buffer.getvalue()
            resutl_header = header.getvalue()
            result_code = c.getinfo(c.HTTP_CODE)
        except Exception, e:
            c.close()
            buffer.close()
            header.close()
            raise Exception, e
        c.close()
        if result_str and isinstance(result_str, (list, dict, str, int)):
            result_dic = json.loads(result_str)
            print("\n\nAccess_token:"), (result_dic["access_token"]), ("\n")
            return result_dic["access_token"]
        else:
            if result_code == 200:
                raise AssertionError("None returned from request URI, please check it manually.")
            else:
                msg = "Connection error to request URI with http_code %s, please check it manually." %result_code
                raise AssertionError(msg)
