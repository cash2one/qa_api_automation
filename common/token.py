#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import os,pycurl, urllib, json, ConfigParser,sys
try:
	from io import BytesIO
except ImportError:
	from StringIO import StringIO as BytesIO

def get_auth(env):
# 	获取当前文件完整路径
# 	print os.path.join( os.path.dirname(__file__))
	#		 项目路径
	proDir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
	#		 config目录路径   
	confDir =  os.path.join(proDir, "config")
	sys.path.append(confDir)
# 	print confDir
# 	print proDir
	# Return a dict containing url and auth data of specific environment.
	# Example: {'url':'http://api.jiankongbao.com', 'auth':{'name','rita@163.com'}}
	conf = ConfigParser.ConfigParser()
# 	conf.read('/Users/sunying/Desktop/cloudwise/eclipse_work/QA-Automation-master/config/api_auth_data.ini')
	conf.read(confDir +'/api_auth_data.ini')
	# 	aecs = conf.sections()  
	#opts = conf.options(env)
# 	获取指定env 的配置信息
	itms = conf.items(env)
	conf_auth = conf.get(env, 'auth')
# 	print '~~~~~~~~~~~~~~'
# 	print conf_auth
	#print itms, type(itms[0]), type(itms[1][1])
	#print conf_auth, type(conf_auth), "+"*10
	auth_dict = {itms[0][0]:itms[0][1], itms[1][0]:json.loads(conf_auth)}
	return auth_dict

def get_access_token(url_prefix, url_suffix, auth_data):
	buffer = BytesIO()
	header = BytesIO() 
# 	url_suffix = '/v2/oauth/token.json'
	c = pycurl.Curl()
	c.setopt(c.URL, url_prefix + url_suffix)
	url = url_prefix + url_suffix
	print url
	#c.setopt(c.VERBOSE, True)
	#c.setopt(c.POST, False)
	c.setopt(c.SSL_VERIFYPEER, False)
	c.setopt(c.POSTFIELDS, urllib.urlencode(auth_data))
	print "--------------"
	print str(auth_data).decode('unicode_escape').encode('utf-8')
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

def pycurl_get(url_prefix, url_suffix, access_token, url_params=''):
	url_params = '&' + url_params if url_params else ''
	url = url_prefix + url_suffix + '?access_token=' + access_token + url_params
	print('Request URI:'), (url), ('\n')
	buffer = BytesIO()
	header = BytesIO()
	c = pycurl.Curl()
	c.setopt(c.URL, url)
	c.setopt(c.WRITEFUNCTION, buffer.write)
	c.setopt(c.HEADERFUNCTION, header.write)
	c.setopt(c.SSL_VERIFYPEER, False)
	try:
		c.perform()
	except Exception, e:
		c.close()
		buffer.close()
		header.close()
	result_str = buffer.getvalue()
	result_header = header.getvalue()
	result_code = c.getinfo(c.HTTP_CODE)
	c.close()

	if  result_code == 200:
		try:
# 			print 'result_str'
# 			print type(result_str)
			result = result_str.replace('null', "\"null\"")
			result = result_str.replace('true', "\"true\"")
			result = result_str.replace('false', "\"false\"")
			result = json.loads(result)
# 			print 'result:'
# 			print type(result)
		except BaseException, e:
			msg = ("Abnormal result returned from request URI, please check it manually.")
			print msg
			result = result_str
			#raise AssertionError(msg)
	else:
		result = None
	if result_code >= 500:
		msg = "Connection error to request URI with http_code %s, please check it manually." %result_code
		print msg
		result = msg
	return result
