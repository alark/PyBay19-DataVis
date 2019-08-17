import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd


labels = ['NBC', 'ABC', 'CBS', 'FOX']
sizes = [35, 30, 35, 10]



obj2 = pd.Series(sizes, index=labels)
obj2.name = "sizes"
obj2.index.name = "labels"

print(obj2)


sns.set_style("darkgrid")
# plt.plot(np.cumsum(np.random.randn(1000,1)))
nyc_chart = sns.lineplot(data=obj2).set_title('TV Viewership Share')


plt.show()