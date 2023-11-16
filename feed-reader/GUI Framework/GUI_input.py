import tkinter as tk

def on_submit():
    name = entry.get()
    label_result.config(text=f"Hallo, {name}!")

# Maak het hoofdvenster
root = tk.Tk()
root.title("Invoerveld voor naam")

# Voeg een invoerveld toe
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Voeg een knop toe
submit_button = tk.Button(root, text="Indienen", command=on_submit)
submit_button.pack()

# Voeg een label toe voor resultaat
label_result = tk.Label(root, text="")
label_result.pack(pady=10)

# Start de GUI-loop
root.mainloop()
