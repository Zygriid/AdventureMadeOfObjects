

class Cave:

    def __init__(self, rooms=None, passages=None, monsterindex=None, playerindex=None):
        if rooms is None:
            rooms = {}
        self._rooms = rooms
        if passages is None:
            passages = {}
        self._passages = passages
        if monsterindex is None:
            monsterindex = {}
        self._monsterindex = monsterindex
        if playerindex is None:
            playerindex = {}
        self._playerindex = playerindex

    def get_passage(self, name):
        return self._passages.get(name, None)

    def get_room(self, name):
        assert name in self._rooms
        return self._rooms[name]

    def get_rooms(self):
        return self._rooms

    def get_playerindex(self):
        return self._playerindex

    def get_monsterindex(self):
        return self._monsterindex

    def add_room(self, room):
        self._rooms[room.get_name()] = room

    def add_passage(self, passage):
        self._passages[passage.get_name()] = passage

    def add_monster(self, monster):
        self._monsterindex[monster.get_name()] = monster

    def add_player(self, player):
        self._playerindex[player.get_name()] = player

    def __str__(self):
        return str("The Cave")


    def describe(self):
        print("State of the Cave:")
        print("\tConnections:")
        for room in self._rooms.values():
            print(f"\t{room.get_name()}")
            for direction, other in room.get_connections().items():
                print(f"""\t\t{direction}: {other.get_name()}""")

#    Rooms:""")

# for name, description in self._rooms.items():
#            print(f"""\t\t{name}: {description}""")
