# The code you provided is a Python script that
# sets up a FastAPI application and runs it using the
# Uvicorn server.
from fastapi import FastAPI
from core.config.app import Config
from core.config.config import EnvVariables
from core.models.ListModel import EnvMain
import logging

# Настройка логгирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

var = EnvVariables()

env = EnvMain(
    title=var.get_value("APP_NAME"),
    debug=bool(var.get_value("APP_DEBUG")),
    version=str(var.get_value("APP_VERSION")),
)

app = FastAPI(
    title=env.title,
    version=env.version,
    debug=env.debug,
    redoc_url=env.redoc_url)

Config().run(app)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host=var.get_params_local_url()[0],
        port=var.get_params_local_url()[1],
        reload=True,
    )
