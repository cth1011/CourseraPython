import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import numpy as np
import os

directory = './Data'
if not os.path.exists(directory):
    os.makedirs(directory)


fig = Figure()
canvas = FigureCanvasAgg(fig)

ax = fig.add_subplot(111)
ax.plot(3,2,'.')
canvas.print_png(directory+'/test.png')

#=============================================================================
#               Scatterplot
#=============================================================================
x = np.array([1,2,3,4,5,6,7,8])
y=x
plt.figure()

colors = ['green']*(len(x)-1)
colors.append('grey')
plt.scatter(x,y,s=100, c=colors)

zip_generator = zip([1,2,3,4,5], [6,7,8,9,10])
#print(list(zip_generator)) 'Output [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
x,y =zip(*zip_generator) # * is an unsplat operator that unpacks the lists into smaller pices


fig =plt.figure()
plt.scatter(x[:2],y[:2], s=100, c='red', label='Tall students')
plt.scatter(x[2:],y[2:], s=100, c='blue', label='Short Students')
plt.xlabel('The number of times the child kicked a ball')
plt.ylabel('The grade of the student')
plt.title('Relationship between ball kicking and grades')

plt.legend(loc=4, frameon=False, title='Legend')
canvas = FigureCanvasAgg(fig)
canvas.print_png(directory+'/test1.png')



#=============================================================================
#               Line Plots
#=============================================================================

linear_data = np.array(range(1,9))
quadratic_data = linear_data**2

plt.figure()
plt.plot(linear_data, '-o', quadratic_data, '--o')
plt.plot(linear_data*2,'--r')

plt.xlabel('Data')
plt.ylabel('More Data')
plt.title('A sexy title')
plt.legend(['Baseline', 'Competition', 'Us'])
plt.gca().fill_between(range(len(linear_data)),
                    linear_data,linear_data*2,
                    facecolor='blue',
                    alpha=0.25)
import pandas as pd
plt.figure()

observation_dates = np.arange('2017-01-01', '2017-01-09', dtype='datetime64[D]')
observations_dates = list(map(pd.to_datetime, observation_dates))
plt.plot(observation_dates, linear_data, '-o',
         observation_dates, quadratic_data, '-o')

x = plt.gca().xaxis

for item in x.get_ticklabels():
    item.set_rotation(45)
plt.subplots_adjust(bottom=0.25)

ax=plt.gca()
ax.set_xlabel('Date')
ax.set_ylabel('Units')
ax.set_title('Quadratric ($x^2$) vs. Linear ($x$)')

#=============================================================================
#              Bar Charts
#=============================================================================
plt.figure()

xvals = range(len(linear_data))
plt.bar(xvals,linear_data,width=0.3) 
new_xvals = []
for item in xvals:
    new_xvals.append(item+0.3)

plt.bar(new_xvals, quadratic_data,width=0.3, color='red')

from random import randint
linear_err = [randint(0,15) for x in range(len(linear_data))]
plt.bar(xvals,linear_data,width=0.3,yerr=linear_err)

plt.figure()
xvals = range(len(linear_data))
plt.bar(xvals, linear_data, width=0.3, color='b')
plt.bar(xvals, quadratic_data, width=0.3, bottom=linear_data, color='r')

plt.figure()
xvals = range(len(linear_data))
plt.barh(xvals, linear_data, height=0.3, color='b')
plt.barh(xvals, quadratic_data, height=0.3, left=linear_data, color='r')

#=============================================================================
#              Dejunkifying Charts
#=============================================================================
plt.figure()

languages =['Python', 'SQL', 'Java', 'C++', 'JavaScript']
pos = np.arange(len(languages))
popularity = [56, 39, 34, 34, 29]


# soften all labels by turning grey
bars=plt.bar(pos, popularity, align='center', linewidth=0, color='lightslategrey')
bars[0].set_color('#1F77B4')
plt.xticks(pos, languages, alpha=0.8)
plt.ylabel('% Popularity',alpha=0.8)
plt.title('Top 5 Languages for Math & Data \nby % popularity on Stack Overflow',
          alpha=0.8)

# remove all the ticks (both axes), and tick labels on the Y axis
plt.tick_params(top='off', bottom='off', left='off', right='off',
                labelleft='off', labelbottom='on')

# remove the frame of the chart
for spine in plt.gca().spines.values():
    spine.set_visible(False)

# direct label each bar with Y axis values
for bar in bars:
    plt.gca().text(bar.get_x() + bar.get_width()/2, bar.get_height() - 5, str(int(bar.get_height())) + '%', 
                 ha='center', color='w', fontsize=11)

plt.show()