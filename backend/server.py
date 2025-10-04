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

APP_NAME = "GRS - APP"
PREFIX_URI="/api/v1"

@app.get(f"{PREFIX_URI}/greeting")
def index():
    return {"message": f"Bienvenido a {APP_NAME}"}

@app.post(f"{PREFIX_URI}/login")
def login(credentials: Credential):
    print(credentials)
    credentials.names = "Juan Ramos"
    return credentials