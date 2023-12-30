import os
import gtts
import random
from playsound import playsound

def text_speech(speech):
    speech_file = gtts.gTTS(speech)
    speech_file.save("speech.mp3")
  
    playsound("speech.mp3")

    os.remove("speech.mp3")

def random_number():
    r_int = random.randint(0, 2)
    if r_int == 0:
        return "rock"
    elif r_int == 1:
        return "paper"
    elif r_int == 2:
        return "scissors"

def check_win(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "-- Its a Draw!"
    elif comp_choice == "paper" and user_choice == "rock":
        return "-- Computer wins the game!"
    elif comp_choice == "rock" and user_choice == "scissors":
        return "-- Computer wins the game!"
    elif comp_choice == "scissors" and user_choice == "paper":
        return "-- Computer wins the game!"
    else:
        return "-- User won the game this time!"

def check_value(user_input):
    valid_tpl = ("rock", "scissors", "paper")
    if user_input.lower() in valid_tpl:
        return True
    else:
        return False

def output_text(user_choice, comp_choice, result):
    if result == "-- Its a Draw!":
        text_speech(f"You entered {user_choice}. Computer chose {comp_choice}.")
        print("-- Its a Draw!")

    elif result == "-- Computer wins the game!":
        text_speech(f"You entered {user_choice}. Computer chose {comp_choice}.")
        print("-- Computer wins the game!")
    
    else:
        text_speech(f"You entered {user_choice}. Computer chose {comp_choice}.")
        print("-- User won the game this time!")

def scores(result, scores_list):
    if result == "-- Its a Draw!":
        scores_list[0] += 1
    elif result == "-- User won the game this time!":
        scores_list[1] += 1
    else:
        scores_list[2] += 1
    return scores_list

scores_list = [0, 0, 0]

print("\n")

flag = True
while flag:
  
    text_speech("Please enter either Rock, Paper or Scissors : ")
    user_choice = input("Please enter either Rock, Paper or Scissors : ")
    user_choice = user_choice.lower()

    check = check_value(user_choice)

    while check is False:
        text_speech("Error! Please input Rock, Paper or Scissors.")
        user_choice = input("Choose either Rock, Paper or Sciccors >>>")
        check = check_value(user_choice)
    
    comp_choice = random_number()
    result = check_win(user_choice, comp_choice)
    output_text(user_choice, comp_choice, result)
    scores_list = scores(result, scores_list)

    print("\n")

    count = input("Do you like to continue? (yes/no) : ")

    if count.lower() != "yes":
        flag = False

else:
    text_speech("Thank you so much for playing this game!")
    
    print(f"""\n\t\t----SCOREBOARD----\n
    \t\tNumber of draws : {scores_list[0]}
    \t\tUser Wins : {scores_list[1]}
    \t\tComputer Wins : {scores_list[2]}""")
