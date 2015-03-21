from app import create_test_app, app
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
			phone_number = "1231241241",
			description = 'fdsafsadfa',
			email = '327272993@qq.com',
			myattr = 'fsdfsa',
			company = "test",
			is_vip = False
			)
		json_data = json.dumps(data)
		headers = self.get_headers(json_data)
		rep = self.client.post(BASEURL + 'users', headers = headers,
			data = json_data)
		#print rep.data
		assert rep.status_code is 201
		return json.loads(rep.data)

	
	def get_headers(self,json_data):
		headers = [('Content-Type', 'application/json')]
		if len(json_data) > 0:
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

	def check_code(self, rep, expect_code):
		if rep.status_code is not expect_code:
			print rep.data
		assert rep.status_code is expect_code

class B_MessageTest(BaseTest):
	def test_get_all_message(self):
		"""
			Test CURD of message.
				- Get all message
		"""
		rep = self.client.get(BASEURL + 'messages')
		assert rep.status_code is 200

	def test_send_message(self):
		"""
			Test user send message to system.
		"""
		data = dict(
			content='test message',
			token=self.token)
		json_data = json.dumps(data)
		rep = self.client.post(BASEURL + 'message/send',
			headers=self.get_headers(json_data), data=json_data)
		assert rep.status_code is 201

class C_UserApiTest(BaseTest):
	def test_get_userprofile(self):
		"""
			获取用户信息测试
		"""
		data = dict(
			token=self.token)
		json_data = json.dumps(data)
		rep = self.client.post(BASEURL + 'user/profile',
			headers=self.get_headers(json_data),
			data=json_data)
		assert rep.status_code is 200

	def test_update_username_nickname(self):
		"""
			更新用户姓名和头像
		"""
		name = 'user' + str(random.randint(1,10000))
		self.u['name'] = name
		self.u['nickname'] = 'nicknick'+ str(random.randint(1,10000))
		json_data = json.dumps(self.u)
		rep = self.client.post(BASEURL + 'user/' + str(self.u['id']) +'/update_name',
			headers=self.get_headers(json_data),
			data=json_data)
		assert json.loads(rep.data)['name'] == name

	def test_update_user_profile(self):
		"""
			更新用户头像和信息
		"""
		pass


	def register_a_new_user(self):
		"""
			注册一个新用户
		"""
		pass

class D_ImageTest(BaseTest):
	def test_get_mockimage(self):
		rep = self.client.get(BASEURL +'mockimage')
		assert rep.status_code is 200

class E_NewsTest(BaseTest):
	def test_add_news(self):
		print '\nInit NewsTest'
		data = dict(title = 'test title'
			,content = 'test content'
			, create_time = '2014-12-10'
			, update_time = '2014-12-10'
			, author = 'fdsafsa'
			, view_count = 0
			, is_draft = False
			, publisher = 0)
		json_data = json.dumps(data)
		rep = self.client.post(BASEURL + 'news',
    		headers = self.get_headers(json_data),
    		data=json_data)
		assert rep.status_code is 201
		self.news = json.loads(rep.data)

	def test_get_news(self):
		"""
			
		"""
		pass

	def test_news_crud(self):
		pass


class F_ConferenceTest(BaseTest):
	def test_confernce_crud(self):
		print '\nTest add a conference...\n' 
		data = dict(
 			intro_content = 'test content'
        	, logistics_content = 'test content'
        	, title = 'test title'
        	, created_time = '2014-12-10'
        	, updated_time = '2014-12-10'
        	, view_count = 0
        	, is_draft = False
		)
		json_data = json.dumps(data)
		rep = self.client.post(BASEURL + 'conferences',
			headers=self.get_headers(json_data),
			data=json_data)
		self.check_code(rep, 201)

		conference = json.loads(rep.data)
		print '\nTest get conference file\n'
		rep = self.client.get(BASEURL + 'conferences/'+ str(conference['id'])+
			'/get_file/GROUP', headers=self.get_headers(""))
		assert rep.status_code is 200

		print '\nTest get all profile of conference\n'
		rep = self.client.get(BASEURL + 'conferences/content',
			headers=self.get_headers(""))
		assert rep.status_code is 200