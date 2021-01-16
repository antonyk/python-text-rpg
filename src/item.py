# All objects will inherit from "item"

# IS vs HAS --
# use IS (inheritance) as a way to easily configure; 



class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Equipment(Item):
    def __item__(self, name, description, bodypart, protection):
        super().__init__(name, description)
        self.bodypart = bodypart
        self.protection = protection


items = {
    ''
}
