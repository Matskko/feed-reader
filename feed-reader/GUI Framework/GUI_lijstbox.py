import tkinter as tk

def on_select(event):
    selected_item = listbox.get(listbox.curselection())
    label.config(text=f"Geselecteerd: {selected_item}")

# Maak het hoofdvenster
root = tk.Tk()
root.title("Lijstbox voor selectie")

# Voeg een lijstbox toe
listbox = tk.Listbox(root, selectmode=tk.SINGLE)
listbox.pack(pady=10)

# Voeg items toe aan de lijstbox
for item in ["Optie 1", "Optie 2", "Optie 3", "Optie 4"]:
    listbox.insert(tk.END, item)

# Voeg een label toe voor resultaat
label = tk.Label(root, text="Selecteer een optie")
label.pack()

# Koppel een functie aan de selectiegebeurtenis
listbox.bind("<<ListboxSelect>>", on_select)

# Start de GUI-loop
root.mainloop()
