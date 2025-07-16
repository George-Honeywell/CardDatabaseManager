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
window.minsize("1200","400")
window.maxsize("1200","400")

tabControl = ttk.Notebook(window)
tabOne = ttk.Frame(tabControl)
tabTwo = ttk.Frame(tabControl)

tabControl.add(tabOne, text="Enter 'Creature' Card")
tabControl.add(tabTwo, text="Card Viewer")
tabControl.pack(expand=1, fill="both")

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

def refresh_card_viewer():
    card_viewer.delete(*card_viewer.get_children())
    for row in conn.execute('SELECT * FROM card_db'):
        card_viewer.insert("", 'end', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

# Card Labels
label_card_mana = ttk.Label(tabOne, text="Mana:").grid(row=0, column=0)
label_card_title = ttk.Label(tabOne, text="Title:").grid(row=1, column=0)
label_card_type = ttk.Label(tabOne, text="Type:").grid(row=2, column=0)
label_card_subtype = ttk.Label(tabOne, text="Subtype:").grid(row=3, column=0)
label_card_effect = ttk.Label(tabOne, text="Effect:").grid(row=4, column=0)
label_card_attack = ttk.Label(tabOne, text="Attack:").grid(row=5, column=0)
label_card_affinity = ttk.Label(tabOne, text="Affinity:").grid(row=6, column=0)
label_card_health = ttk.Label(tabOne, text="Health:").grid(row=7, column=0)

# Input Fields
entry_card_mana = ttk.Entry(tabOne)
entry_card_mana.grid(row=0, column=1, padx=5, pady=5)

entry_card_title = ttk.Entry(tabOne)
entry_card_title.grid(row=1, column=1, padx=5, pady=5)

entry_card_type = ttk.Entry(tabOne)
entry_card_type.grid(row=2, column=1, padx=5, pady=5)

entry_card_subtype = ttk.Entry(tabOne)
entry_card_subtype.grid(row=3, column=1, padx=5, pady=5)

entry_card_effect = ttk.Entry(tabOne)
entry_card_effect.grid(row=4, column=1, padx=5, pady=5)

entry_card_attack = ttk.Entry(tabOne)
entry_card_attack.grid(row=5, column=1, padx=5, pady=5)

entry_card_affinity = ttk.Entry(tabOne)
entry_card_affinity.grid(row=6, column=1, padx=5, pady=5)

entry_card_health = ttk.Entry(tabOne)
entry_card_health.grid(row=7, column=1, padx=5, pady=5)

button_add_card = ttk.Button(tabOne, text="Add Card", command=add_card).grid(row=8, columnspan=2)
button_update_card_viewer = ttk.Button(tabTwo, text="Reload Database", command=refresh_card_viewer).pack()

card_viewer = ttk.Treeview(tabTwo)
card_viewer["columns"] = ("1","2","3","4","5","6","7","8")

card_viewer.column("#0", width=0, stretch=False)
card_viewer.heading("#0", text='')

column_num = ('1', '2', '3', '4', '5', '6', '7', '8')
column_width = (1, 50, 50, 100, 100, 100, 200, 50, 50, 50)

for num, width in zip(column_num, column_width):
    card_viewer.column(num, width=width)

column_heading = ('ID', 'Mana', 'Title', 'Type', 'Subtype', 'Effect', 'Attack', 'Affinity', 'Health')

for num, heading in zip(column_num, column_heading):
    card_viewer.heading(num, text=heading)

card_viewer.place(width=1200, height=250, y=30)

window.mainloop()