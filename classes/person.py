class Person:

    def __init__(self, names: str, last_names: str, birth_date: str, gender: bool):
        self.names = names
        self.last_names = last_names
        self.birth_date = birth_date
        self.gender = gender
    
    def introduce(self):
        return f"{self.last_names} {self.names} - {'Masculino' if self.gender else 'Femenino'}"
    
