import random
import pyttsx3
import sys

number = random.randint(0, 100)
max_guess_number = 6
guess_number = 0
engine = pyttsx3.init()
engine.setProperty('rate', 170)     # setting up new voice rate
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[0].id)   # 1 for female, 0 for male

while (guess_number < max_guess_number):
    guess = int(input(f"please enter your guess (an integer number between 0-100, you have {max_guess_number} chances): "))

    if number < guess:
        print("Lower")
        engine.say("Lower!")
        engine.runAndWait()

    elif number > guess:
        print("Higher")
        engine.say("Higher!")
        engine.runAndWait()

    else:
        print("Congratulations! you win!")
        engine.say("Congratulations! you win!")
        engine.runAndWait()
        sys.exit()

    guess_number += 1


print("You Lose!")
engine.say("You Lose!")
engine.runAndWait()
