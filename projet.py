class patient():
    def __init__(self, nom, maladie, argent, poche, etat__sante):
        self.nom = nom
        self.maladie = maladie
        self.argent = argent
        self.poche = poche
        self.etat_sante = etat__sante

    def se_deplacer(self):
        print
    def take_pills(self):
        print
    def payer(self):
        print
    def afficher_info(self):
        print(f"| {self.nom} | {self.maladie} | {self.argent} | {self.poche} | {self.etat_sante} |")
#Initialisation
marcus = patient ("Marcus","Mal indenté",100,[],"malade")
optimus = patient ("Optimus","unsave",200,[],"malade")
sangoku = patient ("Sangoku","404",80,[],"malade")
darth_vader = patient ("DarthVader","Azmatique",110,[],"malade")
semicolon = patient ("Semicolon","syntaxError",60,[],"malade")
#Affichage informations patients
print("| Nom    | Maladie      | Argent  | Poche   | Etat de santé    |")
marcus.afficher_info()
optimus.afficher_info()
sangoku.afficher_info()
darth_vader.afficher_info()
semicolon.afficher_info()
