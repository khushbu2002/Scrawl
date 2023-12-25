from tkinter import *
import numpy as np
from PIL import ImageGrab
import network as net
# import cv2 
# import matplotlib.pyplot as plt


window = Tk()
window.title("Scrawl")
 
def MyProject():
    global l1
 
    widget = cv
    # Setting co-ordinates of canvas
    x = window.winfo_rootx() + widget.winfo_x()
    y = window.winfo_rooty() + widget.winfo_y()
    x1 = x + widget.winfo_width()
    y1 = y + widget.winfo_height()
 
    # Image is captured from canvas and is resized to (28 X 28) px
    img = ImageGrab.grab().crop((x+2, y+2, x1-2, y1-2)).resize((28, 28))
    img.save("captured_from_canvas.png")
    
    # Converting rgb to grayscale image
    img = img.convert('L')
    img.save("grayscale_captured_from_canvas.png")
    
    img = np.asarray(img)

    # Extracting pixel matrix of image and converting it to a vector of (1, 784)
    vec = np.zeros((784, 1))
    k = 0
    for i in range(28):
        for j in range(28):
            vec[k][0] = img[i][j]
            k += 1
 
    # Loading Thetas
    network=net.load("trained_data")

 
    # Calling function for prediction
    ans=np.argmax(network.feedforward(vec))
    print (ans)
    # Displaying the result
    l1.config(text="Digit = "+ str(ans))
 
 
lastx, lasty = None, None
 
 
# Clears the canvas
def clear_widget():
    global cv, l1
    cv.delete("all")
    l1.config(text="Digit = ?")
 
# Activate canvas
def event_activation(event):
    global lastx, lasty
    cv.bind('<B1-Motion>', draw_lines)
    lastx, lasty = event.x, event.y

 
# To draw on canvas
def draw_lines(event):
    global lastx, lasty
    x, y = event.x, event.y
    cv.create_line((lastx, lasty, x, y), width=30, fill='white', capstyle=ROUND, smooth=TRUE, splinesteps=12)
    lastx, lasty = x, y


bgLb=Label(window, bg="#ffbe7a",width=720,height=405)
bgLb.place(x=0, y=0)

l1 = Label(window, text="Digit = ?",bg="#ffbe7a",fg='black',font=('times',20))
l1.place(x=550, y=200)

# Label
titleL = Label(window, text="Canvas",bg="#ffbe7a",fg='black', font=('times', 20))
titleL.place(x=330, y=0)

# Button to clear canvas , font=('Algerian', 15)
b1 = Button(window, text="Clear Canvas", bg="black", fg="#ffbe7a", command=clear_widget)
b1.place(x=150, y=330)
 
# Button to predict digit drawn on canvas, font=('Algerian', 15)
b2 = Button(window, text="Prediction", bg="black", fg="#ffbe7a", command=MyProject)
b2.place(x=500, y=330)
 
# Setting properties of canvas
cv = Canvas(window, width=280, height=280, bg='black')
cv.place(x=220, y=30)
 
cv.bind('<Button-1>', event_activation)
window.geometry("720x405")
window.mainloop()