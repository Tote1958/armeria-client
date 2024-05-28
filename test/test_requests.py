import unittest
from sqlalchemy import text
import requests

from app import create_app, db

class ConnectionTestCase(unittest.TestCase):


    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
    
    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_find_by_id(self):
        client = self.app.test_client(use_cookies=True) 
        response = client.get('http://localhost:5000/api/v1/id/1')
        self.assertEqual(response.status_code, 200)
    
    def test_find_all(self):
        client = self.app.test_client(use_cookies=True)
        response = client.get('http://localhost:5000/api/v1/')
        self.assertEqual(response.status_code, 200)
    
if __name__ == '__main__':
    unittest.main()