# 	
# 	#print json.dumps(result_str, indent=4)
# 	if result_code == 200:
# 		if result_str and isinstance(result_str, (str, list, dict, int)):
# 			print "API returned:", result_str, type(result_str)
# 			try:
# # 				result_dic = json.loads(result_str)
# 				result_str = result_str.replace('null', "\"null\"")
# 				result_str = result_str.replace('true', "\"true\"")
# 				result_str = result_str.replace('false', "\"false\"")
# 				return result_str
# # 				print result_str
# # 				str1_evaled = eval(result_str)
# # # 				print "str1_evaled", str1_evaled, type(str1_evaled)
# # 				if isinstance(str1_evaled, list):
# # 					print "实际结果key(list)---------------------"
# # 					if str1_evaled == []:
# # 						msg = '实际返回值为空！'
# # 						raise AssertionError(msg)
# # 					for dict1 in str1_evaled:
# # 						print "实际结果第一个dict返回值",dict1, type(dict1)
# # 						actual_dic=dict1 .keys()
# # 						print  actual_dic
# # # 							s1 = '\n'.join(d)
# # # 							print s1
# # 						break
# # 						print "----------------------------------"
# 				else:
# 						print "实际结果key(dict)---------------------"
# 						dict1 = json.loads(result_str)
# 						actual_dic= dict1.keys()
# 						print actual_dic, type(actual_dic)
# 						print "实际结果dict返回值",dict1, type(dict1)
# 						print "----------------------------------"
# 				
# # 				a = {}
# # 				if isinstance(result_dic,list):
# # 					result_dict = json.loads(result_dic)
# # 					print result_dict
# #            			 list_convert(result_dic,dict)
# #            			 actual_keys = set(result_dic.keys())
# # 					expected_keys = set(expected.keys())
# # 					actual_key_extra = actual_keys - expected_keys
# #         	      	elif isinstance(a,int):
# #             output.append(a)
# # 				
# # 				if isinstance(result_dic, list):
# 					
# # 		print "actual_key_extra:", actual_key_extra
# # 				print "实际结果key---------------------"
# # 				actual_key= result_dic.keys()
# # # 				if isinstance(result_dic, list) 
# # # 					actual_keys = set(actual_key.keys())
# # # 					print actual_key
# # 				print "----------------------------------"
# 			except BaseException, e:
# 				msg = ("Abnormal result returned from request URI, please check it manually.")
# 				print e;
# 				raise AssertionError(msg)
# 	else:
# 		msg = "Connection error to request URI with http_code %s, please check it manually." %result_code
# 		raise AssertionError(msg)
# 	return dict1

def pycurl_post(url_prefix, url_suffix, access_token, post_dict):
	url = url_prefix + url_suffix + '?access_token=' + access_token
	print('Request URI:'), (url), ('\n')
	post_data = 'data=' + urllib.quote(json.dumps(post_dict))
	buffer = BytesIO()
	header = BytesIO()
	c = pycurl.Curl()
	c.setopt(c.URL, url)
	# For x-www-form-urlencoded type 
	#c.setopt(c.POSTFIELDS, urllib.urlencode(post_data))
	c.setopt(c.POSTFIELDS, urllib.quote(post_data))
	c.setopt(c.POSTFIELDS, post_data)
	c.setopt(c.WRITEFUNCTION, buffer.write)
	c.setopt(c.HEADERFUNCTION, header.write)
	c.setopt(c.SSL_VERIFYPEER, False)
	#c.setopt(c.VERBOSE, True)
	try:
		c.perform()
	except Exception, e:
		c.close()
		buffer.close()
		header.close()
	result_str = buffer.getvalue()
	resutl_header = header.getvalue()
	result_code = c.getinfo(c.HTTP_CODE)
	c.close()
	if  result_code == 200:
		try:
# 			print 'result_str'
# 			print type(result_str)
			result = result_str.replace('null', "\"null\"")
			result = result_str.replace('true', "\"true\"")
			result = result_str.replace('false', "\"false\"")
			result = json.loads(result)
# 			print 'result:'
# 			print type(result)
		except BaseException, e:
			msg = ("Abnormal result returned from request URI, please check it manually.")
			print msg
			result = result_str
			#raise AssertionError(msg)
	else:
		result = None
	if result_code >= 500:
		msg = "Connection error to request URI with http_code %s, please check it manually." %result_code
		print msg
		result = msg
	return result	
