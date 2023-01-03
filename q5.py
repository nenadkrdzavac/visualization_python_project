# Sum of gross exports for EU countries. Displays result of q5.sparql
import plotly.graph_objects as go

fig = go.Figure(data=[go.Sankey(
    node = dict(
        pad = 15,
        thickness = 20,
        line = dict(color = "black", width = 0.5),
        label = ["DEU", "ITA", "FRA", "ESP", "AUT", "POL", "NLD", "CZE", "BEL", "SWE", "SVK", "HUN", "FIN", "PRT", "IRL", "DNK", "NOR", "SVN", "GRC", "LUX", "BGR", "HRV", "EST", "LTU", "LVA", "MLT", "CYP",
                 "gross_export" ],
        color = "blue"
    ),
    link = dict(
        source = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26], # indices correspond to labels, eg A1, A2, A2, B1, ...
        target = [27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27],
        value = [13665590.17,
                 6499552.768,
                 4733456.841,
                 3291333.449,
                 2568275.529,
                 2337396.296,
                 1940959.864,
                 1833709.06,
                 1701192.368,
                 1552090.781,
                 1102518.569,
                 982303.69,
                 804312.318,
                 630536.883,
                 595786.569,
                 587727.602,
                 465150.076,
                 463451.835,
                 358356.684,
                 297030.137,
                 284681.374,
                 129759.106,
                 117422.859,
                 96180.93,
                 62335.731,
                 31499.91,
                 18407.405 ],

    ))])

fig.update_layout(title_text="Sum of gross exports for EU countries", font_size=10)
fig.show()
