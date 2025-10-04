from pydantic import BaseModel
from typing import Optional, Dict

class Credential(BaseModel):
    username: str
    password: str
    names: Optional[str] = ""
