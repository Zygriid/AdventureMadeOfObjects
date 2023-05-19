Reciprocal Relationships:

Created reciprocal relationships between the player, monsters, rooms. 

created a method inside the Player class that calls a method in the Monster class to execute interactions centering around appeasment and battle

Introduced the attributes hunger and thirst to the Player class.



Unitests

i made a file called unit_tests in order to test my code. I made this a little too far into the process, and found that much of the code i had written did not work. 

The setUp method is used to set up the necessary objects and environment before each test is executed. It creates instances of the Room, Player, and Monster classes and initializes their attributes accordingly.

The file includes the following unit tests:

test_appease_monster_with_food: Tests if the player can successfully appease the monster by providing the correct food item.
test_appease_monster_without_food: Tests if the player dies when attempting to appease the monster without the required food item.
test_attack_monster_with_weapon: Tests if the player can successfully attack and kill the monster using a weapon.
test_attack_monster_without_weapon: Tests if the player dies when trying to attack the monster without a weapon.
test_increase_hunger_and_thirst: Verifies that the player's hunger and thirst levels increase as expected.
test_pick_up_food: Tests if the player can pick up food and verifies the corresponding changes in hunger.
test_pick_up_weapon: Tests if the player can pick up a weapon.
test_pick_up_nonexistent_item: Tests if the player cannot pick up a nonexistent item.

In doing these unit tests I learned I had been doing inhertinace wrong, and alot of my reciproical relationships were unfunctional. I spent a lot of time amending those. I wrote unit tests, and then spent whole coding sessions debugging just one unitest! fix on error, and on to the next. Pycharm's error handling was really useful. 
