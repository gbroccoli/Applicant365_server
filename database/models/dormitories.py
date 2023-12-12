from sqlalchemy import Column, Integer, String
from core.config.datebase import Base

class Dormitories(Base):

	__tablename__ = "dormitories"

	id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
	name = Column(String(50), nullable=False)
	address = Column(String(150), nullable=False)

# __all__ = ["Dormitories"]