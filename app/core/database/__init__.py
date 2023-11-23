from os import listdir
from importlib import import_module
from sqlalchemy.orm import DeclarativeBase
from app.core.config import EnvVariables
from typing import Dict

imported_models = []

models_directory = "app/core/database/models"

model_files = [file for file in listdir(models_directory) if file.endswith(
    ".py") and file != "__init__.py" and file != "models.py"]

for model in model_files:
    module_name = f"app.core.database.models.{model[:-3]}"
    module = import_module(module_name)

    modules_names = getattr(
        module, "__all__", [name for name in dir(module) if not name.startswith('_')])

    imported_models.extend([getattr(module, modul_name)
                            for modul_name in modules_names])


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
