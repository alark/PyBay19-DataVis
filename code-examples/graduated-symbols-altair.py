import altair as alt
from vega_datasets import data

import pandas as pd

# airports = data.airports()
states = alt.topo_feature(data.us_10m.url, feature='states')

source = pd.read_csv('data/us-lat-lon-population.csv')


# US states background
background = alt.Chart(states).mark_geoshape(
    fill='lightgray',
    stroke='white'
).properties(
    width=700,
    height=600
).project('albersUsa')

# airport positions on background
points = alt.Chart(source).mark_circle(
    color='steelblue'
).encode(
    size=  'Population:Q',
    longitude='Longitude:Q',
    latitude='Latitude:Q',
    tooltip=['State' , 'Population']
)

chart = background + points

chart.save('html/graduated-symbols.html')