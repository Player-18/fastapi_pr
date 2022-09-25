from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from core.bd import Base


class Post(Base):
    __tablename__ = "fastdb_posts"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    text = Column(Text)
    date = Column(DateTime)
    user = Column(Integer, ForeignKey("fastdb_users.id"))
    user_id = relationship("User")

