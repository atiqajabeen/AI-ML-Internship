import random 
secret = random.randint(1,20)
while True:
    guess = int(input("Enter a guess number:"))
    if guess == secret :
        print("Correct")
    elif guess > secret:
        print("Too high")
    else:
        print("Too low")
