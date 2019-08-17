import altair as alt
from vega_datasets import data

import pandas as pd


# source = data.cars()
source = pd.read_csv('data/Warriors-reg-season-2019-updated.csv')

# chart = alt.Chart(source).mark_circle(size=90).encode(
#     alt.X(alt.repeat("column"), type='quantitative'),
#     alt.Y(alt.repeat("row"), type='quantitative'),
#     color='Pos',
# 	tooltip = ['Player', 'FG%']
# ).properties(
#     width=150,
#     height=150
# ).repeat(
#     row=['FT%', 'TO', 'AST', 'STL', 'Age', 'MIN'],
#     column=['3P%', 'FG%', 'BLK', 'GP', 'REB', 'PTS']
# ).interactive()

chart = alt.Chart(source).mark_circle(size=90).encode(
    alt.X(alt.repeat("column"), type='quantitative'),
    alt.Y(alt.repeat("row"), type='quantitative'),
    color='Pos',
	tooltip = ['Player', 'Age', 'Weight']
).properties(
    width=150,
    height=150
).repeat(
    row=['Age', 'PTS' ],
    column=['Weight', 'Exp' ]
).interactive()


chart.save('html/warriors-simple-splom-chart.html')