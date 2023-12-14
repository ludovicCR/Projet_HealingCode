class patient():
    def __init__(self, nom, maladie, argent, poche, etat_sante):
        self.nom = nom
        self.maladie = maladie
        self.argent = argent
        self.poche = poche
        self.etat_sante = etat_sante

    def se_deplacer(self):
        print
    def take_pills(self):
        print
    def payer(self,montant):
        if self.argent >= montant:
            self.argent -= montant
            print(f"{self.nom} paie {montant}.")
    
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

class Docteur:
    def __init__(self ,nom ,argent ,cabinet ,diagnostique ,patient_in=None ,patient_out=None ):
        self.nom = nom
        self.argent = argent
        self.cabinet = cabinet
        self.diagnostique = diagnostique
        self.patient_in = patient_in
        self.patient_out = patient_out

    def payer_consultation(self,patient):
        patient.payer(50)
        self.argent += 50
    
    def prescrire_traitement(self,patient):
        grille_diagnostics = {
            "mal indenté": "ctrl+maj+f",
            "unsave": "saveOnFocusChange",
            "404": "CheckLinkRelation",
            "azmatique": "Ventoline",
            "syntaxError": "f12+doc"
        }

        traitement = grille_diagnostics.get(patient.maladie)
        if traitement:
            print(f"{self.nom} prescrit le traitement {traitement} à {patient.nom}.")
        else:
            print(f"Aucun traitement trouvé pour la maladie de {patient.nom} :( )")
    def diagnostiquer(self, patient):
        print(f"{self.nom} diagnostique {patient.nom}.")
        patient.etat_sante = "En traitement"
        self.payer_consultation(patient)
        self.prescrire_traitement(patient)
        self.patient_out = patient
        self.patient_in = None
    def sortie_patient(self):
        if self.patient_out:
            print(f"{self.nom} fait sortir {self.patient_out.nom} de son cabinet.")
            self.patient_out = None
        else:
            print("Aucun patient à faire sortir.")

debugger = Docteur("Debugger", 0, ["chat"], "-")

#Affichage
print("| Nom       | Argent | Cabinet | Diagnostique | Patient In | Patient Out |")
print("|-----------|--------|---------|--------------|------------|-------------|")
print(f"| {debugger.nom} | {debugger.argent} | {debugger.cabinet} | {debugger.diagnostique} | "
      f"{debugger.patient_in} | {debugger.patient_out} |")

#Simulation
debugger.patient_in = marcus
debugger.diagnostiquer(marcus)
debugger.sortie_patient()