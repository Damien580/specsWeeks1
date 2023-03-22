def player_guess():
    guess = ''
    while guess not in ["0", "1", "2"]:
        guess = input(" Pick a number: 0, 1 or 2! ")
    return int(guess)

my_index = player_guess()
print(my_index)


example = [1, 2, 3, 4, 5, 6, 7]
from random import shuffle
shuffle(example)


def shuffle_cup(my_list):
    shuffle(my_list)
    return my_list

result = shuffle_cup(example)


my_cups = [" ", "O", " "]

print(shuffle_cup(my_cups))

print('==========================================')