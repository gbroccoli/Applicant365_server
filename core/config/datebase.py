from core.config.config import EnvVariables
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from typing import Dict

class Base(DeclarativeBase):
	pass

envDB = EnvVariables()

DB_CONFIG: Dict[str, str | int] = {
    "HOST": envDB.get_value("DB_HOST") or "",
    "PORT": int(envDB.get_value("DB_PORT", 5432) or 5432),
    "USER": envDB.get_value("DB_USER"),
    "PASSWORD": envDB.get_value("DB_PASSWORD"),
    "NAME": str(envDB.get_value("DB_NAME")),
}

DATA_URL = f"postgresql+asyncpg://{DB_CONFIG['USER']}:{DB_CONFIG['PASSWORD']}@{DB_CONFIG['HOST']}:{DB_CONFIG['PORT']}/{DB_CONFIG['NAME']}"

engine = create_async_engine(DATA_URL)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)