import pandas as pd
from pySankey.sankey import sankey
import seaborn as sns

#url = "https://raw.githubusercontent.com/nenadkrdzavac/mapping-trade-in-value-added/master/src/main/resources/test.csv"
#url = "https://raw.githubusercontent.com/anazalea/pySankey/master/pysankey/fruits.txt"
url = "https://github.com/nenadkrdzavac/visualization_python_project/blob/main/sparql-results/q9-sankey.csv"

df = pd.read_csv(url, sep=" ")

print(df)

colors = {
    "apple": "#f71b1b",
    "blueberry": "#1b7ef7",
    "banana": "#f3f71b",
    "lime": "#12e23f",
    "orange": "#f78c1b"
}

sankey(
    left=df["source"], right=df["target"],
    leftWeight= df["revenue"], rightWeight=df["revenue"],
    aspect=20, fontsize=20
)
