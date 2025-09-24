class AuditableUnit:
    def __init__(self, name: str, address:str, phone: str, email: str, latitude: float, longitude: float):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.latitude = latitude
        self.longitude = longitude
    
    def __str__(self):
        return f"{self.name} {self.address} | Ubicado: Lat: {self.latitude}, Lng: {self.longitude}"