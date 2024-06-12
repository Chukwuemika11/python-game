import random

print("you are welcome to pyhton guessing game")

myMind = random.randint(1, 100)

choose_level = input("Choose a difficulty type 'easy' or 'hard': ")

if choose_level == 'easy':
    countDown = 10
    print(f"you have {countDown} attempts left to guess the number")

elif choose_level == 'hard':
    countDown = 5
    print(f"you have {countDown} attempts left to guess the number")

while countDown > 0:
    chosen_number =  int(input("Guess the number:"))
    if chosen_number == myMind:
      print(f"congratulations! you guessed the correct number. The number was {myMind} ")

    elif chosen_number > myMind:
        countDown -= 1
        print(f"Too high you have {countDown} guesses left")  

    elif chosen_number < myMind:
        countDown -= 1
        print(f"Too low you have {countDown} guesses left")


    if countDown == 0:
        print(f"Sorry yo cant guess again because you have {countDown} guesses left meanwhile the number was {myMind}")    
