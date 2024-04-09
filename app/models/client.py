from __future__ import annotations
from app.config.database import db
from sqlalchemy.ext.hybrid import hybrid_property
from dataclasses import dataclass


@dataclass
class Client(db.Model):
    __tablename__ = 'client'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String(105))
    dni = db.Column('dni', db.String(9))
    email = db.Column('email', db.String(256))
    code = db.Column('code', db.String(205))
    address = db.Column('address', db.String(105))
    

    """
    name: str name of supplier max char 105
    dni: str cuil of supplier max char 250
    email: str email of supplier max char 250
    code: str code of supplier max char 256
    address: str addres of supplier max char 256
    """