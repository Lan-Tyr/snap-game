import random
import time
from tkinter import Tk, Canvas, HIDDEN, NORMAL # HIDDEN state will hide the shapes until the program reveals them by switching to the NORMAL state.

# Note that a "global" variable exists outside a function and can be used in any part of the program; a "local" variable exists only inside a function. In order to
# update the value of a global variable through a funciton, we need to use the keyword "global" before the variable's name. This way changes to a global variable
# will be seen throughout the whole program.

def next_shape():
    global shape
    global previous_color
    global current_color
    
    previous_color = current_color

    c.delete(shape) # Deletes the current shape so that the new shape isn't appearing overtop of it.
    if len(shapes) > 0: # Checks to see if there are any shapes left in the list.
        shape = shapes.pop() # If there are shapes left, a new shape is pulled out.
        c.itemconfigure(shape, state=NORMAL) # Changes the state of the shape to NORMAL so that it is visible.
        current_color = c.itemcget(shape, "fill") # Assigns current_color to the new shape.
        root.after(1000, next_shape) # Waits 1 second before showing the next shape.
    else:
        c.unbind("q")
        c.unbind("p")
        if player1_score > player2_score:
            c.create_text(200, 200, text="Winner: Player 1")
        elif player2_score > player1_score:
            c.create_text(200, 200, text="Winner: Player 2")
        else:
            c.create_text(200, 200, text="Draw")
        c.pack()

def snap(event):
    global shape
    global player1_score
    global player2_score
    valid = False

    c.delete(shape)

    if previous_color == current_color:
        valid = True

    if valid:
        if event.char == "q":
            player1_score = player1_score + 1
        else:
            player2_score = player2_score + 1
        shape = c.create_text(200, 200, text="SNAP! You score 1 point!")
    else:
        if event.char == "q":
            player1_score = player1_score - 1
        else:
            player2_score = player2_score - 1
        shape = c.create_text(200, 200, text="WRONG! You lose 1 point!")
    c.pack()
    root.update_idletasks()
    time.sleep(1) # Waits 1 second while the players read the message.

root = Tk()
root.title("Snap")
c = Canvas(root, width=400, height=400)

shapes = [] # Empty list to store the shapes we will create below.

circle = c.create_oval(35, 20, 365, 350, outline="black", fill="black", state=HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20, 365, 350, outline="red", fill="red", state=HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20, 365, 350, outline="green", fill="green", state=HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20, 365, 350, outline="blue", fill="blue", state=HIDDEN)
shapes.append(circle)

rectangle = c.create_rectangle(35, 100, 365, 270, outline="black", fill="black", state=HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35, 100, 365, 270, outline="red", fill="red", state=HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35, 100, 365, 270, outline="green", fill="green", state=HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35, 100, 365, 270, outline="blue", fill="blue", state=HIDDEN)
shapes.append(rectangle)

square = c.create_rectangle(35, 20, 365, 350, outline="black", fill="black", state=HIDDEN)
shapes.append(square)
square = c.create_rectangle(35, 20, 365, 350, outline="red", fill="red", state=HIDDEN)
shapes.append(square)
square = c.create_rectangle(35, 20, 365, 350, outline="green", fill="green", state=HIDDEN)
shapes.append(square)
square = c.create_rectangle(35, 20, 365, 350, outline="blue", fill="blue", state=HIDDEN)
shapes.append(square)

c.pack()
random.shuffle(shapes) # Shuffles all the shapes randomly in the "shapes" list.

shape = None # Initial state for the shapes is essentially "0" indicating that no shapes are active yet.
previous_color = "" # Initially empty values that will update with the previous and current colors of the shapes.
current_color = ""
player1_score = 0 # Player scores start at "0" and update as they gain points.
player2_score = 0

root.after(3000, next_shape) # The program waits 3 seconds before calling a new shape.
c.bind("q", snap) # Makes the "q" key a valid input for the program.
c.bind("p", snap) # Makes the "p" key a valid input for the program.
c.focus_set() # Tells the key presses to go to the canvas so that it can react to them.

root.mainloop()