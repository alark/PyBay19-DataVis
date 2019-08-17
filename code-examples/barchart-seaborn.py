import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# sns.set(style="white", context="talk")
sns.set_style("darkgrid")

rs = np.random.RandomState(8)

# Set up the matplotlib figure
# f, ax3 = plt.subplots(1, 1, figsize=(7, 5), sharex=True)
f, ax3 = plt.subplots()

# Generate some sequential data
x = np.array(list("ABCDEFGHIJ"))
y1 = np.arange(1, 11)
# sns.barplot(x=x, y=y1, palette="rocket", ax=ax1)
# ax1.axhline(0, color="k", clip_on=False)
# ax1.set_ylabel("Sequential")
#
# # Center the data to make it diverging
# y2 = y1 - 5.5
# sns.barplot(x=x, y=y2, palette="vlag", ax=ax2)
# ax2.axhline(0, color="k", clip_on=False)
# ax2.set_ylabel("Diverging")

labels = ['NBC', 'ABC', 'CBS', 'FOX']
sizes = [35, 30, 35, 10]

# Randomly reorder the data to make it qualitative
# y3 = rs.choice(sizes, len(sizes), replace=False)
sns.barplot(x=labels, y=sizes, palette="deep", ax=ax3)
ax3.axhline(0, color="k", clip_on=False)


plt.annotate('actual group', xy=(sizes+0.2,sizes), xytext=(x+0.3, 300),
             arrowprops=dict(facecolor='black', shrink=0.05, headwidth=20, width=7))

# ax3.set_ylabel("Qualitative")


# Finalize the plot
sns.despine(bottom=True)
plt.setp(f.axes, yticks=[])
plt.tight_layout(h_pad=2)

# Configure the y-axis
plt.yticks(np.arange(0, max(sizes)+1, 5))


plt.show()