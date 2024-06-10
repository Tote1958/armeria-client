import unittest
from sqlalchemy import text
import requests
from app.services.client_service import Client, ClientService
from app import create_app, db, cache

service = ClientService()

class TestRequests(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        cache.clear()
        self.app_context.pop()
    
    def create_client(self):
        client = Client()
        client.name = 'Santino'
        client.code = '1234'
        client.dni = '32123543'
        client.email = 'santino@gmail.com'
        client.address = 'Sarmiento 321'
        client_db = service.create(client)
        return client_db
    
    def test_find_by_id(self):
        client_db = self.create_client()
        client = self.app.test_client(use_cookies=True) 
        response = client.get('http://localhost:5000/api/v1/client/id/1')
        self.assertEqual(response.status_code, 200)
    
    def test_find_all(self):
        client = self.app.test_client(use_cookies=True)
        response = client.get('http://localhost:5000/api/v1/client/')
        self.assertEqual(response.status_code, 200)
    
if __name__ == '__main__':
    unittest.main()