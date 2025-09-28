from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.credential import Credential

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

PREFIX_URI = "/api/v1"

@app.get(f"{PREFIX_URI}/greeting")
def index():
    return {"message": "Hola Mundo, Bienvenido"}

@app.post(f"{PREFIX_URI}/login")
async def login(credential: Credential):
    print(credential)
    return credential