from fastapi import FastAPI
from core.config.app import Config
from core.config.config import EnvVariables
from core.models.ListModel import EnvMain

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
	redoc_url=env.redoc_url
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

Config().run(app)
# config.config(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8080, reload=True)
