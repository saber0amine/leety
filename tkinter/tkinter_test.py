import tkinter as tk 



# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Mon Application Tkinter")
fenetre.geometry("900x600")  # Définir la taille de la fenêtre

entry = tk.Entry(fenetre)
entry.pack()
print(entry.get())

cadre = tk.Frame(fenetre)
# Ajout de widgets (par exemple, un bouton)
bouton = tk.Button(fenetre, text="Cliquez-moi !", command=print(f"{entry.get()}") )
cadre.pack()
bouton.pack(pady=20) # Ajouter le bouton à la fenêtre

canvas = tk.Canvas(fenetre, width=200, height=100)
canvas.pack()

canvas.create_rectangle(50, 25, 150, 75, fill="blue")

checkbutton = tk.Checkbutton(fenetre , text="choos me " , command=lambda: print("Hello Saber from checkbutton !"))
checkbutton.pack()


label = tk.Label(fenetre ,  text="Ceci est une etiquete")
label.pack()

radio_button1 = tk.Radiobutton(fenetre, text="Option 1" , command=lambda: print("Hello Saber from radio 1 !"))
radio_button2 = tk.Radiobutton(fenetre, text="Option 2")
radio_button1.pack()
radio_button2.pack()

listbox = tk.Listbox(fenetre)
listbox.insert(1, "Option 1")
listbox.insert(4, "Option 2")
listbox.pack()

menubutton = tk.Menubutton(fenetre , text="Menu")
menu = tk.Menu(menubutton)
menubutton.config(menu=menu)
menu.add_command(label="Option 1")
menu.add_command(label="Option 2")
menubutton.pack()

message =  tk.Message(fenetre ,  text="ceci est un message")
message.pack()
 
paned_window = tk.PanedWindow(fenetre, orient=tk.HORIZONTAL)
paned_window.pack()
cadre1 = tk.Frame(paned_window, bd=4, relief=tk.RAISED)
cadre2 = tk.Frame(paned_window, bd=4, relief=tk.RAISED)
paned_window.add(cadre1)
paned_window.add(cadre2)

bouton1 = tk.Button(cadre1, text="Volet 1")
bouton2 = tk.Button(cadre2, text="Volet 2")
bouton1.pack()
bouton2.pack()



def on_scale_change(value):
      print(f"Valeur sélectionnée : {value}")





def open_new_window():
      new_window = tk.Toplevel(fenetre)
      label = tk.Label(new_window, text="Nouvelle fenêtre !")
      label.pack()
      scale = tk.Scale(new_window, from_=0, to=100, orient=tk.HORIZONTAL, command=on_scale_change)
      scale.pack()
      spinbox = tk.Spinbox(new_window, from_=1, to=10)
      spinbox.pack()

bouton = tk.Button(fenetre, text="Ouvrir une nouvelle fenêtre", command=open_new_window)
bouton.pack()
# Lancer la boucle principale de l'application
fenetre.mainloop()