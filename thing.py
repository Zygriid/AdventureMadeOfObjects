from entity import Entity

class Thing(Entity):

    def __init__(self, name, description):
        super().__init__(name, description)

class Treasure(Thing):

    def __init__(self, name, description, value):
        super().__init__(name, description)
        self._value = value
        self._description = description

    def __str__(self):
        return f"""{self._description} worth {self._value}"""

class Weapon(Thing):

    def __init__(self, name, description):
        super().__init__(name, description)

class Resource(Thing):

    def __init__(self, name, description):
        super().__init__(name, description)

