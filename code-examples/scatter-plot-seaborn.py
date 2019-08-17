import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd



sns.set()


# iris = sns.load_dataset("iris")
# ax = sns.scatterplot(x=iris.sepal_length, y=iris.sepal_width,
#                      hue=iris.species,  size=iris.petal_length)
#
# plt.show()

df = pd.read_csv('data/warriors-roster-18-19.csv')

df2 = pd.read_csv('data/Warriors-reg-season-2019.csv')


# ax = sns.scatterplot(x=df.Age, y=df.Weight, size=df2.GP, hue=df2.PTS, style=df.Pos)
ax = sns.scatterplot(x=df.Age, y=df.Weight, size=df2.PTS, hue=df.Pos)

# print(df)

def label_point(x, y, val, ax):
    a = pd.concat({'x': x, 'y': y, 'val': val}, axis=1)
    for i, point in a.iterrows():
        ax.text(point['x']+.05, point['y'], str(point['val']))

label_point(df.Age, df.Weight, df.Player, plt.gca())

plt.show()