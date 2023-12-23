import tkinter
import random

root = tkinter.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("700x800")

user_score =0
computer_score=0

random_number = random.randint(1, 3)
if random_number == 1:
    computer_choice = "R"
elif random_number == 2:
    computer_choice = "P"
elif random_number == 3:
    computer_choice = "S"

# ASCII art images for Rock, Paper, Scissors game

rock_img = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper_img = """

    __________
---'    ______)____
           ________)
          _______)
         _______)
---.__________)"""

scissors_img = """
    _______
---'   ____)____
          ______)   
       __________)   
      (____)
---.__(___)"""


# Functions creation
# rock function
def rock():
    global user_score, computer_score
    user_label_choice['text'] = rock_img
    
    # Execution based on choices
    if computer_choice == "R":
        result_label['text'] = "TIE"
        computer_label_choice['text'] = rock_img
        user_score = user_score + 1
        computer_score = computer_score + 1
        computer_score_label.config(text="COMPUTER SCORE: "+ str(computer_score))
        user_score_label.config(text="PLAYER SCORE: "+str(user_score))
        
    elif computer_choice == "P":
        result_label['text'] = "Computer wins!"
        computer_label_choice['text'] = paper_img
        computer_score = computer_score + 2
        computer_score_label.config(text="COMPUTER SCORE: "+ str(computer_score))
        
    elif computer_choice == "S":
        result_label['text'] = "Player wins!"
        computer_label_choice['text'] = scissors_img
        user_score = user_score + 2
        user_score_label.config(text="PLAYER SCORE: "+ str(user_score))

# paper function 
def paper():
    global user_score, computer_score
    user_label_choice['text'] = paper_img
    
    # Execution based on choices
    if computer_choice == "P":
        result_label['text'] = "TIE"
        computer_label_choice['text'] = paper_img
        user_score = user_score + 1
        computer_score = computer_score + 1
        computer_score_label.config(text="COMPUTER SCORE: "+ str(computer_score))
        user_score_label.config(text="PLAYER SCORE: "+str(user_score))
        
    elif computer_choice == "S":
        result_label['text'] = "Computer wins!"
        computer_label_choice['text'] = scissors_img
        computer_score = computer_score + 2
        computer_score_label.config(text="COMPUTER SCORE: "+ str(computer_score))
        
    elif computer_choice == "R":
        result_label['text'] = "Player wins!"
        computer_label_choice['text'] = rock_img
        computer_score = computer_score + 2
        computer_score_label.config(text="PLAYER SCORE: "+ str(user_score))
    
# scissors function
def scissors():
    global user_score, computer_score
    user_label_choice['text'] = scissors_img
    
    # Execution based on choices
    if computer_choice == "S":
        result_label['text'] = "TIE"
        computer_label_choice['text'] = scissors_img
        user_score = user_score + 1
        computer_score = computer_score + 1
        computer_score_label.config(text="COMPUTER SCORE: "+ str(computer_score))
        user_score_label.config(text="PLAYER SCORE: "+str(user_score))
        
    elif computer_choice == "R":
        result_label['text'] = "Computer wins!"
        computer_label_choice['text'] = rock_img
        computer_score = computer_score + 2
        computer_score_label.config(text="COMPUTER SCORE: "+ str(computer_score))
        
    elif computer_choice == "P":
        result_label['text'] = "Player wins!"
        computer_label_choice['text'] = paper_img
        user_score = user_score + 2
        user_score_label.config(text="PLAYER SCORE: "+ str(user_score))
    
# reset  function
def reset():
    global computer_choice, user_score, computer_score
    random_number = random.randint(1, 3)
    if random_number == 1:
        computer_choice = "R"
        
    elif random_number == 2:
        computer_choice = "P"
        
    elif random_number == 3:
        computer_choice = "S"
        
    computer_label_choice['text'] = ""
    user_label_choice['text'] = ""
    user_score = 0
    computer_score = 0
    result_label['text'] = "Choose [Rock, Paper, Scissors]"
    user_score_label['text'] = "PLAYER SCORE: 0"
    computer_score_label['text'] = "COMPUTER SCORE: 0"



heading_label = tkinter.Label(root, justify= tkinter.CENTER, text="Rock Paper Scissors", font=("calibri, 17"))
heading_label.pack()

computer_score_label = tkinter.Label(root,  text="COMPUTER SCORE: 0",font=("calibri",14))
computer_score_label.pack()

user_score_label = tkinter.Label(root,  text="PLAYER SCORE: 0",font=("calibri",14))
user_score_label.pack()

rock_button = tkinter.Button(root, text="Rock", command = rock)
rock_button.pack()

paper_button = tkinter.Button(root, text="Paper", command = paper)
paper_button.pack()

scissors_button = tkinter.Button(root, text="Scissors", command = scissors)
scissors_button.pack()

computer_label_choice = tkinter.Label(root, font="Courier", text="")
computer_label_choice.pack()

user_label_choice = tkinter.Label(root, font="Courier", text="")
user_label_choice.pack()

result_label = tkinter.Label(root, text="Choose [Rock, Paper, Scissors]")
result_label.pack()

reset_button = tkinter.Button(root, text="Reset", command = reset)
reset_button.pack()

root.mainloop()
