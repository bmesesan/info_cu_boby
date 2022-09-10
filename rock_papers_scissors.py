import time
import random

def main():
    user_score = 0
    computer_score = 0
    three_games = 3

    print("Let's play rock/paper/scissors, a match of best of 3!")
    time.sleep(1)


    while three_games > 0 :
        user_choice = input("Choose between rock/paper/scissors: ")
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print("The computer chose: " + computer_choice)
        time.sleep(1)
        
        if computer_choice == user_choice.lower():
            print("This game is a draw, let's redo it.")
            three_games += 1
            
        elif computer_choice == "rock" and user_choice.lower() == "paper":
            print("You won this one!")
            user_score += 1
        elif computer_choice == "paper" and user_choice.lower() == "scissors":
            print("You won this one!")
            user_score += 1
        elif computer_choice == "scissors" and user_choice.lower() == "rock":
            print("You won this one!")
            user_score += 1
            
        elif computer_choice == "rock" and user_choice.lower() == "scissors":
            print("The computer won this one!")
            computer_score += 1
        elif computer_choice == "paper" and user_choice.lower() == "rock":
            print("The computer won this one!")
            computer_score += 1
        elif computer_choice == "scissors" and user_choice.lower() == "paper":
            print("The computer won this one!")
            computer_score += 1
        else:
            print("You have mispelled the word, let's try again.")
            three_games += 1
        time.sleep(1)
        three_games -= 1
            
    if user_score > computer_score:
        print("Congrats, you won the entire match!")
    elif user_score < computer_score:
        print("The computer won the entire match, good luck next time!")



if __name__ == "__main__":
    main()