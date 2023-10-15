# import libraries
from tkinter import *
import random

# Colors and timing
colors = ['Red','Blue','Green','Pink','Yellow','Orange','White','Purple','Brown']
score = 0
time_left = 30
timing_start= False

# Start the game
def start():
    global timing_start
    btn.config(text="NEXT")
    if timing_start == False:
        countdown()
        timing_start = True    
    nextColor()

# Timing table with countdown system
def countdown():
    global time_left
    
    if time_left > 0:
        time_left -= 1
        timeLabel.config(text = "Time left: " + str(time_left))
        timeLabel.after(1000, countdown)    

# Color choice system
def nextColor():
    global score
    global time_left
 
    if time_left > 0:
 
        if answer.get().lower() == colors[1].lower():
             
            score += 1
        answer.delete(0, END)
        random.shuffle(colors)
         
        label.config(fg = str(colors[1]), text = str(colors[0]),font="Britannic 30")
         
        score_label.config(text = "Score: " + str(score))
        


# lets start making the environment 

win = Tk()
win.title("Color game")
win.geometry("375x280")
win.configure(bg="Black")
photo = PhotoImage(file="BYR_color_wheel.png")
win.iconphoto(False, photo)
win.resizable(0,0)

label = Label(win,text="Welcome to color game!",fg="Red",bg="black",font=("Britannic Bold",19))
label.pack()

timeLabel = Label(win, text = "Time left: " + str(time_left), 
                    font = ('Arial Rounded MT Bold', 17),fg="yellow",bg="black")
            
timeLabel.pack(pady=5)

answer = Entry(win,width=10,justify="center",font=('Arial 24'))
answer.pack(pady=20)

btn = Button(win,text="START",width=10,font=('Arial 15'),command=start)
btn.pack()

score_label = Label(win,text="Score: 0",font="Arial 15",fg="White",bg="black")
score_label.pack(pady=20)

win.mainloop()