from tkinter import Tk, ttk, messagebox

window = Tk()
window.title("PRIMEVAL: Battles - Card Manager")

# Card Labels
label_card_mana = ttk.Label(window, text="Mana:").grid(row=0, column=0)
label_card_title = ttk.Label(window, text="Title:").grid(row=1, column=0)
label_card_type = ttk.Label(window, text="Type:").grid(row=2, column=0)
label_card_subtype = ttk.Label(window, text="Subtype:").grid(row=3, column=0)
label_card_effect = ttk.Label(window, text="Effect:").grid(row=4, column=0)
label_card_attack = ttk.Label(window, text="Attack:").grid(row=5, column=0)
label_card_affinity = ttk.Label(window, text="Affinity:").grid(row=6, column=0)
label_card_health = ttk.Label(window, text="Health:").grid(row=7, column=0)

# Input Fields
entry_card_mana = ttk.Entry(window).grid(row=0, column=1, padx=5, pady=5)
entry_card_title = ttk.Entry(window).grid(row=1, column=1, padx=5, pady=5)
entry_card_type = ttk.Entry(window).grid(row=2, column=1, padx=5, pady=5)
entry_card_subtype = ttk.Entry(window).grid(row=3, column=1, padx=5, pady=5)
entry_card_effect = ttk.Entry(window).grid(row=4, column=1, padx=5, pady=5)
entry_card_attack = ttk.Entry(window).grid(row=5, column=1, padx=5, pady=5)
entry_card_affinity = ttk.Entry(window).grid(row=6, column=1, padx=5, pady=5)
entry_card_health = ttk.Entry(window).grid(row=7, column=1, padx=5, pady=5)

window.mainloop()