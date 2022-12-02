import random
import math

rules = {
    'scissors': {
        'paper': "WIN",
        'stone': "LOOSE",
        'scissors': "TIE"
    },
    'paper': {
        'paper': "TIE",
        'stone': "WIN",
        'scissors': "LOOSE"
    },
    'stone': {
        'paper': "LOOSE",
        'stone': "TIE",
        'scissors': "WIN"
    },
}

def randomiseWord():
    randomisedNumber = math.floor(random.random()*3)
    randomisedWord = ["paper", "scissors", "stone"][randomisedNumber]
    return randomisedWord

while 1:
    inputWord = input("Enter your choise (for ex. paper, scissors, stone):")
    computerChoose = randomiseWord()
    if inputWord in rules:
        matchResult = rules[inputWord][computerChoose]
        print(f"I choosed {computerChoose} so it's {matchResult} \n")
    else:
        print("\nyou made a mistake while typing, try again😚")