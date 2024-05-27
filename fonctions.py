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
        for ligne in json_load:
            movie = json.loads(ligne)
            cast = movie["cast"]
            cast = [acteur.strip("[]") for acteur in cast]
            for i in range(len(cast)):
                for j in range(i + 1, len(cast)):
                    G.add_edge(cast[i], cast[j], movie=movie["title"])
    print("Graphe créé")
    return G

def afficher_graphe(G):
    '''
    Affiche le graphe en utilisant la bibliothèque Matplotlib.
    Args:
        G (nx.Graph): Le graphe à afficher.
    '''
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, seed=42)
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
        set: L’ensemble des acteurs qui ont collaboré avec les deux acteurs.
    '''
    if acteur1 not in G.nodes or acteur2 not in G.nodes:
        print(f"Erreur: Un des acteurs ({acteur1}, {acteur2}) n'existe pas dans le graphe.")
        return set()
    voisins_acteur1 = set(G.neighbors(acteur1))
    voisins_acteur2 = set(G.neighbors(acteur2))

    collaborateurs_communs = voisins_acteur1.intersection(voisins_acteur2)
    
    return collaborateurs_communs

def collaborateur_proche(acteur, k, G):
    '''
    Renvoit les acteurs qui se trouvent à distance au plus k d'un acteur
    Args:
        acteur (str): Le nom d'un acteur
        k (int): La distance maximale
        G (nx.Graph): Le graphe contenant les collaborations entre acteurs
    Returns:
        set: L’ensemble des acteurs qui se trouvent à distance au plus k d'un acteur
    '''
    if acteur not in G:
        print(f"Erreur: L'acteur {acteur} n'existe pas dans le graphe.")
        return set()
    
    bfs_tree = nx.bfs_tree(G, acteur, depth_limit=k)
    acteurs_proches = set(bfs_tree.nodes())
    acteurs_proches.remove(acteur)

    return acteurs_proches

def distance_entre_acteurs(acteur1, acteur2, G):
    '''
    Trouve la distance entre deux acteurs dans un graphe.
    Args:
        acteur1 (str): Le nom du premier acteur.
        acteur2 (str): Le nom du second acteur.
        G (nx.Graph): Le graphe contenant les collaborations entre acteurs.
    Returns:
        int: La distance entre les deux acteurs, ou -1 si les acteurs ne sont pas connectés.
    '''
    if acteur1 not in G.nodes or acteur2 not in G.nodes:
        print(f"Erreur: Un des acteurs ({acteur1}, {acteur2}) n'existe pas dans le graphe.")
        return -1

    queue = [(acteur1, 0)]
    visited = set([acteur1])

    while queue:
        current, distance = queue.pop(0)
        if current == acteur2:
            return distance

        for voisin in G.neighbors(current):
            if voisin not in visited:
                visited.add(voisin)
                queue.append((voisin, distance + 1))

    return -1

def excentricite(acteur, G):
    '''
    Calcule l'excentricité d'un acteur dans un graphe.
    Args:
        acteur (str): Le nom de l'acteur.
        G (nx.Graph): Le graphe contenant les collaborations entre acteurs.
    Returns:
        int: L'excentricité de l'acteur.
    '''
    if acteur not in G.nodes:
        print(f"Erreur: L'acteur {acteur} n'existe pas dans le graphe.")
        return -1

    #ici, on utilise l'algorithme de dijkstra
    longest_distance = 0
    for target in G.nodes:
        if target != acteur:
            distance = nx.shortest_path_length(G, source=acteur, target=target)
            if distance > longest_distance:
                longest_distance = distance
    return longest_distance

def acteur_central(G):
    '''
    Trouve l'acteur le plus central dans un graphe.
    Args:
        G (nx.Graph): Le graphe contenant les collaborations entre acteurs.
    Returns:
        str: Le nom de l'acteur le plus central.
    '''
    centralite_min = float('inf')
    acteur_central = None
    
    for acteur in G.nodes:
        centralite_acteur = excentricite(acteur, G)
        if centralite_acteur < centralite_min:
            centralite_min = centralite_acteur
            acteur_central = acteur
    return acteur_central


#TESTS
# dataTest2
# data_100

graphe = construire_graphe("data_100.json")
#distance = distance_entre_acteurs("ACTEUR 1", "ACTEUR 1", graphe)

#print(collaborateur_proche("ACTEUR 5", 1, construire_graphe("dataTest1.json")))

#print(excentricite("James Woods", graphe))
#print(acteur_central(graphe))
afficher_graphe(graphe)