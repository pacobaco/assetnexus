import pandas as pd
import networkx as nx

df = pd.read_csv("../data/sample_ledger.csv")
G = nx.DiGraph()

for _, row in df.iterrows():
    asset = row["asset_ref"]
    vendor = row["vendor"]
    location = row["location"]
    event = row["description"]
    date = row["date"]

    G.add_node(asset, type="asset_fragment")
    G.add_node(vendor, type="vendor")
    G.add_node(location, type="location")
    G.add_node(event, type="event")

    G.add_edge(asset, vendor, relation="supplied_by", timestamp=date)
    G.add_edge(asset, location, relation="located_at", timestamp=date)
    G.add_edge(asset, event, relation="event", timestamp=date)

nx.write_gpickle(G, "../asset_graph.gpickle")
print("Graph built successfully.")