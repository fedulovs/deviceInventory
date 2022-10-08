from sqlalchemy import Column, Integer, String

from database import Base

"""
Brand str
Device str
OS version str
Comments str
Not Compatible with str
"""


class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String)
    device = Column(String)
    owner = Column(String)
    os_version = Column(String)
    comments = Column(String)
    not_compatible_with = Column(String)


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    password = Column(String)
