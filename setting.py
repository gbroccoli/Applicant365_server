from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from routers import urls


class Config:

	def __init__(self):
		self.origins:List[str] = ["http://localhost","http://localhost:8080"]
		self.static: List[str] = []
		self.url: List = urls

	def config(self, app: FastAPI):
		app.add_middleware(
			CORSMiddleware,
			allow_origins=self.origins,
			allow_credentials=True,
			allow_methods=["*"],
			allow_headers=["*"],
		)

		for route in self.url:
			print(route)

	def addOrigin(self, origins: List[str]):
		for origin in origins:
			self.origins.append(origin)

