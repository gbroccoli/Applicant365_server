from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from typing import List, Dict
from routers import urls
from app.core.models.ListModel import StaticType


class Config:

    def __init__(self):
        self.origins: List[str] = ["http://localhost", "http://localhost:8080"]
        self.static: List[StaticType] = []
        self.urls: List = urls

    def config(self, app: FastAPI):
        app.add_middleware(
            CORSMiddleware,
            allow_origins=self.origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        for static in self.static:
            app.mount("{}".format(static.subpath), StaticFiles(
                directory=static.dir), name=static.name)

        for url in self.urls:
            app.include_router(url)

    def addOrigin(self, origins: List[str]):
        for origin in origins:
            self.origins.append(origin)

    def addStatic(self, arrayStatic: List[Dict]):
        for array in arrayStatic:
            self.static.append(StaticType(subpath="{}".format(
                array["subpath"]), dir=array["dir"], name=array["name"]))
