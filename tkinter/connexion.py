import pymysql as sql 
# import matplotlib.pyplot as pl
# import numpy as np

class connexion : 
    """Classe de connexion à la base de données"""
    def __init__(self) :
        self.dbconnection = sql.connect(host="localhost", user='root', password='A1m2i3n4e5@', db='dbcomptoire')

        self.cursor = self.dbconnection.cursor()
        
    def commit_db(self) : 
        self.dbconnection.commit()
        
    def close_db(self) : 
        self.cursor.close()
        self.dbconnection.close()
        
        
# data = connexion()
# data.cursor.execute("SELECT count(détailscommandes.Quantité) , commandes.NCommande FROM commandes   JOIN détailscommandes ON commandes.NCommande= détailscommandes.Ncommande  GROUP BY commandes.NCommande ")
# clients = np.array(data.cursor.fetchall())
# qt = clients.transpose()[1]
# commande = clients.transpose()[0]
# print(qt)
# print("========"*20)
# print(clients[0][:])

# pl.figure()
# pl.bar(qt , commande)
# pl.xlabel("les N de commades ")
# pl.ylabel("les quantity")
# pl.show()
# pl.close()
# data.close_db()