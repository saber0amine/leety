import tkinter as tk
from tkinter import ttk
import pymysql as mysql 

class Connexion:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def execute_query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

class InterfaceConsultation(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Consultation des Articles")

        self.conn = Connexion(host="localhost", user="root", password="A1m2i3n4e5@", database="gestcatego")

        self.create_widgets()

    def create_widgets(self):
        # Création de widgets pour l'interface ici (labels, boutons, graphiques, etc.)
        # Vous pouvez utiliser ttk.Treeview pour afficher les informations dans un tableau, et matplotlib pour le graphique à barres.

        # Exemple : Treeview pour afficher les informations des articles
        self.treeview_articles = ttk.Treeview(self, columns=("Réf", "Libellé", "Prix HT", "Num Catégorie"))
        self.treeview_articles.heading("#0", text="ID")
        self.treeview_articles.heading("Réf", text="Réf")
        self.treeview_articles.heading("Libellé", text="Libellé")
        self.treeview_articles.heading("Prix HT", text="Prix HT")
        self.treeview_articles.heading("Num Catégorie", text="Num Catégorie")

        # Exemple : Graphique à barres pour la répartition des montants de vente
        # Utilisez la bibliothèque matplotlib pour créer le graphique à barres

        # Placez les widgets dans la fenêtre en utilisant grid ou pack, selon vos besoins.

    def query_articles(self, num_categorie):
        # Exécutez la requête SQL pour obtenir les informations des articles pour une catégorie spécifique
        query = "SELECT ref, libelle, prixHt, numCategorie FROM Articles WHERE numCategorie = %s"
        params = (num_categorie,)
        result = self.conn.execute_query(query, params)
        
        # Mettez à jour le Treeview avec les résultats de la requête
        self.update_treeview_articles(result)

    def update_treeview_articles(self, data):
        # Effacez le Treeview avant de mettre à jour avec de nouvelles données
        for item in self.treeview_articles.get_children():
            self.treeview_articles.delete(item)

        # Insérez les nouvelles données dans le Treeview
        for row in data:
            self.treeview_articles.insert("", "end", values=row)

    def query_ventes_par_categorie(self):
        # Exécutez la requête SQL pour obtenir les montants de vente par catégorie
        query = """
            SELECT C.numCategorie, C.intitule, SUM(A.prixHt * (1 + C.TauxTVA/100) * DC.quantite) AS montantVente
            FROM Categorie C
            JOIN Articles A ON C.numCategorie = A.numCategorie
            JOIN DetailColis DC ON A.ref = DC.ref
            GROUP BY C.numCategorie, C.intitule
        """
        result = self.conn.execute_query(query)

        # Affichez les résultats dans le graphique à barres (utilisez la bibliothèque matplotlib)
        # ...

    def on_category_selected(self, event):
        # Cette méthode est appelée lorsqu'une catégorie est sélectionnée dans l'interface
        selected_item = self.treeview_categories.selection()
        if selected_item:
            num_categorie = self.treeview_categories.item(selected_item, "values")[0]
            self.query_articles(num_categorie)
            self.query_ventes_par_categorie()

    def run(self):
        self.mainloop()

    def __del__(self):
        self.conn.close_connection()

# Utilisation de la classe InterfaceConsultation
if __name__ == "__main__":
    app = InterfaceConsultation()
    app.run()
