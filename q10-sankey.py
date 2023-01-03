# First ten highest gross exports of value added origin countries with DE. Displays result of q10-sankey.sparql
import plotly.graph_objects as go

fig = go.Figure(data=[go.Sankey(
    node = dict(
        pad = 15,
        thickness = 20,
        line = dict(color = "green", width = 0.5),
        label = ["WLD",
                 "G20",
                 "OECD",
                 "ZEUR",
                 "EU28",
                 "EU27_2020",
                 "EU15",
                 "EA19",
                 "DXD",
                 "APEC",
                 "DEU"],
        color = "blue"
    ),
    link = dict(
        source = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ], # indices correspond to labels, eg A1, A2, A2, B1, ...
        target = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        value = [1603701.755,
                 1545507.428,
                 1482903.463,
                 1448815.328,
                 1393099.256,
                 1383968.728,
                 1332220.215,
                 1319089.034,
                 1140611.476,
                 143534.598
                 ],
    ))])

fig.update_layout(title_text="First ten highest gross exports of value added origin countries with DE", font_size=10)
fig.show()
