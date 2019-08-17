import altair as alt
from vega_datasets import data
import pandas as pd


counties = alt.topo_feature(data.us_10m.url, 'counties')

source = pd.read_csv('data/2016_US_County_Level_Presidential_Results.csv')
# source = data.unemployment.url



chart = alt.Chart(counties).mark_geoshape().encode(
    color='votes_dem:Q'
).transform_lookup(
    lookup= 'id',
    from_=alt.LookupData(source, 'combined_fips', ['votes_dem'])
).project(
    type='albersUsa'
).properties(
    width=500,
    height=300
).interactive()

chart.save('html/choropleth.html')