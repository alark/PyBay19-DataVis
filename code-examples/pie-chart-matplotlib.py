import matplotlib.pyplot as plt

# Pie chart
labels = ['NBC', 'ABC', 'CBS', 'FOX']
sizes = [35, 30, 35, 10]

# only "explode" the 2nd slice (i.e. 'Hogs')
# explode = (0.0, 0.0, 0, 0)

fig1, ax1 = plt.subplots()
# ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
# 		shadow=False, startangle=0)

ax1.pie(sizes, shadow=False, startangle=0)


# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')

plt.tight_layout()
plt.show()