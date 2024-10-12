import random
should_continue = True
print("welcome in game")
print("computer thinking random number btw 1 to 100:")

chosen_num = random.randint(1,100)
# print(chosen_num)


guess =0 
dicide = input("select easy or hard level")
def game_logic():
    global guess

    if guess > chosen_num:
        print("too high \n guess again...")
    elif guess < chosen_num:
        print("too low \n guess again...")
def low():
    for life in range(10,0,-1):
        global guess
        print(f"you have {life} remaining to guess a number.")  
        guess= int(input("guess the number"))
        if guess == chosen_num:
            print("you got it -- win")
            break
        elif life == 1 and guess != chosen_num:
            print("YOU LOSE BUDDY, TRY AGAIN")
        else:
            game_logic()

    
def high():
    for life in range(5,0,-1):
        global guess
        print(f"you have {life} remaining to guess a number.")
        guess = int(input("guess the number"))
        if guess == chosen_num:
            print("you got it -- win")
            break
        elif life == 1 and guess != chosen_num:
            print("YOU LOSE BUDDY , TRY EASY ")
        else:
            game_logic()
        
while should_continue:
    if dicide == 'easy':
        low()
        should_continue = False
    else:
        high()
        should_continue = False
