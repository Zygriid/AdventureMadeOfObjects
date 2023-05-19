import unittest
from unittest.mock import patch
from thing import *
from actor import *
from cave import *
from place import *


class tests(unittest.TestCase):

    def setUp(self):
        # Create a room instance and other necessary objects
        # for testing the monsterattack function
        self.room1 = Room("Room1", 'a nice room')
        self.room2 = Room("Room2", "A spacious room")
        self.room3 = Room("room3", 'A wonderful room')
        self.room1.connect("N", self.room2)
        self.room2.connect("S", self.room1)
        self.room1.connect("E", self.room3)

        self.player = Player(self.room1, "Me", "the player")
        self.monster = Monster(self.room1, "Monster", "a fierce monster", 'Food', 'axe', self.player)
        self.room1._contents = [self.monster, self.player]

    def test_appease_monster_with_food(self):

        # Call the monsterappease function
        self.player.resources.append("Food")
        self.player.monsterappease(self.monster,"Food")

        # Assert the expected behavior
        self.assertNotEqual(self.player.room, self.monster.room)
        self.assertNotIn("Food", self.player.resources)

    def test_appease_monster_without_food(self):
        with self.assertRaises(PlayerDiedException):
            self.player.monsterappease(self.monster, "")


    def test_attack_monster_with_weapon(self):
        # Test the monsterattack function
        self.weapon = Weapon("axe", "a sharp axe")
        self.player.things.append(self.weapon)
        self.assertTrue(self.weapon in self.player.things)

        self.player.monsterattack(self.monster, 'axe')
        self.assertNotIn(self.monster, self.player.room._contents)

    def test_attack_monster_without_weapon(self):
        # Test if the player cannot attack the monster without having a weapon
        weapon = 'sword'
        with self.assertRaises(PlayerDiedException):
            self.player.monsterattack(self.monster, weapon)

    def test_increase_hunger_and_thirst(self):
        # Verify initial hunger and thirst values
        self.assertEqual(self.player.get_hunger(), 0)
        self.assertEqual(self.player.get_thirst(), 0)

        # Increase hunger and thirst
        self.player.increase_hunger_and_thirst()

        # Verify updated hunger and thirst values
        self.assertEqual(self.player.get_hunger(), 1)
        self.assertEqual(self.player.get_thirst(), 0)

        # Increase hunger and thirst again
        self.player.increase_hunger_and_thirst()

        # Verify updated hunger and thirst values
        self.assertEqual(self.player.get_hunger(), 1)
        self.assertEqual(self.player.get_thirst(), 1)

        # Increase hunger and thirst one more time
        self.player.increase_hunger_and_thirst()

        # Verify updated hunger and thirst values
        self.assertEqual(self.player.get_hunger(), 2)
        self.assertEqual(self.player.get_thirst(), 1)

    def test_pick_up_food(self):

        # Test if the player can successfully pick up food
        item = "food"
        room_contents = ["food"]
        self.player.room._contents = room_contents
        self.player.pick_up(item)
        # Check if the item is added to the resources list
        self.assertIn(item, self.player.resources)
        # Check if the hunger is reset to 0
        self.assertEqual(self.player.get_hunger(), 0)

    def test_pick_up_weapon(self):
        # Test if the player can pick up a generic item (axe)
        item = "axe"
        room_contents = ["axe"]
        self.player.room._contents = room_contents
        self.player.pick_up(item)
        # Check if the item is added to the things list
        self.assertIn(item, self.player.things)

    def test_pick_up_nonexistent_item(self):
        # Test if the player cannot pick up a nonexistent item (key)
        item = "key"
        room_contents = ["food", "water", "axe"]
        self.player.room._contents = room_contents
        self.player.pick_up(item)
        # Check if the item is not added to the resources list
        self.assertNotIn(item, self.player.resources)
        # Check if the item is not added to the things list
        self.assertNotIn(item, self.player.things)

    def test_move_valid_direction(self):
        # Mocking the input to simulate the player choosing a valid direction
        self.player.move("N")

        # Assert that the player's current room has changed to room2
        self.assertEqual(self.player._room, self.room2)


    def test_move_invalid_direction(self):
        # Mocking the input to simulate the player choosing an invalid direction
        self.player.move('W')

        # Assert that the player's current room remains unchanged
        self.assertEqual(self.player.room, self.room1)


if __name__ == '__main__':
    unittest.main()
