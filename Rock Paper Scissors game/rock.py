import tkinter
import random
from PIL import Image, ImageTk

root = tkinter.Tk()
root.title = "Rock, Paper Scissors game"
root.geometry("700x700")

user_score = 0
computer_score = 0

random_num = random.randint(1, 3)
if random_num == 1:
    computer_choice = "R"
elif random_num == 2:
    computer_choice = "P"
elif random_num == 3:
    computer_choice = "S"


img_pillow = Image.open("D:\CODSOFT\Rock Paper Scissors game\images\com_scissor.png")
rock_img = ImageTk.PhotoImage(img_pillow)

rock_image_label = rock_img
    
# Create a label to display the image
# rock_image_label.config(image=rock_img)
# rock_image_label.pack()


paper_img = tkinter.PhotoImage(file ="D:\CODSOFT\Rock Paper Scissors game\images\com_paper.png")
scissors_img = tkinter.PhotoImage(file="D:\CODSOFT\Rock Paper Scissors game\images\com_scissor.png")
# rock_img = """
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)"""

# paper_img = """

#      _______
# ---'    ____)_____
#            _______)
#           _______)
#          _______)
# ---.__________)"""

# scissors_img = """
#     _______
# ---'   ____)____
#           ______)   
#        __________)   
#       (____)
# ---.__(___)"""


# Create functions
def rock():
    global user_score, computer_score
    user_choice_label['text'] = rock_img
    
    # Deal with the choices
    if computer_choice == "R":
        result_label['text'] = "TIE"
        computer_choice_label['text'] = rock_img
        user_score = user_score + 1
        computer_score = computer_score + 1
        user_score_label.config(text="player : "+str(user_score))
        computer_score_label.config(text="COMPUTER : "+ str(computer_score))
                
    elif computer_choice == "P":
        result_label['text'] = "Computer wins!"
        computer_choice_label['text'] = paper_img
        computer_score = computer_score + 2
        computer_score_label.config(text="COMPUTER : "+ str(computer_score))
        
    elif computer_choice == "S":
        result_label['text'] = "Player wins!"
        user_score = user_score + 2
        computer_choice_label['text'] = scissors_img
        user_score_label.config(text="player : "+str(user_score))

    
def paper():
    global user_score, computer_score
    user_choice_label['text'] = paper_img
    
    # Deal with the choices
    if computer_choice == "P":
        result_label['text'] = "TIE"
        computer_choice_label['text'] = paper_img
        computer_score =computer_score +1
        user_score = user_score + 1
        user_score_label.config(text="player : "+str(user_score))
        computer_score_label.config(text="computer : "+str(computer_score))

    elif computer_choice == "S":
        result_label['text'] = "Computer wins!"
        computer_choice_label['text'] = scissors_img
        computer_score = computer_score + 1
        computer_score_label.config(text="computer : "+str(computer_score))

    elif computer_choice == "R":
        result_label['text'] = "Player wins!"
        computer_choice_label['text'] = rock_img
        user_score = user_score +1
        user_score_label.config(text="player : "+str(user_score))

    
def scissors():
    global user_score, computer_score
    user_choice_label['text'] = scissors_img
    
    # Deal with the choices
    if computer_choice == "S":
        result_label['text'] = "TIE"
        computer_choice_label['text'] = scissors_img
        user_score = user_score +1
        computer_score =computer_score +1
        user_score_label.config(text="player : "+str(user_score))
        computer_choice_label.config(text="player : "+str(computer_score))

    elif computer_choice == "R":
        result_label['text'] = "Computer wins!"
        computer_choice_label['text'] = rock_img
        computer_score = computer_score+1
        computer_score_label.config(text="player : "+str(computer_score))

    elif computer_choice == "P":
        result_label['text'] = "Player wins!"
        computer_choice_label['text'] = paper_img
        user_score = user_score + 1
        user_score_label.config(text="player : "+str(user_score))

    
def reset():
    global computer_choice
    random_num = random.randint(1, 3)
    if random_num == 1:
        computer_choice = "R"
    elif random_num == 2:
        computer_choice = "P"
    elif random_num == 3:
        computer_choice = "S"
        
    computer_choice_label['text'] = ""
    user_choice_label['text'] = ""
    result_label['text'] = "Choose..."


heading_label = tkinter.Label(root, justify= tkinter.CENTER, text="Rock Paper Scissors", font=("calibri, 17"))
heading_label.pack()

rock_image_label = tkinter.Label(root)
rock_image_label.pack()



computer_score_label = tkinter.Label(root,  text="Computer Score : 0",font=("calibri",14))
computer_score_label.pack()

user_score_label = tkinter.Label(root, text="Player Score : 0",font=("calibri",14),)
user_score_label.pack()

# user_score_label.grid(row=2)

rock_btn = tkinter.Button(root, text="Rock", command= rock)
rock_btn.pack()

button_paper = tkinter.Button(root, text="Paper", command= paper)
button_paper.pack()

scissors_btn = tkinter.Button(root, text="Scissors", command= scissors)
scissors_btn.pack()

computer_choice_label = tkinter.Label(root, justify=tkinter.LEFT, font="SanSerif", text="")
computer_choice_label.pack()

user_choice_label = tkinter.Label(root, justify=tkinter.LEFT, font="Courier", text="")
user_choice_label.pack()

result_label = tkinter.Label(root, text="Choose...")
result_label.pack()

button_reset = tkinter.Button(root, text="Reset", command=reset)
button_reset.pack()


root.mainloop()