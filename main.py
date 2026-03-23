# main.py

from gestion_transport import *

clients = []
taxis = []
itineraires = []

initialiser_donnees(taxis, itineraires)

while True:
    print("\n========= MENU PRINCIPAL =========")
    print("1. PRENDRE UN TAXI")
    print("2. AJOUTER UN TAXI OU UN CLIENT")
    print("3. AJOUTER UN ITINERAIRE")
    print("4. AFFICHER LES TRAJETS (itinéraires)")
    print("5. AFFICHER LES CLIENTS")
    print("6. AFFICHER LES VOITURES")
    print("7. Quitter")
    choix = input("Choix : ")

    if choix == "1":
        prendre_taxi(itineraires, taxis)
    elif choix == "2":
        print("\n1. Ajouter un client")
        print("2. Ajouter un taxi")
        sous_choix = input("Choix : ")
        if sous_choix == "1":
            ajouter_client(clients)
        elif sous_choix == "2":
            ajouter_taxi(taxis, itineraires)
        else:
            print("❌ Choix invalide.")
    elif choix == "3":
        ajouter_itineraire(itineraires)
    elif choix == "4":
        afficher_itineraires(itineraires)
    elif choix == "5":
        afficher_clients(clients)
    elif choix == "6":
        afficher_voitures(taxis)
    elif choix == "7":
        print("👋 Au revoir !")
        break
    else:
        print("❌ Choix invalide.")
