from tkinter import *
from tkinter import ttk
from connexion  import connexion
from tkinter import Canvas
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np


class interface(Frame) : 
    def __init__(self , fenetre ):
        Frame.__init__( self,fenetre )
        self.pack(fill=BOTH)
        self.db = connexion()
        
        req = "SELECT libelle from Sondages "
        self.db.cursor.execute(req)
        result = self.db.cursor.fetchall()
        print(result[0][0])
        self.libelle_selected =StringVar()
        
        cbLibelS = ttk.Combobox(self , values=result[0][0] , textvariable=self.libelle_selected )
        cbLibelS.bind("<<ComboboxSelected>>" , self.update_sujet)
        sondage_label = Label(self , text="Libelle")
        sondage_label.grid(row=0 , column= 0)
        cbLibelS.grid(row=0 , column= 1)
        
        
        self.sujet_selected = StringVar()
        self.cbIntitulS = ttk.Combobox(self , textvariable= self.sujet_selected)
        self.cbIntitulS.bind("<<ComboboxSelected>>" , self.update_tree_view)
        sujet_label = Label(self , text="Intutille sujet")
        sujet_label.grid(row=1 , column= 0)
        self.cbIntitulS.grid(row=1 , column= 1)
        
        
        frame1 = Frame(self)
        frame1.grid(row=2 , column= 1)

        votesFrame = LabelFrame(frame1 , text="info Votes")
        votesFrame.pack(side="left")
        self.treeVotes =ttk.Treeview(votesFrame , columns=(1,2) ,show="headings" , height=8)
        self.treeVotes.heading(1 , text="Nom et Prenom")
        self.treeVotes.heading(2 , text="Vote")
        self.treeVotes.pack(side='left')


        frame2 = Frame(self)
        frame2.grid(row=2 , column= 2)


        self.fig , self.ax = plt.subplots()
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=frame2)
        self.canvas.get_tk_widget().pack()

        
        
    def update_sujet(self , event ) : 
        v_libelle_selected  = self.libelle_selected.get()
        
        req = f"SELECT intitule FROM Sujets s inner join Sondages sg on s.numSo = sg.numSo WHERE sg.libelle= '{v_libelle_selected}' "
        
        self.db.cursor.execute(req)
        result = self.db.cursor.fetchall()
        self.cbIntitulS.config(values=result)
             
   
    def update_tree_view(self , event) : 
       v_sujet_selected = self.sujet_selected.get()
       req = f"SELECT nomPrenom , choixVote FROM Votes v inner join Participants p on v.numP = p.numP WHERE v.numSu = (SELECT numSu from Sujets s where s.intitule = '{v_sujet_selected}' ) "
       self.db.cursor.execute(req)
       result = self.db.cursor.fetchall()
       self.treeVotes.delete(*self.treeVotes.get_children())
       for items in result :
           self.treeVotes.insert('','end', values=(items[0] , items[1]))
           
       vote  = ["Oui" , "Non"]
       req2 =f"SELECT count(*) from Votes v inner join Sujets s on v.numSu = s.numSu  WHERE s.intitule= '{v_sujet_selected}' AND choixVote ='{vote[0]}' GROUP BY choixVote like 'Oui' "
       req3 =f"SELECT count(*) from Votes v inner join Sujets s on v.numSu = s.numSu  WHERE s.intitule= '{v_sujet_selected}' AND choixVote ='{vote[1]}' GROUP BY choixVote like 'Oui' "

       self.db.cursor.execute(req2)
       result2 = self.db.cursor.fetchall()
       self.db.cursor.execute(req3)
       result3 = self.db.cursor.fetchall()
       y= [result2[0][0] , result3[0][0] ]
       
       self.ax.clear()
       self.ax.bar(vote , y)

       self.ax.set_xlabel('Votes')
       self.ax.set_ylabel('Nombre de votes')       

       self.canvas.draw()
           
       
        
        
fenetre = Tk()
fenetre.geometry("800x700")
interf = interface(fenetre)
interf.mainloop()