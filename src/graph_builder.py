# src/graph_builder.py

import networkx as nx
import random
from src import config

def create_synthetic_graph():
    """
    Creates a synthetic brain-like graph using power-law clustering.
    """
    G = nx.powerlaw_cluster_graph(
        config.NUM_NODES,
        config.POWERLAW_M,
        config.POWERLAW_P,
        seed=42
    )
    return G

def add_triangle_motifs(G, count=config.TRIANGLE_COUNT):
    """
    Adds triangle motifs into the graph to simulate local redundancy.
    """
    added = 0
    while added < count:
        nodes = random.sample(list(G.nodes()), 3)
        if not all(G.has_edge(u, v) for u, v in [(nodes[0], nodes[1]), (nodes[1], nodes[2]), (nodes[2], nodes[0])]):
            G.add_edges_from([
                (nodes[0], nodes[1]),
                (nodes[1], nodes[2]),
                (nodes[2], nodes[0])
            ])
            added += 1
    return G
