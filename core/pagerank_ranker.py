import networkx as nx

G = nx.read_gpickle("../asset_graph.gpickle")
pr = nx.pagerank(G)

asset_scores = {n:s for n,s in pr.items() if G.nodes[n].get("type")=="asset_fragment"}

for asset, score in sorted(asset_scores.items(), key=lambda x:x[1], reverse=True):
    print(asset, round(score,4))