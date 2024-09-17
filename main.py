from new import Cilveks
import tkinter as tk
from tkinter import ttk

root= tk.Tk()
root.title("Cilvēku ražotne")
root.geometry("300x300")

frame = ttk.Frame(root)
options = {"padx": 5, "pady": 5}

# Cilvēku saraksts
visi_cilveki = []


# Ekrāns

# Vārds label
vards_label = ttk.Label(frame, text='Vārds')
vards_label.grid(column=0, row=0, sticky='w', **options)

vecums_label = ttk.Label(frame, text='Dzimums')
vecums_label.grid(column=0, row=1, sticky='w', **options)

dzimums_label = ttk.Label(frame, text='Vecums')
dzimums_label.grid(column=0, row=2, sticky='w', **options)



# vards entry
vards = tk.StringVar()
vards = ttk.Entry(frame, textvariable=vards)
vards.grid(column=1, row=0, **options)
vards.focus()

# dzimums entry
dzimums = tk.StringVar()
dzimums_entry = ttk.Entry(frame, textvariable=dzimums)
dzimums_entry.grid(column=1, row=1, **options)

# vecums entry
vecums = tk.IntVar()
vecums_entry = ttk.Entry(frame, textvariable=vecums)
vecums_entry.grid(column=1, row=2, **options)

# ražošanas button
def convert_button_clicked():
    cilveka_vards = vards.get()
    cilveka_dzimums = dzimums.get()
    cilveka_vecums = vecums.get()
    visi_cilveki.append(Cilveks(cilveka_vards, cilveka_dzimums, cilveka_vecums))
    result_label.config(text=visi_cilveki[-1].pastastit_par_sevi())


razot_button = ttk.Button(frame, text='Ražot')
razot_button.grid(column=2, row=0, sticky='W', **options)
razot_button.configure(command=convert_button_clicked)

# result label
result_label = ttk.Label(frame)
result_label.grid(row=3, columnspan=3, **options)

# add padding to the frame and show it
frame.grid(padx=10, pady=10)


# start the app
root.mainloop()