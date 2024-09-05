import tkinter
from tkinter import *
from textblob import TextBlob

root = Tk()
root.title("Spelling Checker")
root.geometry("700x500")
root.config(background="#dae6f6")

# Function to check spelling
def check_spelling():
    word = enter_text.get()
    if not word:
        spell.config(text="Please enter a word!", fg="red")
    else:
        a = TextBlob(word)
        right = str(a.correct())
        spell.config(text="Correct text is: " + right, fg="#364971")

# Function to toggle dark mode
def toggle_mode():
    if root["bg"] == "#dae6f6":
        root.config(background="#333333")
        spell.config(bg="#333333", fg="#FFFFFF")
        heading.config(bg="#333333", fg="#FFFFFF")
    else:
        root.config(background="#dae6f6")
        spell.config(bg="#dae6f6", fg="#364971")
        heading.config(bg="#dae6f6", fg="#364971")

# Function to clear fields
def clear_fields():
    enter_text.delete(0, END)
    spell.config(text="")

# Heading Label
heading = Label(root, text="Spelling Checker", font=("Trebuchet MS", 30, "bold"), bg="#dae6f6", fg="#364971")
heading.pack(pady=(50, 10))

# Input Text Box
enter_text = Entry(root, justify="center", width=30, font=("poppins", 25), bg="white", fg="black", border=2)
enter_text.pack(pady=10)
enter_text.focus()

# Buttons
button = Button(root, text="Check", font=("arial", 20, "bold"), fg="white", bg="red", command=check_spelling)
button.pack(pady=10)

clear_button = Button(root, text="Clear", font=("arial", 15), fg="white", bg="blue", command=clear_fields)
clear_button.pack(pady=10)

toggle_button = Button(root, text="Dark Mode", font=("arial", 15), fg="white", bg="blue", command=toggle_mode)
toggle_button.pack(pady=20)

# Result Label
spell = Label(root, font=("poppins", 20), bg="#dae6f6", fg="#364971")
spell.pack(pady=20)

root.mainloop()
