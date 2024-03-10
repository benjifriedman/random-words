import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
import random

# Function to generate random words
def generate_words(n, length_min=3, length_max=7):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    words = []
    for _ in range(n):
        word = ""
        length = random.randint(length_min, length_max)
        for _ in range(length // 2):
            word += random.choice(consonants) + random.choice(vowels)
        if length % 2:  # If length is odd, add a final consonant
            word += random.choice(consonants)
        words.append(word)
    return " ".join(words)

# Function called when the "Run" button is clicked
def on_run():
    try:
        num = int(entry.get())
    except ValueError:
        num = 100  # Default to 100 if the input is not a valid number
    words = generate_words(num)
    output.config(state=tk.NORMAL)
    output.delete('1.0', tk.END)
    output.insert(tk.END, words)
    output.config(state=tk.DISABLED)

# Function to increase font size
def increase_font():
    font_size = font.actual("size") + 2
    font.config(size=font_size)

# Function to decrease font size
def decrease_font():
    font_size = font.actual("size") - 2
    if font_size > 8:  # Prevent the font size from becoming too small
        font.config(size=font_size)

# Right-click context menu action
def copy_text(event=None):
    output.event_generate("<<Copy>>")

# Create the right-click context menu
def show_context_menu(event):
    context_menu.tk_popup(event.x_root, event.y_root)

# Create the main window
root = tk.Tk()
root.title("Random Word Generator")

# Configure grid columns and rows
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

# Define a font for the Text widget
font = tkFont.Font(family="Helvetica", size=12)

# Create an entry widget
entry_label = tk.Label(root, text="Enter a number: ")
entry_label.grid(row=0, column=0, sticky="w")
entry = tk.Entry(root)
entry.insert(0, "100")  # Default value
entry.grid(row=0, column=1, sticky="ew")

# Create a run button
run_button = tk.Button(root, text="Run", command=on_run)
run_button.grid(row=0, column=2, sticky="ew")

# Create increase and decrease font size buttons
increase_font_button = tk.Button(root, text="A+", command=increase_font)
increase_font_button.grid(row=0, column=3, sticky="ew")

decrease_font_button = tk.Button(root, text="A-", command=decrease_font)
decrease_font_button.grid(row=0, column=4, sticky="ew")

# Create a text widget to display the output, make it expandable
output = tk.Text(root, state=tk.DISABLED, font=font)
output.grid(row=1, column=0, columnspan=5, sticky="nsew")  # Make it expandable in all directions

# Text widget setup with the right-click event binding
output = tk.Text(root, state=tk.NORMAL, font=font)
output.grid(row=1, column=0, columnspan=5, sticky="nsew")
output.bind("<Button-2>", show_context_menu)

# Create a Menu for the right-click context
context_menu = tk.Menu(root, tearoff=0)
context_menu.add_command(label="Copy", command=copy_text)

# Start the main event loop
root.mainloop()
