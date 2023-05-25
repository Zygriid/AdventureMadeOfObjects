from entity import Entity

class Place(Entity):

    def __init__(self, name, description):
        super().__init__(name, description)
        self._contents = {}
        self._connections = {}

    def get_place(self, direction):
        return self._connections.get(direction, None)

    def get_connections(self):
        return self._connections

class Room(Place):

    def __init__(self, name, description, roommonster=[]):
        super().__init__(name, description)
        self._contents = []
        self._connections = {}
        self._name = name
        self.roommonster = roommonster

    def connect(self, direction, other):
        assert direction in ['N', 'E', 'W', 'S']
        self._connections[direction] = other

    def add_content(self, content):
        self._contents.append(content)

    def remove_content(self, content):
        if content in self._contents:
            self._contents.remove(content)

    def describe(self):
        print("You are in", self._name)
        print(self._description)
        print("Contents:", ", ".join(str(content) for content in self._contents))

    def has_monster(self):
        return len(self.roommonster) > 0


class Passage(Place):
    """Goes from one room to another where rooms do not
connect directly"""

    def __init__(self, name, description):
        super().__init__(name, description)

