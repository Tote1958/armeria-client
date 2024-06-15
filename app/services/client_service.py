from app.models import Client
from app.repositories.client_repository import ClientRepository
from app import cache
from tenacity import retry, stop_after_attempt, stop_after_delay

class ClientService:
    def __init__(self):
        self.__repo = ClientRepository()
        
    @retry(stop=(stop_after_delay(10) | stop_after_attempt(5)))
    def find_all(self) -> Client:
        return self.__repo.find_all()
    
    
    def find_by_id(self, id: int) -> Client:
        client = cache.get(str(id))
        if client == None:
            client = self.__repo.find_by_id(id)
            cache.set(str(client.id), client, timeout=50)
        return client
    
    @retry(stop=(stop_after_delay(10) | stop_after_attempt(5)))
    def find_by_name(self, name) -> list:
        client = cache.get(str(name))
        if client == None:
            client = self.__repo.find_by_name(name)
            print(client)
            client = client[0]
            cache.set(str(client.name), client, timeout=50)
        return client
    
    @retry(stop=(stop_after_delay(10) | stop_after_attempt(5)))
    def find_by_email(self, email) -> Client:
        client = cache.get(str(email))
        if client == None:
            client = self.__repo.find_by_email(email)
            cache.set(str(client.email), client, timeout=50)
        return client
    
    @retry(stop=(stop_after_delay(10) | stop_after_attempt(5)))
    def create(self, entity: Client) -> Client:
        client = self.__repo.create(entity)
        cache.set(str(client.id), client, timeout=50)
        return client
    
    @retry(stop=(stop_after_delay(10) | stop_after_attempt(5)))
    def update(self, dto, id: int) -> Client:
        client = self.__repo.update(dto, id)
        cache.set(str(client.id), client, timeout=50)   
        return client
    
    @retry(stop=(stop_after_delay(10) | stop_after_attempt(5)))
    def delete(self, id: int) -> Client:
        client = self.__repo.delete(id)
        cache.set(str(id), client, timeout=0)   
    

        