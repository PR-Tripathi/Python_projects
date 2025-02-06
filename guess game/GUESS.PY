from random import randint

Easy_level_turns = 10
Hard_level_turns= 5

def check_answer(Guess,Answer,turns):
    if Guess>Answer:
        print("Too high")
        return turns-1
    elif Guess<Answer:
        print("Too Low")
        return turns-1
    else:
        print(f"YOU GUESSED CORRECT ANSWER  THE ANSWER IS {Answer}: ")

def set_dificulty():
    Level= input("Choose difficulty type : type 'easy' or 'hard'")
    if Level =="easy":
        return Easy_level_turns
    else:
        return Hard_level_turns
def game():
    print("WELCOME TO THE GUESS GAME : ")
    print("Thinking Number Between 1 and 100")
    Answer=randint(1,100)

   # print(f"psssst,The correct answer is{Answer}")
    turns=set_dificulty()
    print(f"You Have {turns} turns")

    Guess=0
    #while Guess!=Answer:

    while Guess!=Answer:
        print(f"you have {turns} remaining to guess")
        Guess=int(input("Enter your Guessd value  "))

        turns= check_answer(Guess,Answer,turns)
        
        if turns==0:
            print("You have no remaining turn ")
        elif Guess!=Answer:
            print("Guess Again")

game()
