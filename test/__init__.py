from app import create_test_app
import unittest

BASEURL = '/news/'

class BaseTest(unittest.TestCase):
	def setUp(self):
		self.app = create_test_app()
		self.client = self.app.test_client()

class A_MessageTest(BaseTest):
	def test_get_all_message(self):
		"""
			Test CURD of message
		"""
		rep = self.client.get(BASEURL + 'messages')
		assert rep.status_code is 200
