from app import create_test_app
from datetime import datetime
import simplejson as json
import unittest
import random
import time as stime

ran_key = stime.mktime(datetime.now().timetuple())
BASEURL = '/news/'
TESTUSERNAME = 'tu_' + str(ran_key) + str(random.randint(1,1000))
TESTUSERPASS = 'tu_' + str(random.randint(1,1000))

class A_UserInit(unittest.TestCase):
	def setUp(self):
		self.app = create_test_app()
		self.client = self.app.test_client()

	def create_user(self):
		print "---Start to create user ---\n"
		data = dict(
			account = TESTUSERNAME,
			password = TESTUSERPASS,
			name = 'testu',
			role = 'admin',
			nickname = 'nick',
			registered_time = "2014-12-01",
			is_active = True,
			lastlogin_time = "2014-12-01",
			phone_number = 1231241241,
			description = 'fdsafsadfa',
			email = '327272993@qq.com',
			myattr = 'fsdfsa'
			)
		json_data = json.dumps(data)
		headers = self.get_headers(json_data)
		rep = self.client.post(BASEURL + 'users', headers = headers,
			data = json_data)
		assert rep.status_code is 201
		return json.loads(rep.data)

	
	def get_headers(self,json_data):
		headers = [('Content-Type', 'application/json')]
		json_data_length = len(json_data)
		headers.append(('Content-Length', json_data_length))
		return headers

	def test_create_user(self):
		self.create_user()	

class BaseTest(unittest.TestCase):
	def setUp(self):
		self.app = create_test_app()
		self.client = self.app.test_client()
		self.u = self.login()
		self.token = self.u['token'] 

	def login(self):
		data = dict(
			account=TESTUSERNAME,
			password=TESTUSERPASS)
		json_data = json.dumps(data)
		headers = self.get_headers(json_data)
		rep = self.client.post(BASEURL +'login',headers=headers, data=json_data)
		assert rep.status_code is 200
		return json.loads(rep.data)
	
	def get_headers(self,json_data):
		headers = [('Content-Type', 'application/json')]
		json_data_length = len(json_data)
		headers.append(('Content-Length', json_data_length))
		return headers

class B_MessageTest(BaseTest):
	def test_get_all_message(self):
		"""
			Test CURD of message
		"""
		rep = self.client.get(BASEURL + 'messages')
		assert rep.status_code is 200

	def test_send_message(self):
		data = dict(
			content='test message',
			token=self.token)
		json_data = json.dumps(data)
		rep = self.client.post(BASEURL + 'message/send',
			headers=self.get_headers(json_data), data=json_data)
		assert rep.status_code is 201

class C_UserApiTest(BaseTest):
	def test_get_userprofile(self):
		data = dict(
			token=self.token)
		json_data = json.dumps(data)
		rep = self.client.post(BASEURL + 'user/profile',
			headers=self.get_headers(json_data),
			data=json_data)
		assert rep.status_code is 200

	def test_update_username_nickname(self):
		name = 'user' + str(random.randint(1,10000))
		self.u['name'] = name
		self.u['nickname'] = 'nicknick'+ str(random.randint(1,10000))
		json_data = json.dumps(self.u)
		rep = self.client.post(BASEURL + 'user/' + str(self.u['id']) +'/update_name',
			headers=self.get_headers(json_data),
			data=json_data)
		assert json.loads(rep.data)['name'] == name


class D_ImageTest(BaseTest):
	def test_get_mockimage(self):
		rep = self.client.get(BASEURL +'mockimage')
		assert rep.status_code is 200

class E_NewsTest(BaseTest):
	def test_addnews(self):
		pass

	def test_topic(self):
		pass

