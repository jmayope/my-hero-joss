from pydantic import BaseModel
<<<<<<< HEAD
from typing import Optional, Dict

class Credential(BaseModel):
    username: str
    password: str
    names: Optional[str] = ""
=======

class Credential(BaseModel):
    username: str
    password: str
>>>>>>> 029b27d96471254b3a5c082ad1b689f241995d84
