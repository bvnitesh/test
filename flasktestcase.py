import requests
import unittest
import flasktest

#class TestFlask(unittest.TestCase):
#      def test_flask(self):
#          self.assertEqual(requests.get("http://127.0.0.1:5000").text , "Hello World!")

class TestIntegrations(unittest.TestCase):
    def setUp(self):
        self.app = flasktest.app.test_client()

    def test_thing(self):
        response = self.app.get('/')
        self.assertEqual(response.get_data(), b'My name is Nit')

if __name__ == "__main__":
     unittest.main()


