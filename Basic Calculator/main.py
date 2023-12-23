from tkinter import *

root = Tk()
root.title("Basic Calculator")
root.geometry("550x600")

result = ""

def display(value):
    global result
    result += value
    result_label.config(text=result)
    
def clear():
    global result
    result = ""
    result_label.config(text=result)
    
def calculate():
    global result
    output = ""
    if result != "":
        try:
            output = eval(result)
        except:
            output = "Invalid!! Please Enter again."
            result = ""
            
    result_label.config(text=output)

#defining the labels and buttons
heading_label = Label(root, text="Basic Calculator", font =("arial", 30, "bold"))
heading_label.pack()

result_label = Label(root, width=25, height=2, text= "", font=("calibri, 30"), bg = "#850101")
result_label.pack()     

Button(root, text="C", width=5, height=1, font =("calibri", 30, "bold"), bd=1, fg="#fff", bg = "#850101", command = lambda: clear()).place(x=10, y=200) 
Button(root, text="*", width=5, height=1, font =("calibri", 30, "bold"), bd=1, fg="#fff", bg = "#000000", command = lambda: display("*")).place(x=140, y=200)    
Button(root, text="/", width=5, height=1, font =("calibri", 30, "bold"), bd=1, fg="#fff", bg = "#000000", command = lambda: display("/")).place(x=270, y=200)    
Button(root, text="%", width=5, height=1, font =("calibri", 30, "bold"), bd=1, fg="#fff", bg = "#000000", command = lambda: display("%")).place(x=400, y=200)    


Button(root, text="7", width=5, height=1, font =("calibri", 30, "bold"), bd=1, fg="#fff", bg = "#000000", command = lambda: display("7")).place(x=10, y=275) 
Button(root, text="8", width=5, height=1, font =("calibri", 30, "bold"), bd=1, fg="#fff", bg = "#000000", command = lambda: display("8")).place(x=140, y=275)    
Button(root, text="9", width=5, height=1, font =("calibri", 30, "bold"), bd=1, fg="#fff", bg = "#000000", command = lambda: display("9")).place(x=270, y=275)    
Button(root, text="+", width=5, height=1, font =("calibri", 30, "bold"), bd=1, fg="#fff", bg = "#000000", command = lambda: display("+")).place(x=400, y=275)    


Button(root, text="4", width=5, height=1, font =("calibri", 30, "bold"), bd=1, fg="#fff", bg = "#000000", command = lambda: display("4")).place(x=10, y=350) 
Button(root, text="5", width=5, height=1, font =("calibri", 30, "bold"), bd=1, fg="#fff", bg = "#000000", command = lambda: display("5")).place(x=140, y=350)    
Button(root, text="6", width=5, height=1, font =("calibri", 30, "bold"), bd=1, fg="#fff", bg = "#000000", command = lambda: display("6")).place(x=270, y=350)    
Button(root, text="-", width=5, height=1, font =("calibri", 30, "bold"), bd=1, fg="#fff", bg = "#000000", command = lambda: display("-")).place(x=400, y=350)    

Button(root, text="1", width=5, height=1, font =("calibri", 30, "bold"), bd=1, fg="#fff", bg = "#000000", command = lambda: display("1")).place(x=10, y=425)    
Button(root, text="2", width=5, height=1, font =("calibri", 30, "bold"), bd=1, fg="#fff", bg = "#000000", command = lambda: display("2")).place(x=140, y=425)    
Button(root, text="3", width=5, height=1, font =("calibri", 30, "bold"), bd=1, fg="#fff", bg = "#000000", command = lambda: display("3")).place(x=270, y=425)    
Button(root, text="0", width=5, height=1, font =("calibri", 30, "bold"), bd=1, fg="#fff", bg = "#000000", command = lambda: display("0")).place(x=10, y=500)

Button(root, text="00", width=5, height=1, font =("calibri", 30, "bold"), bd=1, fg="#fff", bg = "#000000", command = lambda: display("00")).place(x=140, y=500)    
Button(root, text=".", width=5, height=1, font =("calibri", 30, "bold"), bd=1, fg="#fff", bg = "#000000", command = lambda: display(".")).place(x=270, y=500)    
Button(root, text="=", width=5, height=2, font =("calibri", 30, "bold"), bd=1, fg="#fff", bg = "#008000", command = lambda: calculate()).place(x=400, y=455)    

root.mainloop()
