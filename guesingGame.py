import random
yourNum = input("Enter a number between 1-10: ")
print(yourNum)
chances = 0
number = random.randint(1,9)

while chances < 5:
    if (yourNum == number):
        print("Congrats you win!")
        break
    if not (chances < 5):
        print("You lose! the number is",number)
    
    