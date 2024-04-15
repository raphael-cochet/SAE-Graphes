from afficherGraphes import *


titre = "Programme python"
liste_options = [
    "Afficher graphe petit",
    "Afficher graphe moyen",
    "Afficher graphe complet",
    "Collaborateurs en communs",
    "Quitter"
    ]

def afficher_menu(titre, liste_options):
    print("+" + "-" * (len(titre)+2) + "+")
    print("| "+(titre.upper())+" |")
    print("+" + "-" * (len(titre)+2) + "+")

    for i in range (len(liste_options)):
        print(i+1,"->",liste_options[i])
    rep = input("Entrer votre choix [1-"+str(len(liste_options))+"]: ")
    return rep

def programme_principal():
    while True:
        rep = afficher_menu(titre, liste_options)
        if rep is None:
            print("Cette option n'existe pas")
        elif rep == '1':
            print("Vous avez choisi :",liste_options[int(rep) - 1]) 
            afficher_graphe('dataTest1.json')
        elif rep == '2':
            print("Vous avez choisi :", liste_options[int(rep) - 1])
            afficher_graphe('dataTest2.json')
        elif rep == '3':
            print("Vous avez choisi :", liste_options[int(rep) - 1])
            print("Bonne chance, pour patienter :", "https://www.youtube.com/watch?v=Sagg08DrO5U")
            afficher_graphe('data.json')
        elif rep == '3':
            print("Vous avez choisi :", liste_options[int(rep) - 1])
            afficher_graphe('dataTraining.json')
            break
        else:
            print("Votre réponse n'est pas entre 1 et",str(len(liste_options)))
        input("Appuyer sur Entrée pour retourer au menu ")
    print("Merci au revoir!")
programme_principal()

