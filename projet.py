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

    def cimetiere(self):
        print(f"{self.nom} est mort de sa maladie. Il est poussé au cimetière.")
        self.etat_sante = "Mort"


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
            if self.patient_out.etat_sante == "En traitement":
                print(f"{self.nom} fait sortir {self.patient_out.nom} de son cabinet. Le traitement continue.")
            elif self.patient_out.etat_sante == "Mort":
                print(f"{self.nom} fait sortir {self.patient_out.nom} de son cabinet. Malheureusement il meurt, faute de ne pas avoir su payer son traitement.")
            self.patient_out = None

        else:
            print("Aucun patient à faire sortir.")

    def affiche_info_doc(self):
        doctor_data = [[self.nom, self.argent, self.cabinet, self.diagnostique, self.patient_in, self.patient_out]]
        print(tabulate(doctor_data, headers=["Nom", "Argent", "Cabinet", "Diagnostique", "Patient In", "Patient Out"], tablefmt="pretty"))

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
                patient.cimetiere()
                return False
        else:
            print(f"Aucun tarif trouvé pour {traitement}.")

    def affiche_info_pharma(self):
        tarif_data = [[traitement, prix] for traitement, prix in self.tarifs_traitements.items()]
        print(tabulate(tarif_data, headers=["Traitement", "Prix"], tablefmt="grid"))

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


for patient, traitement in zip(patients,traitements_patients):
    debugger.patient_in = patient
    debugger.diagnostiquer(patient)
    debugger.sortie_patient()

    doctor_data = [[debugger.nom, debugger.argent, debugger.cabinet, debugger.diagnostique, debugger.patient_in, debugger.patient_out]]
    patient_data = [[p.nom, p.maladie, p.argent, p.poche, p.etat_sante] for p in patients]

    complete_data = [[debugger.nom, debugger.argent, debugger.cabinet, debugger.diagnostique, debugger.patient_in, debugger.patient_out]] + [[p.nom, p.maladie, p.argent, p.poche, p.etat_sante] for p in patients]

    print(tabulate(complete_data, headers=["Nom", "Argent", "Cabinet", "Diagnostique", "Patient In", "Patient Out", "Maladie", "Argent", "Poche", "État de Santé"], tablefmt="grid"))

    patient.poche = traitement
    pharmacie.vendre_traitement(patient)

   # Mise à jour de la liste des données du docteur
    doctor_data = [[debugger.nom, debugger.argent, debugger.cabinet, debugger.diagnostique, debugger.patient_in, debugger.patient_out]]
    patient_data = [[p.nom, p.maladie, p.argent, p.poche, p.etat_sante] for p in patients]

    # Concaténez les données du docteur et des patients dans une seule liste
    complete_data = [[debugger.nom, debugger.argent, debugger.cabinet, debugger.diagnostique, debugger.patient_in, debugger.patient_out]] + [[p.nom, p.maladie, p.argent, p.poche, p.etat_sante] for p in patients]

    # Utilisez la bibliothèque tabulate pour afficher toutes les informations
    print(tabulate(complete_data, headers=["Nom", "Argent", "Cabinet", "Diagnostique", "Patient In", "Patient Out", "Maladie", "Argent", "Poche", "État de Santé"], tablefmt="grid"))