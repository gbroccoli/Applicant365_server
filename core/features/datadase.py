import logging
from core.config.datebase import async_session_maker
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError



class DatabaseCRUD:
	
	@classmethod
	async def insertDB(cls, *, query: str, data: dict):
		logger = logging.getLogger(__name__)
		try:
			async with async_session_maker() as session:
				querys = text(query)
				await session.execute(querys, data)
				await session.commit()

				return True
		except:
			return False

	@classmethod
	async def selectDB(cls, *, query: str, data: dict):
		logger = logging.getLogger(__name__)
		try:
			async with async_session_maker() as session:
				querys = text(query)
				res = await session.execute(querys, data)
				rows = res.fetchall()
				return rows
		except SQLAlchemyError as e:
			return e

