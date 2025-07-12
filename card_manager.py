from tkinter import Tk, ttk, messagebox
import sqlite3

conn = sqlite3.connect('card_database.db', isolation_level=None)
conn.execute('CREATE TABLE IF NOT EXISTS card_db (_id INT NOT NULL, ' \
'card_title TEXT,' \
'card_mana TEXT,' \
'card_type TEXT,' \
'card_subtype TEXT,' \
'card_effect TEXT,' \
'card_attack INT,' \
'card_affinity TEXT,' \
'card_health INT ) STRICT')

window = Tk()
window.title("PRIMEVAL: Battles - Card Manager")
window.minsize("400","400")
window.maxsize("400","400")

card_id = 0
def add_card():
    global card_id
    conn.execute('INSERT INTO card_db VALUES (?,?,?,?,?,?,?,?,?)', 
                 [card_id,
                  entry_card_mana.get(),
                  entry_card_title.get(),
                  entry_card_type.get(),
                  entry_card_subtype.get(),
                  entry_card_effect.get(),
                  entry_card_attack.get(),
                  entry_card_affinity.get(),
                  entry_card_health.get()])
    card_id += 1

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

button_add_card = ttk.Button(window, text="Add Card", command=add_card).grid(row=8, columnspan=2)

window.mainloop()