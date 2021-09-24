from random import randint
#random generated

#list of choices
choice = ["Heads", "Tails"]

#computer to choose a random from 0-1
computer = choice[randint(0,1)]


print("\n\nYou flipped {}".format(computer))
