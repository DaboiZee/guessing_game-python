import random 
def welcome():
    print("lets play a game im gonna think of a number between 1 and 10 and you guess it ")
    print("ready?Go!!!!")
def get_guess():
    guess=int(input("enter number: "))
    return guess
def win_check(computer_number,guess,tries_count,tries,win):
    if computer_number==guess:
        win=True
        return True, win
    elif tries==tries_count and computer_number!=guess:
        win=False
        return True, win
    else:
        win=False
        return False, win
def answer_checker(computer_number,guess):
    if computer_number>guess:
        return f"{guess} is smaller than my number"
    elif computer_number<guess:
        return f"{guess} is larger than my number"
    else:
        return f"{guess} is the correct number"
def finish(tries,tries_count,computer_number,win):
    if win:
        print(f"good job you found the number in {tries_count} tries") 
    else:
        print(f"nice try! my number was {computer_number}")    
    again=input("would you like to continue: (Y/N)")   
    return again
def main_game():
    guess=0
    tries=10  
    tries_count=0
    win=False
    computer_number=random.randint(1,10)

    a,b=win_check(computer_number, guess,tries_count,tries,win)
    while not a:
        guess=get_guess()
        tries_count+=1
        print(answer_checker(computer_number,guess))
        a,b=win_check(computer_number, guess,tries_count,tries,win) 
    return finish(tries,tries_count,computer_number,b),tries_count,b
best_score=float("inf")
welcome()
while True:
    c,d,e=main_game()
    if d<best_score and e :
            best_score=d
    if c.upper() not in ["YES","Y"]:
        if best_score==float("inf"):
             print("you have not won yet so there is no best score ")  

        else: 
            print(f"best score: correct guess in {best_score} tries")
        break