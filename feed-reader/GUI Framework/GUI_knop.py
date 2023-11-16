import tkinter as tk

def on_button_click():
    label.config(text="Hello, GUI!")

# Maak het hoofdvenster
root = tk.Tk()
root.title("Eenvoudige GUI")

# Voeg een label toe
label = tk.Label(root, text="Druk op de knop om een bericht te tonen")
label.pack(pady=10)

# Voeg een knop toe
button = tk.Button(root, text="Druk hier", command=on_button_click)
button.pack()

# Start de GUI-loop
root.mainloop()
