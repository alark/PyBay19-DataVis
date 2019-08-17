import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
import seaborn as sns
sns.set(style="whitegrid")

x = np.linspace(0, 10, 50)
dy = 0.8
y = np.sin(x) + dy * np.random.randn(50)

# plt.errorbar(x, y, yerr=dy, fmt='.k');

sns.set(style="whitegrid")
tips = sns.load_dataset("tips")

# ax = sns.barplot(x="day", y="tip", data=tips, capsize=.2)

plt.show()


plt.errorbar(x="day", y="tip", yerr=0.2, fmt='o', color='black',
             ecolor='lightgray', elinewidth=3, capsize=0);



plt.show()