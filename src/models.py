import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table User
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(Integer, primary_key=True)
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250), unique = True, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email
        }

class Gender(enum.Enum):
    male = 1
    female = 2
    NA = 3

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable = False)
    gender = Column(Enum(Gender))
    height = Column(Integer, nullable=False)
    skin_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable =False)

    def todic(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "height": self.height,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color
        }
    
class Planet(Base):
    __tablename__='planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    population = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)

    def todic(self):
        return {}

class Category(enum.Enum):
    character = 1
    planet = 2

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key = True)
    name = Column(String(250), unique=True)
    type = Column(Enum(Category))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    user = Column(Integer, ForeignKey('user.id'))


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
