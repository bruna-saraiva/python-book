import random

trial = 0
# create a random number
random_number = random.randint(1,10)
while trial < 3:
    user_number = int(input("choose your number: "))

    
    print(f"the number you chose is {user_number}")
    if user_number == random_number:
        print("congratz, you got it right")
        print(f"the right number is {random_number}")
        break

    else:
        print("ouch.. looks like you got it wrong")
        trial+=1
        left_trials = 3 - trial
        if left_trials > 0:
            print(f"try again, you have more {left_trials}")
    
    print(f"the right number is {random_number}")