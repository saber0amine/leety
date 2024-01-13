from  tkinter import ttk
from tkinter import *
from connexion import connexion 
from tkinter import Canvas
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np



class interface(Frame) : 
    def __init__(self, fenetre ,   **kwargs):
        Frame.__init__(self, fenetre )
        self.pack() 
        
        self.db = connexion()
        req = "SELECT `Code catégorie` from catégories"
        self.db.cursor.execute(req)
        result = self.db.cursor.fetchall()
        
        
        self.selcted_code = IntVar()
        self.comboBox = ttk.Combobox(self ,values=result , textvariable=self.selcted_code)
       
        self.comboBox.current(0)     
        self.comboBox.pack()
        
        self.comboBox.bind("<<ComboboxSelected>> "  , self.update_tree)
        
        
        frame1 = Frame(self)
        frame1.pack()
        
        self.treeview_widget =ttk.Treeview(frame1 , columns=(1,2,3 , 4) , height=5, show="headings")
        self.treeview_widget.grid(row=0 , column=1)
        self.treeview_widget.heading(1 , text="Nom de Produit") ; self.treeview_widget.heading(2 , text="Quantitè") , self.treeview_widget.heading(3 , text="Prix") ;  self.treeview_widget.heading(4 , text="Nom de catégorie")
        
        
        # frame2 = Frame(self)
        # frame2.pack()
        # arr = np.array(np.arange(15)).reshape(3,5)
        # graphe = plt.plot(arr)
        # graphe.pack()
        
        frame2 = Frame(self)
        frame2.pack()

        self.fig , self.ax = plt.subplots()
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=frame2)
        self.canvas.get_tk_widget().pack()

        

 

    def update_tree(self , event) -> None : 
        for items in self.treeview_widget.get_children() : 
            self.treeview_widget.delete(items)   
        
        req = f"SELECT NomProduit , `Quantité par unité` ,  `Prix unitaire` , `Nom de catégorie` from produits p inner join catégories g on p.`Code catégorie` = g.`Code catégorie` WHERE p.`Code catégorie` = {self.selcted_code.get()}"
        self.db.cursor.execute(req)
        self.result_of_tree = self.db.cursor.fetchall()

        for items in self.result_of_tree : 
            self.treeview_widget.insert('','end', values=(items[0], items[1], items[2] , items[3]))
            
       # Extracting values for bar chart
        product_names = [item[0] for item in self.result_of_tree]
        prices = [float(item[2]) for item in self.result_of_tree]

        # Clear existing axes content
        self.ax.clear()

        # Create a bar chart
        self.ax.bar(product_names, prices)

        # Set labels and title
        self.ax.set_xlabel('Nom de Produit')
        self.ax.set_ylabel('Prix unitaire')
        self.ax.set_title('Prix unitaire par produit')

        # Redraw the canvas
        self.canvas.draw()

    
        



fenetre = Tk()
Interface =interface(fenetre)
Interface.mainloop()




























