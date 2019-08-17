import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import pprint

import matplotlib.ticker as plticker

years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
yearsFmt = mdates.DateFormatter('%Y')

fig, ax = plt.subplots(figsize=(18,6))

source = pd.read_csv('data/AAPL-1.csv')

# source = source.head(200)
# t = source.Date.str.split('-',2)[0].tolist()
t = source.Date.str.split('-',2)

source['Year'], source['Month'], source['Day'] = source['Date'].str.split('-', 3).str

datemin = datetime.date(int(source.Year.min()), 1, 1)
datemax = datetime.date(int(source.Year.max()) + 1, 1, 1)

# datemin and datemax work - limits are set limits is not working
# axes = plt.gca()
# axes.set_xlim(datemin, datemax)
# axes.set_xlim([xmin,xmax])
# axes.set_ylim([ymin,ymax])


# ax = plt.axes()
ax.xaxis.set_major_locator(plticker.MultipleLocator(350))
# ax.xaxis.set_minor_locator(plticker.MultipleLocator(1))

# loc = plticker.MultipleLocator(base=1.0) # this locator puts ticks at regular intervals
# loc = plticker.AutoDateLocator()
# ax.xaxis.set_major_locator(loc)

t = source['Date']
s = source['Volume']
line, = ax.plot(t, s, lw=1)

# adf.scaled[1./24] = '%H:%M'  # set the < 1d scale to H:M
# adf.scaled[1.0] = '%Y-%m-%d' # set the > 1d < 1m scale to Y-m-d
# adf.scaled[30.] = '%Y-%m' # set the > 1m < 1Y scale to Y-m
# adf.scaled[365.] = '%Y' # set the > 1y scale to Y



ax.annotate('First iPhone announced', xy=("2007-01-09", 837324600), xytext=("2007-10-10", 847324600),
            xycoords='data', arrowprops=dict(facecolor='black', shrink=0.1),
            )


ax.annotate('Verizon announces iPhone 4 ', xy=("2011-01-18", 470249500), xytext=("2011-09-19", 570249500),
            xycoords='data', arrowprops=dict(facecolor='black', shrink=0.1),
            )


# ax.set_ylim(0,2)

# plt.locator_params(axis='y', nbins=10)
# plt.locator_params(axis='x', nbins=10)

plt.show()
