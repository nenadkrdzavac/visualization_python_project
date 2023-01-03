# Gross exports between G20 and DE per year. Displays result of q8.sparql
import plotly.graph_objects as go

fig = go.Figure(data=[go.Sankey(
    node = dict(
        pad = 15,
        thickness = 20,
        line = dict(color = "green", width = 0.5),
        label = ["2018",
                 "2017",
                 "2016",
                 "2015",
                 "gross_export"
                 ],
        color = "blue"
    ),
    link = dict(
        source = [0, 1, 2, 3 ], # indices correspond to labels, eg A1, A2, A2, B1, ...
        target = [4, 4, 4, 4],
        value = [428618.344,
                 388927.091,
                 363191.097,
                 364770.896
                 ],
    ))])

fig.update_layout(title_text="Gross exports between G20 and DE per year", font_size=10)
fig.show()
