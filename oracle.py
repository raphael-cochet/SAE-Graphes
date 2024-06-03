from requetes import *

titre = "A la conquête d’Hollywood"
liste_options = [
    "Afficher le graphe",
    "Collaborateurs en communs",
    "Collaborateur proche",
    "Est proche",
    "Distance naive",
    "Distance entre acteurs",
    "Centralite d'un acteur",
    "Trouver l'acteur central",
    "Trouver eloignement max",
    "Centralite du groupe",
    "Temps d'execution de distance"
]

def afficher_menu(titre, liste_options):
    print("+" + "-" * (len(titre) + 2) + "+")
    print("| " + titre.upper() + " |")
    print("+" + "-" * (len(titre) + 2) + "+")

    for i in range(len(liste_options)):
        print(i + 1, "->", liste_options[i])
    print("q -> Quitter")
    rep = input("Entrer votre choix [1-" + str(len(liste_options)) + "]: ")
    return rep

def programme_principal():
    fichier = input("Entrez un fichier à charger (sans le .json): ")
    try:
        G = json_vers_nx(fichier + ".json")
    except Exception as e:
        print("Erreur lors du chargement du fichier:", e)
        return
    
    while True:
        rep = afficher_menu(titre, liste_options)
        if rep is None:
            print("Cette option n'existe pas")
        elif rep == '1': # Afficher le graphe
            print("Vous avez choisi :", liste_options[int(rep) - 1])
            afficher_graphe(G)
        elif rep == '2': # Collaborateurs en communs
            print("Vous avez choisi :", liste_options[int(rep) - 1])
            acteur1 = input("Entrez le nom de l'acteur 1: ")
            acteur2 = input("Entrez le nom de l'acteur 2: ")
            print("Les collaborateurs en commun de", acteur1, "et", acteur2, "sont :", collaborateurs_communs(G, acteur1, acteur2))
        elif rep == '3': # Collaborateur proche
            print("Vous avez choisi :", liste_options[int(rep) - 1])
            acteur = input("Entrez le nom de l'acteur: ")
            k = int(input("Entrez la distance maximale: "))
            print("Les acteurs proches de", acteur, "sont :", collaborateurs_proches(G, acteur, k))
        elif rep == '4': # Est proche
            print("Vous avez choisi :", liste_options[int(rep) - 1])
            acteur1 = input("Entrez le nom de l'acteur 1: ")
            acteur2 = input("Entrez le nom de l'acteur 2: ")
            if (est_proche(G,acteur1,acteur2,k=1)):
                print("L'acteur", acteur1, "est proche de", acteur2)
            else:
                print("L'acteur", acteur1, "n'est pas proche de", acteur2)
        elif rep == '5': # Distance naive
            print("Vous avez choisi :", liste_options[int(rep) - 1])
            acteur1 = input("Entrez le nom de l'acteur 1: ")
            acteur2 = input("Entrez le nom de l'acteur 2: ")
            print("La distance naive entre", acteur1, "et", acteur2, "est :", distance_naive(G, acteur1, acteur2))
        elif rep == '6': # Distance entre acteurs
            print("Vous avez choisi :", liste_options[int(rep) - 1])
            acteur1 = input("Entrez le nom de l'acteur 1: ")
            acteur2 = input("Entrez le nom de l'acteur 2: ")
            print("La distance entre", acteur1, "et", acteur2, "est :", distance(G, acteur1, acteur2))
        elif rep == '7': # Centralite d'un acteur
            print("Vous avez choisi :", liste_options[int(rep) - 1])
            acteur = input("Entrez le nom de l'acteur: ")
            print("L'excentricité de:", acteur, "est de:", centralite(G, acteur))
        elif rep == '8': # Trouver l'acteur central
            print("Vous avez choisi :", liste_options[int(rep) - 1])
            print("L'acteur le plus central du graphe est:", centre_hollywood(G))
        elif rep == '9': # Trouver eloignement max
            print("Vous avez choisi :", liste_options[int(rep) - 1])
            print("L'éloignement max est:", eloignement_max(G))
        elif rep == '10': # Centralite du groupe
            print("Vous avez choisi :", liste_options[int(rep) - 1])
            liste = input("Entrez une liste acteur: ")
            print("L'éloignement max est:", centralite_groupe(G, liste))
        elif rep == '11': # Temps d'execution de distance"
            print("Vous avez choisi :", liste_options[int(rep) - 1])
            acteur1 = input("Entrez le nom de l'acteur 1: ")
            acteur2 = input("Entrez le nom de l'acteur 2: ")
            temps_bfs, temps_dijkstra = mesurer_temps_execution(G, acteur1, acteur2)
            print(f"Temps d'exécution pour BFS: {temps_bfs:.6f} secondes")
            print(f"Temps d'exécution pour Dijkstra: {temps_dijkstra:.6f} secondes")
        elif rep == 'q':
            print("Merci, au revoir!")
            break
        else:
            print("Votre réponse n'est pas entre 1 et", str(len(liste_options)))
        input("Appuyer sur une touche pour retourner au menu ")

programme_principal()
