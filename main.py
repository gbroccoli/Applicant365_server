from fastapi import FastAPI
from setting import Config
from app.core.config import EnvVariables
from app.core.models.ListModel import EnvMain

var = EnvVariables()

env = EnvMain(
    title=var.get_value("APP_NAME"),
    debug=bool(var.get_value("APP_DEBUG")),
    version=str(var.get_value("APP_VERSION")),
)

config = Config()



app = FastAPI(
    title=env.title,
    version=env.version,
    debug=env.debug
)

config.addOrigin([
    "http://localhost:5173"
])

config.addStatic([
    {"subpath": "/public", "dir": "public", "name": "public"}
])

config.config(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8080, reload=True)
