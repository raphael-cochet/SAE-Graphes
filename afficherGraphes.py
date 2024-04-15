import networkx as nx
import json
import matplotlib.pyplot as plt

def construire_graphe(nom_fichier):
    '''
    Construit un graphe à partir d'un fichier JSON contenant des films et leurs acteurs.
    Args:
        nom_fichier (str): Le nom du fichier JSON.
    Returns:
        nx.Graph: Un graphe NetworkX où les nœuds sont les acteurs et les arêtes représentent les collaborations entre acteurs dans des films.
    '''
    G = nx.Graph()

    with open(nom_fichier) as json_load:
        for line in json_load:
            movie = json.loads(line)
            cast = movie["cast"]
            for i in range(len(cast)):
                for j in range(i + 1, len(cast)):
                    actor1 = cast[i].strip("[]")
                    actor2 = cast[j].strip("[]")
                    G.add_edge(actor1, actor2, movie=movie["title"])
    return G

def afficher_graphe(G):
    '''
    Affiche le graphe en utilisant la bibliothèque Matplotlib.
    Args:
        G (nx.Graph): Le graphe à afficher.
    '''
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=35, node_color="skyblue", edge_color="gray", alpha=0.7, font_size=5)
    plt.show()

def collaborateur_en_commun(acteur1, acteur2, G):
    '''
    Renvoit l’ensemble des acteurs qui ont collaboré avec deux personnes.
    Args:
        acteur1 (str): Le nom d'un acteur
        acteur2 (str): Le nom d'un acteur
        G (nx.Graph): Le graphe contenant les collaborations entre acteurs
    Returns:
        set: L’ensemble des acteurs qui ont collaboré avec les deux acteurs spécifiés.
    '''
    if acteur1 not in G.nodes or acteur2 not in G.nodes:
        return set()
    voisins_acteur1 = set(G.neighbors(acteur1))
    voisins_acteur2 = set(G.neighbors(acteur2))

    collaborateurs_communs = voisins_acteur1.intersection(voisins_acteur2)
    
    return collaborateurs_communs
