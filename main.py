BACKGROUND_COLOR = "#B1DDC6"

import pandas
from tkinter import *
from tkinter import messagebox
import random

current_card = {}
flip_timer = 3000

try:
    data = pandas.read_csv("./data/french_words.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words_original.csv")
    word_list = original_data.to_dict(orient="records")
else:
    word_list = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(word_list)
    canvas.create_image(400, 263, image=card_front_img)
    canvas.grid(row=0, column=0, columnspan=2)

    canvas.create_text(400, 150, text="French", fill="black", font=("Ariel", 50, "italic"))
    canvas.create_text(400, 263, text=current_card["French"], fill="black", font=("Ariel", 60, "bold"))

    flip_timer = canvas.after(3000, flip)

def flip():
    canvas.create_image(400, 263, image=card_back_img)
    canvas.create_text(400, 150, text="English", fill="white", font=("Ariel", 50, "italic"))
    canvas.create_text(400, 263, text=current_card["English"], fill="white", font=("Ariel", 60, "bold"))

def is_known():
    word_list.remove(current_card)
    data = pandas.DataFrame(word_list)
    data.to_csv("./data/french_words.csv", index=False)

    next_card()

#------------------------------------------------------------#

window = Tk()
window.title("Flash Cards: French")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)

card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)





next_card()



window.mainloop()