# 未改动之前
# 	if result_code == 200:
# 		if result_str and isinstance(result_str, (str, list, dict, int)):
# 			print "API returned:", result_str, type(result_str)
# 			try:
# 				result_dic = json.loads(result_str)

# #改动后，提取key值
# 	if result_code == 200:
# 		if result_str and isinstance(result_str, (str, list, dict, int)):
# 			print "API returned:", result_str, type(result_str)
# 			try:
# # 				result_dic = json.loads(result_str)
# 				result_str = result_str.replace('null', "\"null\"")
# 				print result_str
# 				str1_evaled = eval(result_str)
# # 				print "str1_evaled", str1_evaled, type(str1_evaled)
# 				if isinstance(str1_evaled, list):
# 					print "实际结果key(list)---------------------"
# 					for dict1 in str1_evaled:
# 						print "实际结果第一个dict返回值",dict1, type(dict1)
# 						if isinstance(dict1, int):
# 							actual_dic = dict1
# 							
# 						else:
# 							actual_dic=dict1 .keys()
# 							print  actual_dic, type(actual_dic)
# # 							s1 = '\n'.join(d)
# # 							print s1
# 							break
# 							print "----------------------------------"
# 				else:
# 						print "实际结果key(dict)---------------------"
# 						dict1 = json.loads(result_str)
# 						actual_dic= dict1.keys()
# 						print actual_dic, type(dict1)
# 						print "实际结果dict返回值",dict1, type(dict1)
# 						print "----------------------------------"
# 
# 			except BaseException, e:
# 				msg = ("Abnormal result returned from request URI, please check it manually.")
# 				print e;
# 				raise AssertionError(msg)
# 	else:
# 		msg = "Connection error to request URI with http_code %s, please check it manually." %result_code
# 		raise AssertionError(msg)
# # 	return result_dic
# 	return dict1

def pycurl_put(url_prefix, url_suffix, access_token, url_params=''):
	url_params = '&' + url_params if url_params else ''
	url = url_prefix + url_suffix + '?access_token=' + access_token + url_params
	print('Request URI:'), (url), ('\n')
	buffer = BytesIO()
	header = BytesIO()
	c = pycurl.Curl()
	c.setopt(c.URL, url)
	c.setopt(c.WRITEFUNCTION, buffer.write)
	c.setopt(c.HEADERFUNCTION, header.write)
	c.setopt(c.SSL_VERIFYPEER, False)
	c.setopt(pycurl.CUSTOMREQUEST,"PUT")
	try:
		c.perform()
	except Exception, e:
		c.close()
		buffer.close()
		header.close()
	result_str = buffer.getvalue()
	result_header = header.getvalue()
	result_code = c.getinfo(c.HTTP_CODE)
	c.close()
	#print json.dumps(result_str, indent=4)
	if result_code == 200:
		if result_str and isinstance(result_str, (str, list, dict, int)):
			print "API returned:", result_str, type(result_str)
			try:
# 				result_dic = json.loads(result_str)
				result_str = result_str.replace('null', "\"null\"")
				print result_str
				str1_evaled = eval(result_str)
				print "str1_evaled", str1_evaled, type(str1_evaled)
				if isinstance(str1_evaled, list):
					print "实际结果key(list)---------------------"
					for dict1 in str1_evaled:
						print "实际结果第一个dict返回值",dict1, type(dict1)
						actual_dic=dict1 .keys()
						print  actual_dic
# 							s1 = '\n'.join(d)
# 							print s1
						break
						print "----------------------------------"
				else:
						print "实际结果key---------------------"
						dict1 = json.loads(result_str)
						print "实际结果dict返回值",dict1, type(dict1)
						actual_dic= dict1.keys()
						print actual_dic, type(dict1)
						print "----------------------------------"
				
