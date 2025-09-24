from .residue_type import ResidueType

class Residue:
    def __init__(self, name: str, type: ResidueType, description, category, sub_category):
        self.name = name
        self.type = type
        self.description = description
        self.category = category
        self.sub_category = sub_category
    
    def __str__(self):
        return f"{self.name} - {self.category} - {self.sub_category}"
