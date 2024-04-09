import networkx as nx
import json
import matplotlib.pyplot as plt


def afficher_graphe(nom_fichier):
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

    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=35, node_color="skyblue", edge_color="gray", alpha=0.7, font_size=5)

    plt.show()