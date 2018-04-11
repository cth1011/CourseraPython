import matplotlib.pyplot as plt
import numpy as np

'''
plt.figure()
plt.subplot(1,2,1)

linear_data = np.array([1,2,3,4,5,6,7,8])

plt.plot(linear_data, '-o')

exponential_data = linear_data**2

plt.subplot(1,2,2)
plt.plot(exponential_data, '-o')

plt.subplot(1,2,1)
plt.plot(exponential_data,'-x')


#New and Better Figure
plt.figure()
ax1 = plt.subplot(1,2,1)
plt.plot(linear_data,'-o')
ax2 = plt.subplot(1,2,2, sharey=ax1)
plt.plot(exponential_data,'-x')


plt.figure()
# the right hand side is equivalent shorthand syntax
plt.subplot(1,2,1) == plt.subplot(121)
#create a 3x3 grid of subplots
fig, ((ax1,ax2,ax3), (ax4,ax5,ax6),(ax7,ax8,ax9)) = plt.subplots(3,3, sharex=True,sharey=True)

ax5.plot(linear_data, '-')
#set inside tick labels to visible
for ax in plt.gcf().get_axes():
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_visible(True)
#Redraw
plt.gcf().canvas.draw()


#Histograms

#create  2x2 grid of axis subplots
fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2, sharex=True)
axs = [ax1,ax2,ax3,ax4]

#draw n = 10, 100, 1000, and 10000 samples from the normal distribution
for n in range(0,len(axs)):
    sample_size = 10**(n+1)
    sample =np.random.normal(loc=0.0,scale=1.0,size=sample_size)
    axs[n].hist(sample,bins=100)
    axs[n].set_title( 'n={}'.format(sample_size))
    
plt.figure()
Y = np.random.normal(loc=0.0, scale=1.0, size=10000)
X = np.random.random(size=10000)
plt.scatter(X,Y)
# use gridspec to partition the figure into subplots
import matplotlib.gridspec as gridspec

plt.figure()
gspec = gridspec.GridSpec(3,3)

top_histogram = plt.subplot(gspec[0,1:])
side_histogram = plt.subplot(gspec[1:,0])
lower_right = plt.subplot(gspec[1:,1:])
Y = np.random.normal(loc=0.0, scale=1.0, size=10000)
X = np.random.random(size=10000)
lower_right.scatter(X,Y)
top_histogram.hist(X,bins=100)
s=side_histogram.hist(Y,bins=100,orientation='horizontal')

# clear the histograms and plot normed histograms
top_histogram.clear()
top_histogram.hist(X, bins=100, normed=True)
side_histogram.clear()
side_histogram.hist(Y, bins=100, orientation='horizontal', normed=True)
# flip the side histogram's x axis
side_histogram.invert_xaxis()

# change axes limits
for ax in [top_histogram, lower_right]:
    ax.set_xlim(0, 1)
for ax in [side_histogram, lower_right]:
    ax.set_ylim(-5, 5)

#Box Plots
import pandas as pd
normal_sample = np.random.normal(loc=0.0, scale=1.0, size=10000)
random_sample = np.random.random(size = 10000)
gamma_sample = np.random.gamma(2, size=10000)

df = pd.DataFrame({'normal':normal_sample,
                   'random':random_sample,
                   'gamma': gamma_sample})
    
df.describe()

plt.figure()
# create a boxplot of the normal data, assign the output to a variable to supress output
_ = plt.boxplot(df['normal'], whis='range')
# clear the current figure
plt.clf()

# plot boxplots for all three of df's colmns
_ = plt.boxplot([df['normal'],df['random'],df['gamma']], whis='range')

plt.figure()
_ = plt.hist(df['gamma'], bins=100)

import mpl_toolkits.axes_grid1.inset_locator as mpl_il

plt.figure()
plt.boxplot([df['normal'], df['random'], df['gamma']], whis='range')
#overlay axis on top of another
ax2 =mpl_il.inset_axes(plt.gca(),width='60%',height='40%',loc=2)
ax2. hist(df['gamma'],bins=100)
ax2.margins(x=0.5)

#switch the y axis ticks for ax2 to the right side
ax2.yaxis.tick_right()

#if 'whis' argument isn't passed, boxplot defaults to showing 1.5*interquartile (IQR) whiskers with outliers
plt.figure()
_ = plt.boxplot([ df['normal'], df['random'], df['gamma']])

    '''
    # Heat Maps
plt.figure()

Y= np.random.normal(loc=0.0, scale=1.0, size=10000)
X = np. random.random(size=10000)
_ = plt.hist2d(X,Y,bins=100)

plt.figure()
_ = plt.hist2d(X,Y, bins=25)
#add a colorbar legend
plt.colorbar()
