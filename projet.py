from tabulate import tabulate
import time

class Patient:
    def __init__(self, nom, maladie, argent, poche, etat_sante):
        self.nom = nom
        self.maladie = maladie
        self.argent = argent
        self.poche = poche
        self.etat_sante = etat_sante

    def se_rendre(self, endroit):
        print(f"{self.nom} se rend à {endroit}.")
        if endroit == "cabinet":
            self.cabinet()
        elif endroit == "pharmacie":
            self.pharmacie()
        elif endroit == "cimetiere":
            self.cimetiere()

    def cabinet(self):
        print(f"{self.nom} entre dans le cabinet du docteur.")
        self.miaulement_chat()

    def miaulement_chat(self):
        print("Le chat miaule...")
        time.sleep(2)
        print("Le chat miaule encore...")
        time.sleep(2)

    def pharmacie(self):
        print(f"{self.nom} est arrivé à la pharmacie.")

    def payer(self, montant):
        if self.argent >= montant:
            self.argent -= montant
            print(f"{self.nom} paie {montant}.")

    def cimetiere(self):
        print(f"{self.nom} est mort de sa maladie. Il est poussé au cimetière.")
        self.etat_sante = "Mort"

class Docteur:
    def __init__(self, nom, argent, cabinet, diagnostique, patient_in=None, patient_out=None):
        self.nom = nom
        self.argent = argent
        self.cabinet = cabinet
        self.diagnostique = diagnostique
        self.patient_in = patient_in
        self.patient_out = patient_out

    def traiter_patient(self, patient):
        self.diagnostiquer(patient)
        self.sortie_patient()
        self.afficher_salle_attente()

    def payer_consultation(self, patient):
        patient.payer(50)
        self.argent += 50

    def prescrire_traitement(self, patient):
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
        self.afficher_salle_attente()

    def sortie_patient(self):
        if self.patient_out:
            if self.patient_out.etat_sante == "En traitement":
                print(f"{self.nom} fait sortir {self.patient_out.nom} de son cabinet. Le traitement continue.")
            elif self.patient_out.etat_sante == "Mort":
                print(f"{self.nom} fait sortir {self.patient_out.nom} de son cabinet. Malheureusement, il meurt, faute de ne pas avoir su payer son traitement.")
                self.patient_out.cimetiere()
            self.patient_out_nom = self.patient_out.nom
            self.patient_out = None
        else:
            print("Aucun patient à faire sortir.")

    def affiche_info_doc(self):
        patient_in_nom = self.patient_in.nom if self.patient_in else None
        patient_out_nom = self.patient_out.nom if self.patient_out else None

        doctor_data = [[self.nom, self.argent, self.cabinet, self.diagnostique, patient_in_nom, patient_out_nom]]
        print(tabulate(doctor_data, headers=["Nom", "Argent", "Cabinet", "Diagnostique", "Patient In", "Patient Out"], tablefmt="pretty"))

    def afficher_salle_attente(self):
        print("Salle d'attente :")
        table_data = [["Nom", "Maladie", "Argent", "Poche", "État de Santé"]]
        table_data.extend([[p.nom, p.maladie, p.argent, p.poche, p.etat_sante] for p in self.patients_attente])
        print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))
        print("\n")

class Pharmacie:
    def __init__(self):
        self.tarifs_traitements = {
            "ctrl+maj+f": 45,
            "saveOnFocusChange": 85,
            "CheckLinkRelation": 35,
            "Ventoline": 40,
            "f12+doc": 20
        }

    def vendre_traitement(self, patient):
        traitement = patient.poche
        if traitement in self.tarifs_traitements:
            prix_traitement = self.tarifs_traitements[traitement]
            if self.verifier_achat(patient, prix_traitement):
                self.effectuer_achat(patient, prix_traitement, traitement)
        else:
            print(f"Aucun tarif trouvé pour {traitement}.")

    def verifier_achat(self, patient, prix_traitement):
        if patient.argent >= prix_traitement:
            return True
        else:
            print(f"{patient.nom} n'a pas assez d'argent pour acheter le traitement {traitement}.")
            print(f"{patient.nom} est considéré mort et poussé au cimetière.")
            patient.cimetiere()
            return False

    def effectuer_achat(self, patient, prix_traitement, traitement):
        print(f"{patient.nom} achète le traitement {traitement} à {prix_traitement}€ à la pharmacie.")
        patient.argent -= prix_traitement
        print(f"{patient.nom} a maintenant {patient.argent}€.")
        print(f"{patient.nom} prend le traitement et son état de santé s'améliore.")
        patient.etat_sante = "Guéri"

    def affiche_info_pharma(self):
        tarif_data = [[traitement, prix] for traitement, prix in self.tarifs_traitements.items()]
        print(tabulate(tarif_data, headers=["Traitement", "Prix"], tablefmt="grid"))

# Initialisation des patients
patients = [
    Patient("Marcus", "mal indenté", 100, "Vide", "malade"),
    Patient("Optimus", "unsave", 200, "vide", "malade"),
    Patient("Sangoku", "404", 80, "vide", "malade"),
    Patient("DarthVader", "azmatique", 110, "Vide", "malade"),
    Patient("semicolon", "syntaxError", 60, "vide", "malade"),
]

debugger = Docteur("Debugger", 0, ["chat"], "-")
debugger.patients_attente = patients

pharmacie = Pharmacie()

# Simulation du traitement des patients
traitements_patients = ["ctrl+maj+f", "saveOnFocusChange", "CheckLinkRelation", "Ventoline", "f12+doc"]

for patient, traitement in zip(patients, traitements_patients):
    patient.se_rendre("cabinet")
    debugger.patient_in = patient
    debugger.traiter_patient(patient)

    patient.poche = traitement
    pharmacie.vendre_traitement(patient)

    debugger.patient_out = patient
    debugger.affiche_info_doc()


