from tkinter import *
from tkinter import ttk
from connexion  import connexion

class  interface(Frame) :
    def __init__(self, fenetre):
        Frame.__init__(self, fenetre ) 
        self.pack()
        self.db = connexion()
        
        self.nom = Entry(self)
        nom_label =  Label(self ,  text="Nom et Prenom :")
        
        nom_label.grid(row = 0 , column=0)
        self.nom.grid(row= 0 , column=1 , padx=10)
        
        
        sexe_label= Label(self , text="Sexe :") 
        self.radio_selected1 = StringVar()
        sexe_list = ["Masulin" ,"Feminin" ]
        
        for item in range(2) : 
            sexe = Radiobutton(self , text=sexe_list[item] , variable=self.radio_selected1 , value=sexe_list[item] )
            sexe.grid(row= 1 , column=item + 1)

        sexe_label.grid(row= 1 , column=0 )
        

        self.date_nais = Entry(self)
        date_nais_label =  Label(self ,  text="Date de naissance :")
        
        date_nais_label.grid(row = 2 , column=0)
        self.date_nais.grid(row= 2 , column=1 , padx=10)
        
        
        self.email = Entry(self)
        email_label =  Label(self ,  text="Email :")
        
        email_label.grid(row = 3 , column=0)
        self.email.grid(row= 3 , column=1 , padx=10)

        self.profil_selected = StringVar()
        
        profils = ttk.Combobox(self ,  values=["Etudiant" , "prof"] , textvariable=self.profil_selected)
        profils_label =  Label(self ,  text="Profil :")
        profils_label.grid(row = 4 , column=0)  
        profils.grid(row= 4 , column=1 , padx=10)
        
        
        ajout_btn = Button(self , text="Ajouter" , command=self.ajout_perssone )
        annuler_btn = Button(self , text="Annuler" , command=self.quit)
        ajout_btn.grid(row=5 , column=0)
        annuler_btn.grid(row=5 , column=1)
        
        
    def ajout_perssone(self) : 
            user_name = self.nom.get()
            user_date = self.date_nais.get()
            user_email = self.email.get()
            user_sexe = self.radio_selected1.get()
            user_profil = self.profil_selected.get()
            # req = "INSERT INTO personne (id , nomPrenom, sexe, dateNaiss, email, idProfil) VALUES (1, %s, %s, %s, %s, %s)"
            # values = (user_name, user_sexe, user_date, user_email, user_profil)
            
            req = "INSERT INTO profil (id , libelle) VALUES (%s, %s)"
            values = (3, user_profil)
            self.db.cursor.execute(req, values)
                    

fenetre = Tk()
inter = interface(fenetre)
inter.mainloop()