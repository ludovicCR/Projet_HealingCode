from tabulate import tabulate

class Patient():
    def __init__(self, nom, maladie, argent, poche, etat_sante):
        self.nom = nom
        self.maladie = maladie
        self.argent = argent
        self.poche = poche
        self.etat_sante = etat_sante

    def se_rendre(self,endroit):
        print (f"{self.nom} se rend à {endroit}.")
        if endroit == "cabinet":
            self.cabinet()
        elif endroit == "pharmacie":
            self.pharmacie()
        elif endroit == "cimetiere":
            self.cimetiere()
    
    def cabinet(self):
        print(f"{self.nom} arrive au cabinet du docteur")

    def pharmacie(self):
        print(f"{self.nom} est arrivé à la pharmacie.")

    def cimetiere(self):
        print(f"{self.nom} est mort de sa maladie. Il est poussé au cimetière.")
    
    def take_pills(self):
        print
    
    def payer(self,montant):
        if self.argent >= montant:
            self.argent -= montant
            print(f"{self.nom} paie {montant}.")
    
    def afficher_info(self):
        print(f"| {self.nom} | {self.maladie} | {self.argent} | {self.poche} | {self.etat_sante} |")

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

#Class pharma
            
class Pharmacie:
    def __init__(self):
        self.tarifs_traitements = {
            "ctrl+maj+f": 55,
            "saveOnFocusChange": 75,
            "CheckLinkRelation": 35,
            "Ventoline": 40,
            "f12+doc": 20

        }
    def vendre_traitement(self, patient):
        traitement = patient.poche
        if traitement in self.tarifs_traitements:
            prix_traitement = self.tarifs_traitements[traitement]
            if patient.argent >= prix_traitement:
                print(f"{patient.nom} achète le traitement {traitement} à {prix_traitement}€ à la pharmacice.")
                patient.argent -= prix_traitement
                print(f"{patient.nom} a maintenant {patient.argent}€")
                print (f"{patient.nom} prend le traitement et son état de santé s'améliore")
                return True
            else:
                print(f"{patient.nom} n'a pas assez d'argent pour acheter le traitement {traitement}.")
                print(f"{patient.nom} est considéré mort et poussé au cimetière.")
                return False
        else:
            print(f"Aucun tarif trouvé pour {traitement}.")

# Initialisation des patients
patients = [
    Patient("Marcus","mal indenté",100,"Vide","malade"),
    Patient("Optimus","unsave",200,"vide","malade"),
    Patient("Sangoku","404",80,"vide","malade"),
    Patient("DarthVader","azmatique",110,"Vide","malade"),
    Patient("semicolon","syntaxError",60,"vide","malade"),
]

debugger = Docteur("Debugger", 0, ["chat"], "-")

pharmacie = Pharmacie()

# Simulation de l'achat de traitement par les patients
traitements_patients = ["ctrl+maj+f", "saveOnFocusChange", "CheckLinkRelation", "Ventoline", "f12+doc"]

print("| Nom       | Maladie         | Argent | Poche | État de Santé |")
print("|-----------|-----------------|--------|-------|---------------|")
patient_data = [[patient.nom, patient.maladie, patient.argent, patient.poche, patient.etat_sante] for patient in patients]
print(tabulate(patient_data, headers=["Nom", "Maladie", "Argent", "Poche", "État de Santé"], tablefmt="grid"))

doctor_data = [[debugger.nom, debugger.argent, debugger.cabinet, debugger.diagnostique, debugger.patient_in, debugger.patient_out]]
print("| Nom       | Argent | Cabinet | Diagnostique | Patient In | Patient Out |")
print("|-----------|--------|---------|--------------|------------|-------------|")
print(tabulate(doctor_data, headers=["Nom", "Argent", "Cabinet", "Diagnostique", "Patient In", "Patient Out"], tablefmt="grid"))

for patient in patients:
    debugger.patient_in = patient
    debugger.diagnostiquer(patient)
    debugger.sortie_patient()

    doctor_data = [[debugger.nom, debugger.argent, debugger.cabinet, debugger.diagnostique, debugger.patient_in, debugger.patient_out]]

    print("| Nom       | Argent | Cabinet | Diagnostique | Patient In | Patient Out |")
    print("|-----------|--------|---------|--------------|------------|-------------|")
    print(tabulate(doctor_data, headers=["Nom", "Argent", "Cabinet", "Diagnostique", "Patient In", "Patient Out"], tablefmt="grid"))

    patient.poche = traitements_patients[patients.index(patient)]
    pharmacie.vendre_traitement(patient)

    # Mise à jour de la liste des données du docteur
    doctor_data = [[debugger.nom, debugger.argent, debugger.cabinet, debugger.diagnostique, debugger.patient_in, debugger.patient_out]]
    
    # Affichage des informations du docteur et des patients après chaque étape
    print("| Nom       | Argent | Cabinet | Diagnostique | Patient In | Patient Out |")
    print("|-----------|--------|---------|--------------|------------|-------------|")
    print(tabulate(doctor_data, headers=["Nom", "Argent", "Cabinet", "Diagnostique", "Patient In", "Patient Out"], tablefmt="grid"))


