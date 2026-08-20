from fastapi import FastAPI

from app.lib.env import initEnv
from app.lib.autoloader import autoloader
initEnv(path=".", file=".env")

app = FastAPI()

autoloader(app)