#!/usr/bin/env python
#-*- encoding: utf-8 -*-

e = {"list":["a","b",1],"fake_dict":{"a":"1","b":"2"},"user_status":"normal","user_id":"305228","orgnization":[{"node_id":"2993","node_title":"rita"},{"node_id":"3312","node_titile":"admin"}],"username":"rita","user_email":"rita@163.com"}
a = {"list":["a",2,3,"b"],"fake_dict":{"a":"1","b":"2"},"user_status":"normal","user_id":"305228","orgnization":[{"node_id":"2993","node_title":"rita"},{"node_id":"3312","node_titile":"admin"}],"username":"rita","user_email":"rita@163.com"}

def assert_loose_equal(actual, expected):
	aaa = _do_assertion(actual, expected, _assert_loose_equal)
	if ( aaa == 'true'):
		return "true"
	else:
		return "false"

def assert_strict_equal(actual, expected):
# 	return _do_assertion(actual, expected, _assert_strict_equal)
	bbb = _do_assertion(actual, expected, _assert_strict_equal)
	if ( bbb == 'true'):
		return "true"
	else:
		return "false"	

def _do_assertion(actual, expected, assert_func):
	try:
		return  assert_func(actual, expected, [])
	except AssertionError, e:
		msg = "\n--------------------------------- >> Actual << ------------------------------------\n"
# 		msg += str(actual).decode('unicode_escape')
		actual = str(actual).replace('u\'','\'')  
 		
		msg += str(actual).decode('unicode_escape').encode('utf-8')
				
		msg += "\n-------------------------------- >> Expected << -----------------------------------\n"
# 		msg += str(expected).decode('unicode_escape')
		msg += str(expected).decode('unicode_escape').encode('utf-8')
		msg += "\n\n" + str(e)
		raise AssertionError(msg.encode('utf-8'))
	
def aaaaaa():
	return "true"

def _assert_loose_equal(actual, expected, path):
	path_str = '/' + '/'.join(map(str, path)) #map produce a list of str(path)
	if isinstance(actual, dict) and isinstance(expected, dict):
		actual_keys = set(actual.keys())
		print "actual_keys",actual_keys
		expected_keys = set(expected.keys())
		print "expected_keys",expected_keys
		actual_key_extra = actual_keys - expected_keys
		print "actual_key_extra:", actual_key_extra
# 		and_keys = expected_keys & actual_keys
		print "actual_keys == expected_keys:", actual_keys == expected_keys
		assert actual_keys == expected_keys
		if(actual_keys == expected_keys):
# 			print actual_keys == expected_keys
			print "true======"
			return "true"
		else:
			return "false"
		
		if actual_keys != expected_keys or expected_keys ==[]:
# 		and_keys = expected_keys & actual_keys
# 		print "and_keys == expected_keys:", and_keys == expected_keys
# 		assert and_keys == expected_keys
# 		
# 		if and_keys != expected_keys or expected_keys ==[]:
			msg = "Actual got unexpected keys %s at %s" % (list(actual_key_extra), path_str)
			raise AssertionError(msg)
		#if actual_key_extra and not ignore_extra_keys:
		#	msg = "at %s, actual got unexpected keys %s" % (path_str, list(actual_key_extra))
		#	raise AssertionError(msg)
		#expected_key_extra = expected_keys - actual_keys
		#if expected_key_extra:
		#	msg = "at %s, expected keys %s are absent in actual" % (path_str, list(expected_key_extra))
		#	raise AssertionError(msg)

		for key in expected_keys:
			_assert_loose_equal(actual[key], expected[key], path + [key])

	elif isinstance(actual, list) and isinstance(expected, list) or \
			isinstance(actual, tuple) and isinstance(expected, tuple):
		actual_len = len(actual)
		expected_len = len(expected)
		min_len = expected_len if expected_len <= actual_len else actual_len
		for i in xrange(min_len):
			#print "List iter degree:", i, "====================="
			return _assert_loose_equal(actual[i], expected[i], path + [i])
	else:
		if type(expected) != type(actual):
			raise AssertionError("Assert str/int: Expect type %r, actual type %r, at %s" %(expected.__class__.__name__, actual.__class__.__name__, path_str))	

def _assert_strict_equal(actual, expected, path):
	path_str = '/' + '/'.join(map(str, path))
	if isinstance(actual, dict) and isinstance(expected, dict):
		actual_keys = set(actual.keys())
		expected_keys = set(expected.keys())
		actual_key_extra = actual_keys - expected_keys
		print "actual_key_extra:", actual_key_extra
		
		if actual_keys != expected_keys:
			msg = "Assert dict: Actual got unexpected keys %s, at %s" % (list(actual_key_extra), path_str)
			raise AssertionError(msg)

		for key in expected_keys:
			_assert_strict_equal(actual[key], expected[key], path + [key])

	elif isinstance(actual, list) and isinstance(expected, list) or \
			isinstance(actual, tuple) and isinstance(expected, tuple):
		actual_len = len(actual)
		expected_len = len(expected)
		if actual_len != expected_len:
			raise AssertionError("Assert list: Expected length %s, actual length %s, at %s" % (expected_len, actual_len, path_str))
		#actual_pars = set(actual)
		#expected_pars = set(expected)
		#if actual_pars & expected_pars:
		#	raise AssertionError()
		for i in xrange(expected_len):
			_assert_strict_equal(actual[i], expected[i], path + [i])
	else:
		if actual != expected:
			raise AssertionError("Assert str/int: Expected value %r, actual value %r, at %s" %(expected, actual, path_str))

# assert_loose_equal(a,e)
# assert_strict_equal(a,e)
