
# Game of Greed 1

Submission pull request: [here](https://github.com/GameofGreed/game_of_greed/pull/6)

__________
#### Developers: Kim Damalas, Amber Falbo, Brandon Gonzalez, Mason Fryberger
#### Created: 27 December 2020
#### Version 1.0 
#### Class: seattle-py-401n2
___________
## Description
___________

This module creates a command line version of the dice game `Game of Greed`

Review [rules of game](https://en.wikipedia.org/wiki/Dice_10000)

Play the game [online](http://www.playonlinedicegames.com/farkle)

____________
## Feature Tasks and Requirements
___________

1. Define a `GameLogic` class in `game_of_greed/game_logic.py file`.

2. Handle calculating score for dice roll:
- Add `calculate_score` static method to `GameLogic` class.

    - The input to `calculate_score` is a tuple of integers that represent a dice roll.

    - The output from `calculate_score` is an integer representing the roll’s score according to rules of game.

3. Handle rolling dice:
- Add `roll_dice` static method to `GameLogic` class

    - The input to `roll_dice` is an integer between 1 and 6

    - The output of `roll_dice` is a tuple with random values between 1 and 6

    - The length of tuple must match the argument given to `roll_dice` method

4. Handle banking points:
- Define a `Banker` class

- Add a `shelf` instance method

    - Input to `shelf` is the amount of points (integer) to add to shelf

    - `shelf` should temporarily store ***unbanked*** points

- Add a `bank` instance method

    - `bank` should add any points on the shelf to total and reset shelf to 0

    - `bank` output should be the amount of points added to total from shelf

- Add a `clear_shelf` instance method
    - `clear_shelf` should remove all unbanked points.
______________

## Configuration and Technologies
__________

The user must have Python and all associated dependencies installed.  Poetry was used to create math-series project and the program is run by typing  `game_of_greed.py` in the command line
___________
## Changes
__________

21 Dec: set up file structure; updated README.md

22 Dec:
___________

## Testing
________
Testing accomplished using built-in `pytest` and tests coded into `test_game_logic.py`

Required tests:
### Testing - Roll Dice
When rolling 1 to 6 dice ensure…
- sequence of correct length is returned
- each item in sequence is an integer with value between 1 and 6

### Testing - Calculate Score
- zilch - non scoring roll should return 0
- ones - rolls with various number of 1s should return correct score
- twos - rolls with various number of 2s should return correct score
- threes - rolls with various number of 3s should return correct score
- fours - rolls with various number of 4s should return correct score
- fives - rolls with various number of 5s should return correct score
- sixes - rolls with various number of 6s should return correct score
- straight - 1,2,3,4,5,6 should return correct score
- three_pairs - 3 pairs should return correct score
- two_trios - 2 sets of 3 should return correct score
- leftover_ones - 1s not used in set of 3 (or greater) should return correct score
- leftover_fives - 5s not used in set of 3 (or greater) should return correct score

### Testing - Banker

`shelf`
- should properly track unbanked points
bank
- should properly add unbanked points to total and return the deposited amount

`clear_shelf`
- should remove any unbanked points, resetting to zero
- should not affect previously banked points
____________

## Contributing
____________
The team includes:  
- Kim Damalas
- Amber Falbo
- Brandon Gonzalez
- Mason Fryberger
