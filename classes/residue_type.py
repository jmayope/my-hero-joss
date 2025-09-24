class ResidueType:
    def __init__(self, name: str, description: str, status: bool):
        self.name = name
        self.description = description
        self.status = status
    
    def __str__(self):
        return f"{self.name} - {self.description} - {'Activo' if self.status else 'Inactivo'}"