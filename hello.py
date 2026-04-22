import random 
choice = "yes"
while choice == "yes":
    number = random.randint(1,100)
    usernumber = 0
    mode = int(input("Choose difficulty: 1.hard 2.medium 3.easy"))
    if mode == 1:
        totaltries = 5
        tries = totaltries
    elif mode == 2:
        totaltries = 7
        tries = totaltries
    elif mode == 3:
        totaltries = 10
        tries = totaltries
    else:
        print("invalid input, set to medium")
        totaltries = 7
        tries = totaltries

    while True:
        usernumber = int(input("Guess the number-"))
        tries -= 1
        if usernumber > number:
            print("too big")
            print("Attempts left:",tries)
        elif usernumber < number:
            print("too small")
            print("Attempts left:",tries)
        else:
            print("U got it!")
            print(f"U guessed it in {totaltries - tries} tries")   
            break
        if tries == 0:
            print("You lost,the number was",number)
            break
    choice = input("Play again? (yes/no): ").lower()               

    