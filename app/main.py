from fastapi import FastAPI
from modules.env import initEnv, getEnvByKey

initEnv(path="..", file=".env")  

app = FastAPI()
