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

    def test_create(self): 
        body = {"name":"Santino", "code":"1234", "dni":"32123543", "email":"santino@gmail.com",
                "address":"Sarmiento 321"}
        #client = self.app.test_client(use_cookies=True)    Por alguna razon deja de devolver json con este
        response = requests.post('http://127.0.0.1:5000/api/v1/client/create', json=body)
        response = response.json()
        self.assertEqual(response["id"], 1)
        self.assertEqual(response["name"], 'Santino')
        self.assertEqual(response["code"], '1234')
        self.assertEqual(response["dni"], '32123543')
        self.assertEqual(response["email"], 'santino@gmail.com')
        self.assertEqual(response["address"], 'Sarmiento 321')
        
    def test_find_by_id(self):
        client_db = self.create_client()
        client = self.app.test_client(use_cookies=True)
        response = client.get('http://localhost:5000/api/v1/client/id/1')
        response = response.get_json()
        # self.assertGreaterEqual(response["id"], 1) Cual va?
        self.assertEqual(response["id"], 1)
    
    def test_find_all(self): # Preguntar como se testearia un find_all en la vida real
        client = self.app.test_client(use_cookies=True)
        response = client.get('http://localhost:5000/api/v1/client/')
        self.assertEqual(response.status_code, 200)
    
    def test_find_by_name(self):             # Preguntar porque no anda, anda perfecto el metodo
        client_db = self.create_client()
        response = requests.get('http://127.0.0.1:5000/api/v1/client/name/', params={"name":"Santino"})
        response = response.json()
        self.assertEqual(response["id"], 1)

    def test_find_by_email(self):
        client_db = self.create_client()
        client = self.app.test_client(use_cookies=True)
        response = client.get('http://127.0.0.1:5000/api/v1/client/email/santino@gmail.com')
        response = response.get_json()
        self.assertEqual(response["id"], 1)
    
    def test_update(self):
        client_db = self.create_client()
        client = self.app.test_client(use_cookies=True)
        body = {"name": "Pepito", "code":"5432", "dni":"44555666", "email":"pepito@gmail.com","address":"Peru 444"}
        response = client.put('http://localhost:5000/api/v1/client/update/1', json=body)
        response = response.get_json()
        self.assertEqual(response["id"], 1)
        self.assertEqual(response["name"], 'Pepito')
        self.assertEqual(response["code"], '5432')
        self.assertEqual(response["dni"], '44555666')
        self.assertEqual(response["email"], 'pepito@gmail.com')
        self.assertEqual(response["address"], 'Peru 444')
    def test_delete(self):
        client_db = self.create_client()
        client = self.app.test_client(use_cookies=True)
        response = client.delete('http://localhost:5000/api/v1/client/delete/1')
        clients = service.find_all()
        self.assertEqual(len(clients), 0)
if __name__ == '__main__':
    unittest.main()