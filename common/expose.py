#!/usr/bin/env python
#-*- encoding: utf-8 -*-
import sys
if ".." not in sys.path:
	sys.path.append("..")
import os,sys,json,time,random
import ConfigParser
# from Date import getCurrentDate
def expose_data(fuzzy_data):
	visual_data = str(fuzzy_data).decode('unicode_escape').encode('utf-8')
	#visual_data = json.dumps(fuzzy_data).decode('unicode_escape')
	return visual_data
	
def obtain_auth(env):
	print env
	conf = ConfigParser.ConfigParser()
	conf.read('/test/config/auth_data.ini')
	#aecs = conf.sections()
	#opts = conf.options(env)
	itms = conf.items(env)
	conf_auth = conf.get(env, 'auth')
	auth_dict = {itms[0][0]:itms[0][1], itms[1][0]:json.loads(conf_auth)}
	return auth_dict
	#print itms, type(itms[0]), type(itms[1][1])
	#print conf_auth, type(conf_auth), "+"*10
	#str_val = cf.get("sec_a", "a_key1") 
	#int_val = cf.getint("sec_a", "a_key2") 
	##create a new section 
	#cf.add_section('a_new_section') 
	##set a new value 
	#cf.set('a_new_section', 'new_key', 'new_value') 
	##write back to configure file 
	#cf.write(open("test.conf", "w"))

def obtain_task_old(env, task_type):
	conf = ConfigParser.ConfigParser()
	conf.read('/test/config/site_monitor_task.ini')
	#aecs = conf.sections()
	#opts = conf.options(env)
	#itms = conf.items(env)
	conf_file = conf.get(env, 'service_task_file')
	if not os.path.isfile('../config/%s' %conf_file):
		raise IOError('No such configuration file: %s' % conf_file)
	full_file = '../config/%s' % conf_file
	conf = ConfigParser.ConfigParser()
	conf.read(full_file)
	itms = conf.items(task_type)
	task_id = conf.get(task_type, 'task_id')
	print('Task_ID:'), (task_id)
	return task_id

def obtain_task(env, option, key, ini_file):
	# 获取上层文件路径
	dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
# 	print dir
	conf = ConfigParser.ConfigParser()
	conf.read(dir+'/config/' + ini_file)
# 	s = conf.sections()
# 	print 'section:',s
# 	s = env
# 	print s
	itms = conf.items(env)
	task_str = conf.get(env, option)
	task = json.loads(task_str)
	return task[key].encode('utf-8')

def obtain_ent_group(env, option, key, ini_file):
	# 获取上层文件路径
	dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
# 	print dir
	conf = ConfigParser.ConfigParser()
	conf.read(dir+'/config/' + ini_file)
# 	s = conf.sections()
# 	print 'section:',s
# 	s = env
# 	print s
	itms = conf.items(env)
	task_str = conf.get(env, option)
	task = json.loads(task_str)
	return task[key].encode('utf-8')

def obtain_mine_group(env, option, key, ini_file):
	# 获取上层文件路径
	dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
# 	print dir
	conf = ConfigParser.ConfigParser()
	conf.read(dir+'/config/' + ini_file)
# 	s = conf.sections()
# 	print 'section:',s
# 	s = env
# 	print s
	itms = conf.items(env)
	task_str = conf.get(env, option)
	task = json.loads(task_str)
	return task[key].encode('utf-8')
	
def obtain_user(env, option, key, ini_file):
	# 获取上层文件路径
	dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
	print dir
	conf = ConfigParser.ConfigParser()
	conf.read(dir+'/config/' + ini_file)
# 	s = conf.sections()
# 	print 'section:',s
# 	s = env
# 	print s
	itms = conf.items(env)
	task_str = conf.get(env, option)
	task = json.loads(task_str)
	return task[key].encode('utf-8')
	
	#auth_dict = {itms[0][0]:itms[0][1], itms[1][0]:json.loads(conf_auth)}
	#return auth_dict
	#print itms, type(itms[0]), type(itms[1][1])
	#print conf_auth, type(conf_auth), "+"*10
	#str_val = cf.get("sec_a", "a_key1") 
	#int_val = cf.getint("sec_a", "a_key2") 
	##create a new section 
	#cf.add_section('a_new_section') 
	##set a new value 
	#cf.set('a_new_section', 'new_key', 'new_value') 
	##write back to configure file 
	#cf.write(open("test.conf", "w"))
