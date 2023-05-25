from cave import *
from place import *
from thing import *
from actor import *


class Adventure:
    cave_layout = {
        'RA': {'N': 'RB', 'S': 'RC'},
        'RB': {'E': 'RD', 'W': 'RE'},
        'RC': {'W': 'RA', 'E': 'RB', 'S': 'RD'},
        'RD': {'W': 'RB', 'E': 'RC'},
        'RE': {'E': 'RB', 'S': 'RF'},
        'RF': {'N': 'RE'}
    }

    def __init__(self):
        self.setup_cave()
        self.create_things()
        self.create_monsters()
        self.create_player()

    def setup_cave(self):
        self._cave = Cave()
        self.create_rooms()
        self.create_passages()
        self.connect_places()

    def create_rooms(self):
        for room_name, description in [
            ('RA', "room A"),
            ('RB', "room B"),
            ('RC', "room C"),
            ('RD', "room D"),
            ('RE', "room E"),
            ('RF', "room F")
        ]:
            self._cave.add_room(Room(room_name, description))
    def create_passages(self):
        for passage_name, description in [
            ('P1', 'passage 1'),
            ('P2', 'passage 2')
        ]:
            self._cave.add_passage(Passage(passage_name, description))

    def connect_places(self):
        for room_name, connections in self.cave_layout.items():
            for direction, other_room_name in connections.items():
                self._cave.get_room(room_name).connect(direction, self._cave.get_room(other_room_name))

    def create_things(self):
        self.create_resources()
        self.create_treasures()
        self.create_weapons()

    def create_resources(self):
        self._resources = {
            'water': Resource('water', 'water'),
            'food': Resource('food', 'food'),
        }

    def create_treasures(self):
        self._treasures = {
            'diamonds': Treasure('diamonds', '6 diamonds', 100),
            'coins': Treasure('coins', '10 coins', 50),
        }

    def create_weapons(self):
        self._weapons = {
            'axe': Weapon('axe', 'a sharp axe'),
            'rock': Weapon('rock', 'a heavy stone'),
        }

    def create_monsters(self):
        self._monsters = {
            'M1': Monster(None, 'miniturtle', 'Turtle', self._resources['food'], self._weapons['axe'], None),
            'M2': Monster(None, 'Turtlemonster', 'Boss Turtle', self._resources['water'], self._weapons['rock'], None),
        }

    def create_player(self):
        initial_room = self._cave.get_room('RA')
        self.player = Player(initial_room, 'Tosca', 'An intrepid turtle hunter', self._cave)



    def place_everything(self):
            """Put the things in rooms"""
            # Example usage:
            room = self._cave.get_room('RA')
            room.add_content(self._resources['water'])
            room.add_content(self._monsters['M1'])

    def play(self):
        print("Welcome to the Adventure Game!")
        print("================================")
        print("Instructions:")
        print("Enter commands to interact with the game.")
        print("Use 'help' to see available commands.")
        print("================================")
        self.place_everything()
        self.player.describe_current_room()

        while True:
            command = input(">>> ")
            if command == 'help':
                print("Available commands:")
                print("help - Show available commands")
                print("look - Look around the room")
                print("go <direction> - Move in a specific direction (e.g., go N)")
                print("pickup <item> - Pick up an item in the room")
                print("inventory - View your inventory")
                print("quit - Quit the game")
            elif command == 'look':
                self.player._room.describe()
            elif command.startswith('go '):
                direction = command.split(' ')[1].upper()
                self.player.move(direction)
                self.player.describe_current_room()
            elif command.startswith('pickup '):
                item = command.split(' ')[1]
                self.player.pick_up(item)
            elif command == 'inventory':
                self.player.show_inventory()
            elif command == 'quit':
                print("Thank you for playing!")
                break
            else:
                print("Invalid command. Type 'help' to see available commands.")


game = Adventure()
game.play()
