from tkinter import * 
import tkinter.font as tkFt

class Interface(Frame):
    def __init__(self , fenetre , **kwargs) : 
        Frame.__init__(self,fenetre)
        self.pack(fill=BOTH)
        self.header = Entry(self ,  width=40)
        self.header.insert(END , "Amine Saber")
        self.header.pack()  
        
        
        frame1 = Frame(self) 
        frame1.pack()
        
        
        styleLabel = LabelFrame(frame1 , text="Style")
        styleLabel.grid(row=0 , column = 0 , pady=8)
        styleContent = ["normal" , "bold" , "italic" ,  "bold italic"]
        self.style = StringVar() ; self.style.set(styleContent[0])
        for i in range(4) : 
            btnWidget = Radiobutton(styleLabel , text=styleContent[i] , variable=self.style , value=styleContent[i] , command=self.add_style )
            btnWidget.pack(anchor=W)


        tailleLabel = LabelFrame(frame1 ,text="Taille")
        tailleLabel.grid(row=0 , column = 1 )
        self.scrollWidget = Scale(tailleLabel , orient="horizontal" ,from_=10 , to=30 , command=self.add_taill)
        self.taill = IntVar()
        self.taill.set(25)
        self.scrollWidget.set(self.taill.get())
        self.scrollWidget.grid(row= 0  , column = 1 )
        
        
        policeLabel = LabelFrame(frame1 , text="Police ")
        policeLabel.grid( row=0 ,column=2)
        self.police = StringVar()

        scrol_barWidget = Scrollbar(policeLabel)
        
        list = Listbox(policeLabel , relief=SUNKEN, height=6)
        scrol_barWidget.config(command=list.yview)
        list.config(yscrollcommand=scrol_barWidget.set)
        scrol_barWidget.pack(side='right' , fill=Y)
        list.pack()
        self.listbox = list
        list.bind('<Double-Button-1>' , self.add_police)
        
        for items in tkFt.families() : 
            list.insert(END , items)
        print(list)

    def add_police(self , event) : 
        self.police = self.listbox.get(self.listbox.curselection())
        self.add_style()
        print(self.listbox.curselection())
    def add_taill(self , event) : 
        self.taill = self.scrollWidget.get()
        self.add_style()
    def add_style(self): 
        self.header.config(font=( self.police , self.taill ,  self.style.get()))

fenetre = Tk()
fenetre.geometry("400x300")
fenetre.title("Exemple TK ")
interface = Interface(fenetre)
interface.mainloop()
