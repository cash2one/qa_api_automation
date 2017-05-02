#!/usr/bin/env python
# encoding: utf-8 

import sys,os,unittest
from sys import argv
if ".." not in sys.path:
	sys.path.append("..")
proDir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(proDir)
confDir =  os.path.join(proDir, "config")
sys.path.append(confDir)
# print confDir
from common.configHttp import Testcase
# import testsuit
class TestSiteMonitorSmoke(Testcase):
# 	env = Testcase.env = testsuit.test_env
	env = Testcase.env = 'qa'
# 	script,argv_env = argv
# 	env = Testcase.env = argv_env
# 	print Testcase.env
# 	def __init__(self):
# 		self.env = "qa"
# 	@unittest.skip('暂不执行此用例')
	def test_003_create_site_monitor_task_http(self):
		xls_name = "site_create_data.xls"
		url_suffix = "/v2/site/create.json'"
		assert_equal_method = "loose"
		self.method_post(TestSiteMonitorSmoke.env,url_suffix, xls_name,assert_equal_method)
	def test_002_get_site_monitorPoint_list(self):
		xls_name = "site_getMonitors_data.xls"
		url_suffix = "/v2/site/monitors.json"
		assert_equal_method = "loose"
		self.method_get(TestSiteMonitorSmoke.env,url_suffix, xls_name,assert_equal_method)		

	def test_001_get_site_monitor_task_info(self):
		xls_name = "site_create_data.xlsx"
		url_suffix = "/v2/site/create.json'"
		assert_equal_method = "loose"
		task_id = self.method_post_getVariable(TestSiteMonitorSmoke.env,url_suffix, xls_name,assert_equal_method,"task_id")
		print task_id
# 		xls_name = "site_getTaskInfo_data.xlsx"
# 		url_suffix = "/v2/site/info/"+task_id+".json"
# 		assert_equal_method = "loose"
# 		self.method_get(TestSiteMonitorSmoke.env,url_suffix, xls_name,assert_equal_method)		

# 构造测试集
def suite():
	suite = unittest.TestSuite()
	
	suite.addTest(TestSiteMonitorSmoke("test_002_get_site_monitorPoint_list"))
# 	suite.addTest(TestSiteMonitorSmoke("test_003_create_site_monitor_task_http"))
# 	suite.addTest(TestSiteMonitorSmoke("test_001_get_site_monitor_task_info"))


	return suite
# 测试
if __name__ == "__main__":
# 	pass
	unittest.main(defaultTest = 'suite')
#  	 执行测试
# 	runner = unittest.TextTestRunner()
# 	runner.run(suite)
	