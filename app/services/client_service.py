from app.models import Client
from app.repositories.client_repository import ClientRepository
from app import cache


class ClientService:
    def __init__(self):
        self.__repo = ClientRepository()
        
    def find_all(self) -> Client:
        return self.__repo.find_all()
    
    def find_by_id(self, id: int) -> Client:
        client = cache.get(str(id))
        if client == None:
            client = self.__repo.find_by_id(id)
            cache.set(client.id, client, timeout=50)
        return client

    def find_by_name(self, name) -> list:
        client = self.__repo.find_by_name(name)
        first_client = client[0]
        cache.set(str(first_client.id), first_client, timeout=50)
        return client
    
    def find_by_email(self, email) -> Client:
        client = self.__repo.find_by_email(email)
        cache.set(str(client.id), client, timeout=50)
        return client

    def create(self, entity: Client) -> Client:
        client = self.__repo.create(entity)
        cache.set(str(client.id), client, timeout=50)
        return client
    
    def update(self, dto, id: int) -> Client:
        client = self.__repo.update(dto, id)
        cache.set(str(client.id), client, timeout=50)   
        return client
    
    def delete(self, id: int) -> Client:
        client = self.__repo.delete(id)
        cache.set(str(id), client, timeout=0)   
    

        