from entity import Entity
import random
from cave import *


class PlayerDiedException(Exception):
    pass
class Actor(Entity):

    def __init__(self, room, name, description):
        super().__init__(name, description)
        self._room = room

class Player(Actor):

    def __init__(self, room, name, description, cave):
        super().__init__(room, name, description)
        self.resources = []
        self.things = []
        self.room = room
        self._hunger = 0
        self._thirst = 0
        self._hunger_turn = True
        self._cave = cave

    def show_inventory(self):
        inventory = self.resources + self.things
        print("Inventory:")
        if not inventory:
            print("Empty")
        else:
            for item in inventory:
                print("- " + item.get_name())

    def get_hunger(self):
        return self._hunger
    def get_thirst(self):
        return self._thirst
    def increase_hunger(self):
        self._hunger += 1
    def increase_thirst(self):
        self._thirst += 1
    def reset_hunger(self):
        self._hunger = 0
    def reset_thirst(self):
        self._thirst = 0

    def move(self, direction):
        if self._room.get_place(direction) is not None:
            self._room = self._room.get_place(direction)
            monsterlist = self._cave.get_monsterindex()
            for monster in monsterlist:
                monster.receivemove(direction)
            self.increase_hunger_and_thirst()
            self._room.describe()
            if self._room.has_monster():
                print("Monsters in the room:")
                for monster in self.roommonster:
                    print(monster.get_name())
                self.handle_monster()

            else:
                print("There are no monsters in the room.")



        else:
            print("You cannot move in that direction.")

    def increase_hunger_and_thirst(self):
        if self._hunger_turn:
            self._hunger += 1
        else:
            self._thirst += 1
        self._hunger_turn = not self._hunger_turn

    def describe_current_room(self):
        room = self._room
        print(f"You are in {room.get_name()}. {room.get_description()}")

    def pick_up(self, item):
        if item in self.room._contents:
            if item == "food":
                self.reset_hunger()
                print("You pick up the food.")
                self.resources.append(item)
            elif item == "water":
                self.reset_thirst()
                print("You pick up the water.")
                self.resources.append(item)
            else:
                print(f"you pick up the {item}")
                self.things.append(item)
        else:
            print("There is no such thing!")

    def handle_monster(self):
        action = input("What do you want to do? (Try to appease the monster or fight the monsterr? (appease/fight)): ")
        if action.lower() == "appease":
            self.monsterappease()
        elif action.lower() == "attack":
            self.monsterattack()
        else:
            print("Invalid action. Please choose 'monsterappease' or 'monsterattack'.")

    def monsterattack(self, monster_name, weapon):
        if self.room == monster_name.room:
            monster_name.recieveattack(self, weapon)
        else:
            print(f"Luckily, you are not in the same room as {monster_name}")

    def monsterappease(self, monstername, item):
        if self.room == monstername.room:
            monstername.recieveappease(self, item)
            self.resources.remove(item)
        else:
            print(f"You arent in the same room as {monstername}!")

    def die(self):
        raise PlayerDiedException('you have been killed.')

class Monster(Actor):

# replace player with self.cave.player for readiblity?
    def __init__(self, room, name, description, wants, killed_by, player):
        super().__init__(room, name, description)
        self._wants = wants
        self._killed_by = killed_by
        self._player = player
        self.room = room
        self.name = name

    def recieveattack(self, player, weapon):
        if weapon == self._killed_by:
            self._player.room._contents.remove(self)  # Remove the monster from the room's contents
            del self  # Delete the monster object
            return f'you have killed the monster'
        else:
            print('the monster kills you')
            player.die()

    def recieveappease(self, player, food):
        if food == self._wants:
            #choose random room
            self.room = random.choice(list(self.room._connections))
            print(f'{self.name} has been appeased and has moved rooms')

        else:
            print('Appeasing failed')
            player.die()


    def receivemove(self, direction):
        if self._room.get_place(direction) is not None:
            self._room = self._room.get_place(direction)
        else:
            pass













