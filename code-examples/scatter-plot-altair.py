import altair as alt
from vega_datasets import data
import pandas as pd

# source = data.iris()
#
# chart = alt.Chart(source).mark_circle().encode(
# 	alt.X('sepalLength', scale=alt.Scale(zero=False)),
# 	alt.Y('sepalWidth', scale=alt.Scale(zero=False, padding=1)),
# 	color='species',
# 	size='petalWidth',
# 	tooltip=['species']
# )
#
# chart.save('chart.html')

# source = data.iris()
source = pd.read_csv('data/warriors-roster-18-19.csv')

source2 = pd.read_csv('data/Warriors-reg-season-2019.csv')



chart = alt.Chart(source2).mark_circle().encode(
	alt.X('3PM', scale=alt.Scale(zero=False)),
	alt.Y('3PA', scale=alt.Scale(zero=False, padding=1)),
	# color='Pos',
	size='FG%',
	tooltip=['Player', 'FG%']
)

chart.save('html/warriors-chart.html')