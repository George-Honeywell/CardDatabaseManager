from tkinter import Tk, ttk, messagebox
import json
from pathlib import Path

window = Tk()
window.title("PRIMEVAL: Battles - Card Manager")

# Card Labels
label_card_mana = ttk.Label(window, text="Mana:")
label_card_mana.grid(row=0, column=0)

label_card_title = ttk.Label(window, text="Title:")
label_card_title.grid(row=1, column=0)

label_card_type = ttk.Label(window, text="Type:")
label_card_type.grid(row=2, column=0)

label_card_subtype = ttk.Label(window, text="Subtype:")
label_card_subtype.grid(row=3, column=0)

label_card_effect = ttk.Label(window, text="Effect:")
label_card_effect.grid(row=4, column=0)

label_card_attack = ttk.Label(window, text="Attack:")
label_card_attack.grid(row=5, column=0)

label_card_affinity = ttk.Label(window, text="Affinity:")
label_card_affinity.grid(row=6, column=0)

label_card_health = ttk.Label(window, text="Health:")
label_card_health.grid(row=7, column=0)

# Input Fields
entry_card_mana = ttk.Entry(window)
entry_card_mana.grid(row=0, column=1, padx=5, pady=5)
entry_card_title = ttk.Entry(window)
entry_card_title.grid(row=1, column=1, padx=5, pady=5)
entry_card_type = ttk.Entry(window)
entry_card_type.grid(row=2, column=1, padx=5, pady=5)
entry_card_subtype = ttk.Entry(window)
entry_card_subtype.grid(row=3, column=1, padx=5, pady=5)
entry_card_effect = ttk.Entry(window)
entry_card_effect.grid(row=4, column=1, padx=5, pady=5)
entry_card_attack = ttk.Entry(window)
entry_card_attack.grid(row=5, column=1, padx=5, pady=5)
entry_card_affinity = ttk.Entry(window)
entry_card_affinity.grid(row=6, column=1, padx=5, pady=5)
entry_card_health = ttk.Entry(window)
entry_card_health.grid(row=7, column=1, padx=5, pady=5)

window.mainloop()