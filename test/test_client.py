import unittest
from flask import current_app
from app import create_app, db, cache
from app.services.client_service import Client, ClientService

service = ClientService()

class TestClient(unittest.TestCase):
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
        client_db = self.create_client()

        self.assertGreaterEqual(client_db.id, 1)
        self.assertEqual(client_db.name, 'Santino')
        self.assertEqual(client_db.code, '1234')
        self.assertEqual(client_db.dni, '32123543')
        self.assertEqual(client_db.email, 'santino@gmail.com')
        self.assertEqual(client_db.address, 'Sarmiento 321')


        
    def test_find_by_id(self):
        client_db = self.create_client()
        client = service.find_by_id(1)
        self.assertEqual(client.id, 1)
        self.assertEqual(client.name, 'Santino')
        self.assertEqual(client.code, '1234')
        self.assertEqual(client.dni, '32123543')
        self.assertEqual(client.email, 'santino@gmail.com')
        self.assertEqual(client.address, 'Sarmiento 321')
        
    def test_find_by_name(self) -> list:
        client_db = self.create_client()
        client = service.find_by_name('Santino')
        self.assertEqual(client.id, 1)
        self.assertEqual(client.name, 'Santino')
        self.assertEqual(client.code, '1234')
        self.assertEqual(client.dni, '32123543')
        self.assertEqual(client.email, 'santino@gmail.com')
        self.assertEqual(client.address, 'Sarmiento 321')
    
    def test_find_by_email(self) -> Client:
        client_db = self.create_client()
        client = service.find_by_email('santino@gmail.com')
        self.assertEqual(client.id, 1)
        self.assertEqual(client.name, 'Santino')
        self.assertEqual(client.code, '1234')
        self.assertEqual(client.dni, '32123543')
        self.assertEqual(client.email, 'santino@gmail.com')
        self.assertEqual(client.address, 'Sarmiento 321')


    
    def test_update(self) -> Client:
        client_db = self.create_client()
        dto = {"name": "Pepito", "code":"5432", "dni":"44555666", "email":"pepito@gmail.com","address":"Peru 444"}
        client = service.update(dto, 1)
        result = service.find_by_id(1)
        self.assertEqual(result.id, 1)
        self.assertEqual(result.name, 'Pepito')
        self.assertEqual(result.code, '5432')
        self.assertEqual(result.dni, '44555666')
        self.assertEqual(result.email, 'pepito@gmail.com')
        self.assertEqual(result.address, 'Peru 444')
        

    def test_delete(self) -> Client:
        client_db = self.create_client()
        service.delete(1)
        clients = service.find_all()
        self.assertEqual(len(clients), 0)



if __name__ == '__main__':
    unittest.main()