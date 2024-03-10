import tkinter as tk
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

# Create the main window
root = tk.Tk()
root.title("Random Word Generator")

# Configure grid columns and rows
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)  # Allow the second row to expand where the text widget is

# Create an entry widget
entry_label = tk.Label(root, text="Enter a number: ")
entry_label.grid(row=0, column=0, sticky="w")
entry = tk.Entry(root)
entry.insert(0, "100")  # Default value
entry.grid(row=0, column=1, sticky="ew")

# Create a run button
run_button = tk.Button(root, text="Run", command=on_run)
run_button.grid(row=0, column=2, sticky="ew")

# Create a text widget to display the output, make it expandable
output = tk.Text(root, state=tk.DISABLED)
output.grid(row=1, column=0, columnspan=3, sticky="nsew")  # Make it expandable in all directions

# Start the main event loop
root.mainloop()
