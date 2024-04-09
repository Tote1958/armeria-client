from app.models import Client
from app.config.database import db 
from .CRUD import Create, Read, Update, Delete


class ClientRepository(Create, Read, Update, Delete):
    
    def __init__(self):
        self.__model = Client

    """
    Recibe un objeto y lo guarda en la base de datos
    """
    # dto: data transfer object
    def create(self, dto: Client):
        db.session.add(dto)
        db.session.commit()
        return dto

    """
    Cambia el objeto que esta identificado con el id, modificando los atributos ingresados
    """
    def update(self, dto, id: int) -> Client:
        entity = self.find_by_id(id)
        for key, value in dto.items():
            setattr(entity, key, value)
        db.session.commit()
        return entity

    """
    Devuelve un objeto, filtrado por un nombre
    """
    def find_by_name(self, name: str) -> list:
        clients = db.session.query(self.__model).filter(self.__model.name.like(name)).all()  # Ver donde poner el like
        return clients

    """
    Devuelve un objeto, filtrado por un email
    """
    def find_by_email(self, email: str) -> Client:
        return db.session.query(self.__model).filter(self.__model.email == email).first() # Ver donde poner el like

    """
    Devuelve todos los objetos de la base de datos
    """
    def find_all(self):
        return db.session.query(self.__model).all()

    """
    Devuelve el objeto identificado con ese id
    """
    def find_by_id(self, id: int) -> Client:
        return db.session.query(self.__model).filter(self.__model.id == id).one()

    """
    Borra el objeto identificado con ese id
    """
    def delete(self, id: int):
        entity = self.find_by_id(id)
        db.session.delete(entity)
        db.session.commit()
