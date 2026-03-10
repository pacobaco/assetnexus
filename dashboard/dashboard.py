import dash
from dash import dcc, html
import networkx as nx
import plotly.graph_objects as go

G = nx.read_gpickle("../asset_graph.gpickle")
pos = nx.spring_layout(G)

edge_x, edge_y = [], []
for e in G.edges():
    x0,y0 = pos[e[0]]
    x1,y1 = pos[e[1]]
    edge_x += [x0,x1,None]
    edge_y += [y0,y1,None]

edge_trace = go.Scatter(x=edge_x, y=edge_y, mode="lines")

node_x,node_y,node_text=[],[],[]
for n in G.nodes():
    x,y = pos[n]
    node_x.append(x)
    node_y.append(y)
    node_text.append(n)

node_trace = go.Scatter(x=node_x, y=node_y, mode="markers+text", text=node_text)

fig = go.Figure(data=[edge_trace,node_trace])

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("AssetNexus Graph Dashboard"),
    dcc.Graph(figure=fig)
])

app.run_server(debug=True)
