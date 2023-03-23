# example = [1,2,3,4,5,6,7]
from random import shuffle
# shuffle(example)
# print(example)

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

# mylist = [" ", "O", " "]

def player_guess ():
    guess = ''
    while guess not in ["0", "1", "2"]:
        guess = input("Pick a number: 0, 1, or 2 - ")
    return int(guess)
    

def check_guess(mylist, guess):
    if mylist[guess] == 'O':
            print("Winner, Winner, Chicken Dinner!!!")
            print(mylist)
    else:
            print("Too Bad, Sucker!!!")
            print(mylist)

print("==================================")

mylist = [" ", "O", " "]
mixedup_list = shuffle_list(mylist)
guess = player_guess()
check_guess(mixedup_list, guess)