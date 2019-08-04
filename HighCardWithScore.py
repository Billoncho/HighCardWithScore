# HighCardWithScore.py
# Billy Ridgeway
# Plays a card game called War. User vs. Player.

import random       # Imports the random library.
answer = ""         # Sets the answer to [Enter]
myScore = 0         # Keeps track of the player's score.
yourScore = 0       # Keeps track of the computer's score.
tieScore = 0        # Keeps track of the number of tied scores.
handsPlayed = 0     # Keeps track of how many hands have been played.

# Creates a list of card suits.
suits = ["clubs", "diamonds", "hearts", "spades"]

# Creates a list of the card faces.
faces = ["two", "three", "four", "five", "six",
         "seven", "eight", "nine", "ten", "jack",
         "queen", "king", "ace"]

# Creates a while loop that generates the cards and evaluates
# who won the game. The loop continues as long the user presses Enter.
#  If the user presses any other key the game will exit.
for n in range(26):                     # Set n to the number of deals with 2 people playing cards.
    my_face = random.choice(faces)
    my_suit = random.choice(suits)
    your_face = random.choice(faces)
    your_suit = random.choice(suits)
    print("I have the", my_face, "of", my_suit, ".")
    print("You have the", your_face, "of", your_suit, ".")

    if faces.index(my_face) > faces.index(your_face):
        myScore = (myScore + 1)
        if tieScore != 0:
            myScore = (myScore + tieScore)
            tieScore = 0
        print("I win! My score is: ", myScore, "Your score is: ", yourScore)
    elif faces.index(my_face) < faces.index(your_face):
        yourScore = (yourScore + 1)
        if tieScore != 0:
            yourScore = (yourScore + tieScore)
            tieScore = 0
        print("You win! My score is: ", myScore, "Your score is: ", yourScore)
    else:
        tieScore = (tieScore + 1)
        print("It's a tie!")
    answer = input("Hit [Enter] to keep going, or any key to exit: ")
    if answer != "":
        break
print()
print("The final scores are: My Score: ", myScore, " and Your Score: ", yourScore)
if myScore > yourScore:
    print("       I win!")
elif myScore < yourScore:
    print("       You win!")
else:
    print("       We tied!")
print("Thank you for playing.")
print()
