from afficherGraphes import *


titre = "Programme python"
liste_options = [
    "Afficher graphe petit",
    "Afficher graphe moyen",
    "Afficher graphe complet",
    "Collaborateurs en communs",
    "Collaborateurs en communs TEST",
    ]

def afficher_menu(titre, liste_options):
    print("+" + "-" * (len(titre)+2) + "+")
    print("| "+(titre.upper())+" |")
    print("+" + "-" * (len(titre)+2) + "+")

    for i in range (len(liste_options)):
        print(i+1,"->",liste_options[i])
    print("q -> Quitter")
    rep = input("Entrer votre choix [1-"+str(len(liste_options))+"]: ")
    return rep

def programme_principal():
    while True:
        rep = afficher_menu(titre, liste_options)
        if rep is None:
            print("Cette option n'existe pas")
        elif rep == '1':
            print("Vous avez choisi :",liste_options[int(rep) - 1])
            afficher_graphe(construire_graphe("dataTest1.json"))
        elif rep == '2':
            print("Vous avez choisi :", liste_options[int(rep) - 1])
            afficher_graphe(construire_graphe("dataTest2.json"))
        elif rep == '3':
            print("Vous avez choisi :", liste_options[int(rep) - 1])
            print("Bonne chance, pour patienter :", "https://www.youtube.com/watch?v=6R7ykH1movg")
            afficher_graphe('data.json')
        elif rep == '4':
            print("Vous avez choisi :", liste_options[int(rep) - 1])
            acteur1 = input("Entrez le nom de l'acteur 1: ")
            acteur2 = input("Entrez le nom de l'acteur 2: ")
            fichier = input("Entrez un fichier: ")
            graphe = construire_graphe(fichier)
            collaborateurs = collaborateur_en_commun(acteur1, acteur2, graphe)
            print("Les collaborateurs en commun de", acteur1, "et", acteur2, "sont :", collaborateurs)
        elif rep == '5':
            print("Vous avez choisi :", liste_options[int(rep) - 1])
            graphe = construire_graphe("dataTest1.json")
            collaborateurs = collaborateur_en_commun("ACTEUR 1", "ACTEUR 3", graphe)
            print("Les collaborateurs en commun de", acteur1, "et", acteur2, "sont :", collaborateurs)
        elif rep == 'q':
            print("Merci au revoir!")
            break
        else:
            print("Votre réponse n'est pas entre 1 et",str(len(liste_options)))
        input("Appuyer sur Entrée pour retourer au menu ")
programme_principal()
