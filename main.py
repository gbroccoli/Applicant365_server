from fastapi import FastAPI
from setting import Config

config = Config()
app = FastAPI(
	title="Api",
	version="1.0"
)
config.config(app)

config.addOrigin([
	"http://localhost:5731"
])

@app.get("/", include_in_schema=False)
async def index():
	return {"status": "success"}


if __name__ == "__main__":
	import uvicorn
	uvicorn.run("main:app", host="localhost", port=8080, reload=True)