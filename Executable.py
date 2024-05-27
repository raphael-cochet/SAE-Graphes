from fonctions import *

titre = "A la conquête d’Hollywood"
liste_options = [
    "Afficher le graphe",
    "Collaborateurs en communs",
    "Collaborateur proche",
    "Distance entre acteurs",
    "Excentricite d'un acteur",
    "Trouver l'acteur central",
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
    fichier = input("Entrez un fichier à charger (sans le .json): ")
    try:
        G = construire_graphe(fichier+".json")
    except Exception as e:
        print("Erreur lors du chargement du fichier:", e)
        return
    
    while True:
        rep = afficher_menu(titre, liste_options)
        if rep is None:
            print("Cette option n'existe pas")
        elif rep == '1':
            print("Vous avez choisi :", liste_options[int(rep) - 1])
            afficher_graphe(G)
        elif rep == '2':
            print("Vous avez choisi :", liste_options[int(rep) - 1])
            acteur1 = input("Entrez le nom de l'acteur 1: ")
            acteur2 = input("Entrez le nom de l'acteur 2: ")
            print("Les collaborateurs en commun de", acteur1, "et", acteur2, "sont :", collaborateur_en_commun(acteur1, acteur2, G))
        elif rep == '3':
            print("Vous avez choisi :", liste_options[int(rep) - 1])
            acteur = input("Entrez le nom de l'acteur: ")
            k = int(input("Entrez la distance maximale: "))
            print("Les acteurs proches de", acteur, "sont :", collaborateur_proche(acteur, k, G))
        elif rep == '4':
            print("Vous avez choisi :", liste_options[int(rep) - 1])
            acteur1 = input("Entrez le nom de l'acteur 1: ")
            acteur2 = input("Entrez le nom de l'acteur 2: ")
            print("La distance entre", acteur1, "et", acteur2, "est :", distance_entre_acteurs(acteur1, acteur2, G))
        elif rep == '5':
            acteur = input("Entrez le nom de l'acteur: ")
            print("L'excentricité de:", acteur, "est", excentricite(acteur, G))
        elif rep == '6':
            print("L'acteur le plus central du graphe est:", acteur_central(G))
        elif rep == 'q':
            print("Merci, au revoir!")
            break
        else:
            print("Votre réponse n'est pas entre 1 et", str(len(liste_options)))
        input("Appuyer sur une touche pour retourner au menu ")

programme_principal()
