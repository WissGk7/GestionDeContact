import os

FICHIER_CONTACTS = "contacts.txt"


# Ajouter un contact
def ajouter_contact():
    nom = input("Nom : ")
    prenom = input("Prénom : ")
    numero = input("Numéro de téléphone : ")

    with open(FICHIER_CONTACTS, "a") as f:
        f.write(f"{nom},{prenom},{numero}\n")

    print("✅ Contact ajouté.")