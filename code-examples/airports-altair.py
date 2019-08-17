import altair as alt
from vega_datasets import data

airports = data.airports()
states = alt.topo_feature(data.us_10m.url, feature='states')

# US states background
background = alt.Chart(states).mark_geoshape(
    fill='lightgray',
    stroke='white'
).properties(
    width=900,
    height=600
).project('albersUsa')

# airport positions on background
points = alt.Chart(airports).mark_circle(
    size=50,
    color='steelblue'
).encode(
    longitude='longitude:Q',
    latitude='latitude:Q',
    tooltip=['name', 'city', 'state']
)

chart = background + points
#
chart.save('html/airports.html')