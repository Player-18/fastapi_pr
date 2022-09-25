from sqlalchemy import Column, String, Integer, Text, DateTime, Boolean
from core.bd import Base


class User(Base):
    __tablename__ = "fastdb_users"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    date = Column(DateTime)
    is_admin = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
