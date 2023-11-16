import tkinter as tk

def on_checkbox_toggle():
    if checkbox_var.get():
        label.config(text="Checkbox is ingeschakeld")
    else:
        label.config(text="Checkbox is uitgeschakeld")

# Maak het hoofdvenster
root = tk.Tk()
root.title("Checkbox voor status")

# Maak een variabele voor de checkbox
checkbox_var = tk.BooleanVar()

# Voeg een checkbox toe
checkbox = tk.Checkbutton(root, text="Inschakelen", variable=checkbox_var, command=on_checkbox_toggle)
checkbox.pack(pady=10)

# Voeg een label toe voor resultaat
label = tk.Label(root, text="Checkbox is uitgeschakeld")
label.pack()

# Start de GUI-loop
root.mainloop()