# 				a = {}
# 				if isinstance(result_dic,list):
# 					result_dict = json.loads(result_dic)
# 					print result_dict
#            			 list_convert(result_dic,dict)
#            			 actual_keys = set(result_dic.keys())
# 					expected_keys = set(expected.keys())
# 					actual_key_extra = actual_keys - expected_keys
#         	      	elif isinstance(a,int):
#             output.append(a)
# 				
# 				if isinstance(result_dic, list):
					
# 		print "actual_key_extra:", actual_key_extra
# 				print "实际结果key---------------------"
# 				actual_key= result_dic.keys()
# # 				if isinstance(result_dic, list) 
# # 					actual_keys = set(actual_key.keys())
# # 					print actual_key
# 				print "----------------------------------"
			except BaseException, e:
				msg = ("Abnormal result returned from request URI, please check it manually.")
				print e;
				raise AssertionError(msg)
	else:
		msg = "Connection error to request URI with http_code %s, please check it manually." %result_code
		raise AssertionError(msg)
	return dict1

def pycurl_delete(url_prefix, url_suffix, access_token, url_params=''):
	url_params = '&' + url_params if url_params else ''
	url = url_prefix + url_suffix + '?access_token=' + access_token + url_params
	print('Request URI:'), (url), ('\n')
	buffer = BytesIO()
	header = BytesIO()
	c = pycurl.Curl()
	c.setopt(c.URL, url)
	c.setopt(c.WRITEFUNCTION, buffer.write)
	c.setopt(c.HEADERFUNCTION, header.write)
	c.setopt(c.SSL_VERIFYPEER, False)
	c.setopt(pycurl.CUSTOMREQUEST,"DELETE")
	try:
		c.perform()
	except Exception, e:
		c.close()
		buffer.close()
		header.close()
	result_str = buffer.getvalue()
	result_header = header.getvalue()
	result_code = c.getinfo(c.HTTP_CODE)
	c.close()
	#print json.dumps(result_str, indent=4)
	if result_code == 200:
		if result_str and isinstance(result_str, (str, list, dict, int)):
			print "API returned:", result_str, type(result_str)
			try:
# 				result_dic = json.loads(result_str)
				result_str = result_str.replace('null', "\"null\"")
				print result_str
				str1_evaled = eval(result_str)
				print "str1_evaled", str1_evaled, type(str1_evaled)
				if isinstance(str1_evaled, list):
					print "实际结果key(list)---------------------"
					for dict1 in str1_evaled:
						print "实际结果第一个dict返回值",dict1, type(dict1)
						actual_dic=dict1 .keys()
						print  actual_dic
# 							s1 = '\n'.join(d)
# 							print s1
						break
						print "----------------------------------"
				else:
						print "实际结果key---------------------"
						dict1 = json.loads(result_str)
						print "实际结果dict返回值",dict1, type(dict1)
						actual_dic= dict1.keys()
						print actual_dic, type(dict1)
						print "----------------------------------"
				
# 				a = {}
# 				if isinstance(result_dic,list):
# 					result_dict = json.loads(result_dic)
# 					print result_dict
#            			 list_convert(result_dic,dict)
#            			 actual_keys = set(result_dic.keys())
# 					expected_keys = set(expected.keys())
# 					actual_key_extra = actual_keys - expected_keys
#         	      	elif isinstance(a,int):
#             output.append(a)
# 				
# 				if isinstance(result_dic, list):
					
# 		print "actual_key_extra:", actual_key_extra
# 				print "实际结果key---------------------"
# 				actual_key= result_dic.keys()
# # 				if isinstance(result_dic, list) 
# # 					actual_keys = set(actual_key.keys())
# # 					print actual_key
# 				print "----------------------------------"
			except BaseException, e:
				msg = ("Abnormal result returned from request URI, please check it manually.")
				print e;
				raise AssertionError(msg)
	else:
		msg = "Connection error to request URI with http_code %s, please check it manually." %result_code
		raise AssertionError(msg)
	return dict1
print get_auth('qa')


