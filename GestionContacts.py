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


# Lire les contacts depuis le fichier
def lire_contacts():
    contacts = []
    if os.path.exists(FICHIER_CONTACTS):
        with open(FICHIER_CONTACTS, "r") as f:
            for ligne in f:
                ligne = ligne.strip()
                if ligne:
                    nom, prenom, numero = ligne.split(",", 2)
                    contacts.append({"nom": nom, "prenom": prenom, "numero": numero})
    return contacts


# Afficher tous les contacts
def afficher_contacts():
    contacts = lire_contacts()
    if not contacts:
        print("📭 Aucun contact trouvé.")
    else:
        print("📒 Liste des contacts :")
        for i, c in enumerate(contacts, 1):
            print(f"{i}. {c['prenom']} {c['nom']} - 📞 {c['numero']}")


# Rechercher un contact
def rechercher_contact():
    mot_cle = input("Nom ou prénom à rechercher : ").lower()
    contacts = lire_contacts()
    resultats = [c for c in contacts if mot_cle in c['nom'].lower() or mot_cle in c['prenom'].lower()]

    if not resultats:
        print("🔍 Aucun contact trouvé.")
    else:
        for c in resultats:
            print(f"{c['prenom']} {c['nom']} - 📞 {c['numero']}")


# Supprimer un contact
def supprimer_contact():
    contacts = lire_contacts()
    afficher_contacts()
    try:
        index = int(input("Numéro du contact à supprimer : ")) - 1
        if 0 <= index < len(contacts):
            contact_supprimé = contacts.pop(index)
            with open(FICHIER_CONTACTS, "w") as f:
                for c in contacts:
                    f.write(f"{c['nom']},{c['prenom']},{c['numero']}\n")
            print(f"🗑️ Contact supprimé : {contact_supprimé['prenom']} {contact_supprimé['nom']}")
        else:
            print("❌ Index invalide.")
    except ValueError:
        print("❌ Entrée invalide.")


# Menu principal
def menu():
    while True:
        print("\n📱 GESTION DE CONTACTS")
        print("1. Ajouter un contact")
        print("2. Afficher les contacts")
        print("3. Rechercher un contact")
        print("4. Supprimer un contact")
        print("5. Quitter")

        choix = input("Choix : ")

        if choix == '1':
            ajouter_contact()
        elif choix == '2':
            afficher_contacts()
        elif choix == '3':
            rechercher_contact()
        elif choix == '4':
            supprimer_contact()
        elif choix == '5':
            print("👋 Au revoir !")
            break
        else:
            print("❗ Choix invalide.")


if __name__ == "__main__":
    menu()
