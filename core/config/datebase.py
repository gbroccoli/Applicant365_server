from core.config.config import EnvVariables
from sqlalchemy.orm import DeclarativeBase
from typing import Dict

class Base(DeclarativeBase):
	pass

envDB = EnvVariables()

DB_CONFIG: Dict[str, str] = {
    "HOST": envDB.get_value("DB_HOST"),
    "PORT": int(envDB.get_value("DB_PORT", 5432)),
    "USER": envDB.get_value("DB_USER"),
    "PASSWORD": envDB.get_value("DB_PASSWORD"),
    "NAME": str(envDB.get_value("DB_NAME")),
}