def load_post(module_name=None, class_name=None, post_file=None, type=''):
	if not module_name or not class_name:
		expath = os.getcwd()
	else:
		expath = os.getcwd() + '/post_data/' + module_name +'/'+ class_name +'/'
	test_name = sys._getframe().f_back.f_code.co_name 
	if not post_file:
		filename = expath + test_name + '_post.json'
		print '----------'+filename
	else:
		filename = expath + post_file
		print '----------'+filename
	fo = open(filename, 'r')
	fs = fo.read()
	fo.close()
	fd = json.loads(fs)
	print  fd
	return fd
'''
#     json转字符串
	line_json = json.dumps(fd)
	print line_json
	locTime = LocalTime()
#     字符串中内容替换
	line_json_replace =  line_json.replace("vivi",locTime.getLocalTime()+type).replace("email@163.com",'api_creat_'+str(random.randint(1,100))+'@163.com');
# 	line_json_replace =  line_json_replace1.replace("email@163.com",'api_creat_'+str(random.randint(1,100))+'@163.com');
	print line_json_replace
#     字符串转json
	json_replace = json.loads(line_json_replace)
	print  json_replace
	return json_replace
'''

def load_expect(module_name=None, class_name=None, expect_file=None):
	if not module_name or not class_name:
		expath = os.getcwd()
	else:
		expath = os.getcwd() + '/expect_result/' + module_name +'/'+ class_name +'/'
	test_name = sys._getframe().f_back.f_code.co_name 
	if not expect_file:
		#filename = expath + test_name + '_expect.json'
		filename = expath + test_name + '.json'
	else:
		filename = expath + expect_file
	fo = open(filename, 'r')
	fs = fo.read()
	fo.close()
# 	fd = json.loads(fs)
# 	print "预期结果key---------------------"
# 	print fd,type(fd)
	if fs and isinstance(fs, (str, list, dict, int)):
		print "API expect returned:", fs, type(fs)
# 		result_dic = json.loads(fs)
		fs = fs.replace('null', "\"null\"")
# 		print "----wwwwwwww"
		str1_evaled = eval(fs)
# 		print "----wwwwwwww"

		print "str1_evaled", str1_evaled, type(str1_evaled)
		if isinstance(str1_evaled, list):
			print "预期结果key(list)---------------------"
			for dict2 in str1_evaled:
# 						print dict1
					print "预期结果第一个dict返回值",dict2, type(dict2)
					if isinstance(dict2, int):
						actual_dic = dict2
					else:
						actual_dic=dict2 .keys()
					print  actual_dic, type(actual_dic)
# 							s1 = '\n'.join(d)
# 							print s1
					break
					print "----------------------------------"
		else:
			print "预期结果key---------------------"
			dict2 = json.loads(fs)
			print "预期结果dict返回值",dict2, type(dict2)
			actual_dic= dict2.keys()
			print actual_dic, type(dict2)
			print "----------------------------------"
# 	expect_key =  fd.keys()
# 	print expect_key
	return dict2

def record_result(module_name, class_name, test_result):
	#print sys._getframe().f_code.co_name
	test_name = sys._getframe().f_back.f_code.co_name 
	#time_stamp = time.strftime('_%Y-%m-%d_%H:%M:%S', time.localtime())
	#filename = os.getcwd() + '/actual_result/' + module_name +'/'+ class_name +'/'+ test_name + time_stamp + ".json"
	filename = os.getcwd() + '/actual_result/' + module_name +'/'+ class_name +'/'+ test_name + ".json"
	fo = open(filename, 'w')
	if isinstance(test_result, str):
		fo.write(test_result)
	elif isinstance(test_result, dict) or isinstance(test_result, list):
		fo.write(json.dumps(test_result))
	fo.close()
	
def _makedirs(module_name, class_name):
	expect_path = "/".join([os.getcwd(), "expect_result", module_name, class_name])
	actual_path = "/".join([os.getcwd(), "actual_result", module_name, class_name])
	post_path = "/".join([os.getcwd(), "post_data", module_name, class_name])
	if not os.path.exists(expect_path):
		os.makedirs(expect_path)
	if not os.path.exists(actual_path):
		os.makedirs(actual_path)
	if not os.path.exists(post_path):
		os.makedirs(post_path)
	print "Expect result directory:", expect_path
	print "Actual result directory:", actual_path
	print "Post data directory:", post_path
		


#data = {u'user_status': u'\u6b63\u5e38', u'user_id': u'284381', u'user_roles': u'\u7ba1\u7406\u5458', u'last_visit_time': u'2016-03-08 14:22:17', u'user_name': u'Sally.Kang', u'user_email': u'Sally.Kang@yunzhihui.com'}
#print_dict(data)
