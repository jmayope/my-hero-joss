from .person import Person
from .role import Role
from typing import List

class Staff:
    def __init__(self, person: Person, username: str, password: str, status: bool, roles: List[Role]):
        self.person = person
        self.username = username
        self.password = password
        self.status = status
        self.roles = roles
    
    def __str__(self):
        return f"Colaborador: {self.person.last_names} {self.person.names} - {'Activo' if self.status else 'Inactivo'}"