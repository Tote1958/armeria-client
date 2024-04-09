from abc import ABC, abstractmethod
from app.config.database import db


class Create(ABC):

    @abstractmethod
    def create(self, entity:db.Model):
        pass


class Read(ABC):

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def find_by_id(self, id:int):
        pass


class Update(ABC):

    @abstractmethod
    def update(self, entity:db.Model, id:int):
        pass


class Delete(ABC):
    
    @abstractmethod
    def delete(self, entity:db.Model):
        pass

# Es para realizar las consultas en la base de datos
# Este archivo se encarga de obligar al programador a programar (sobrescribir) estos metodos existentes)
