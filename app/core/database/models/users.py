from sqlalchemy import Column, Integer, String
from core.config.datebase import Base

class Users(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True, autoincrement=True)
	surname = Column(String(50), nullable=False)
	name = Column(String(50), nullable=False)
	patronymic = Column(String(50), default=None)
	login = Column(String, nullable=False)
	passwd = Column(String(255), nullable=False)
	

__all__ = ['Users']