from fastapi import FastAPI
from setting import Config

config = Config()

app = FastAPI(
    title="Api",
    version="0.0.0.1 beta"
)

config.addOrigin([
    "http://localhost:5731"
])

config.addStatic([
    {"subpath": "/public", "dir": "public", "name": "public"}
])

config.config(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8080, reload=True)
