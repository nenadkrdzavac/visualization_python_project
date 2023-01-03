#Displays results of q9-sankey.sparql query via <none> graph located at https://labs.tib.eu/sdm/coy/sparql endpoint
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import json, urllib

def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('TIB colleagues:')

app = Dash(__name__)

app.layout = html.Div([
    html.H4('First twenty highest exports between value added origin countries and final demand EU countries'),
    dcc.Graph(id="graph"),
    html.P("Opacity"),
    dcc.Slider(id='slider', min=0, max=1,
               value=0.5, step=0.1)
])

@app.callback(
    Output("graph", "figure"),
    Input("slider", "value"))

def display_sankey(opacity):

    #url = 'https://raw.githubusercontent.com/plotly/plotly.js/master/test/image/mocks/sankey_energy.json'
    url = 'https://raw.githubusercontent.com/nenadkrdzavac/mapping-trade-in-value-added/master/src/main/resources/sparql_results/q9-sankey-limited.json'
    response = urllib.request.urlopen(url)

    data = json.loads(response.read()) # replace with your own data source

    node = data['data'][0]['node']

    node['color'] = [
        f'rgba(255,0,255,{opacity})'
        if c == "magenta" else c.replace('0.8', str(opacity))
        for c in node['color']]

    link = data['data'][0]['link']
    link['color'] = [
        node['color'][src] for src in link['source']]

    fig = go.Figure(go.Sankey(link=link, node=node))
    fig.update_layout(font_size=10)
    return fig

app.run_server(debug=True)



