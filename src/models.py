import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique= True)
    email = Column(String (150), nullable=False, unique = True)
    password = Column(String(150), nullable=False)
    favorites = relationship('Favorite')


class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250))
    vehicle_class = Column(String (250))
    crew = Column (Integer)
    manufacturer = Column(String(250))
    cargo_capacity = Column(Integer)
    cost_in_credits = Column(Integer)
    consumables = Column(Integer)

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250))
    hair_color = Column(String(250))
    eye_color = Column(String(250))
    height = Column(Integer)
    skin_color = Column(Integer)
    birth_year = Column(String(250))


class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(Integer)
    terrain = Column(String(250))
    climate = Column(String(250))
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(String(250))



class Favorite(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id_user = Column(Integer, ForeignKey('user.id'), nullable= False, primary_key=True)
    id_fav = Column(Integer, ForeignKey('vehicles.id'), ForeignKey('characters.id'), ForeignKey('planets.id'))
    fav_name = Column(String(250), ForeignKey('vehicles.name'), ForeignKey('characters.name'), ForeignKey('planets.name'))
    fav_Section = Column(String(250), ForeignKey('vehicles.__tablename__'), ForeignKey('characters.__tablename__'), ForeignKey('planets.__tablename__')) 
   

    def to_dict(self):
        return {}





## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')