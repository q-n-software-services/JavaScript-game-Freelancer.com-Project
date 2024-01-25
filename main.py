import random
import statistics
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


fhand = open('data.txt')
dataX = []
dataY = []
for line in fhand:
    dataX.append(line.split(",")[0].strip())
    dataY.append(line.split(",")[1].strip())

dataX = [float(item) for item in dataX]
dataY = [float(item) for item in dataY]

# *****   Clustering Algorithm     *****

df = pd.DataFrame({
    'x': dataX,
    'y': dataY
})

# Color Scheme for the Scatter Plot
colmap = {1: 'r', 2: 'g', 3: 'b', 4: 'y'}

# *****   K-Means Clustering Algorithm begins here     *****
np.random.seed(200)

# Number of clusters to be created
k = 4

# Generating Random points as centroids for starting the process
centroids = {
    i+1: [np.random.randint(-2, 2), np.random.randint(-2, 2)]
    for i in range(k)
}


# Assignment Stage, assignment of data-points to the respective cluster using the K-Means formula/Method

def assignment(df, centroids):
    for i in centroids.keys():
        # sqrt((x1 - x2)^2 + (y1 - y2)^2)
        df['distance_from_{}'.format(i)] = (
            np.sqrt(
                (df['x'] - centroids[i][0]) ** 2
                + (df['y'] - centroids[i][1]) ** 2
            )
        )

    centroid_distance_cols = ['distance_from_{}'.format(i) for i in centroids.keys()]
    df['closest'] = df.loc[:, centroid_distance_cols].idxmin(axis=1)
    df['closest'] = df['closest'].map(lambda x: int(x.lstrip('distance_from_')))
    df['color'] = df['closest'].map(lambda x: colmap[x])

    return df


df = assignment(df, centroids)
print(df)

# *****     Update Stage     *****

import copy

# Making a new dataset of previous centroids
old_centroids = copy.deepcopy(centroids)


def update(k):
    for i in centroids.keys():
        centroids[i][0] = np.mean(df[df['closest'] == i]['x'])
        centroids[i][1] = np.mean(df[df['closest'] == i]['y'])
    return k


centroids = update(centroids)

# Repeat Assignment Stage

df = assignment(df, centroids)


# Continue until all assigned categories don't change anymore

while True:
    closest_centroids = df['closest'].copy(deep=True)
    centroids = update(centroids)
    df = assignment(df, centroids)
    if closest_centroids.equals(df['closest']):
        break

# Generating the Scatter Plot to see the Data-points and Respective Clusters
fig = plt.figure(figsize=(5, 5))
plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])

plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.show()



scatter_groups = [[], [], [], []]
x_points = [[], [], [], []]
y_points = [[], [], [], []]
for row in df.iloc:
    scatter_groups[int(row['closest'])-1].append((row['x'], row['y']))
    x_points[int(row['closest'])-1].append(row['x'])
    y_points[int(row['closest'])-1].append(row['y'])


means = []
std_deviation = []

# for a in range(4):
#     # means.append((statistics.mean(x_points[a]), statistics.mean(y_points[a])))
#     std_deviation.append((statistics.pstdev(x_points[a]), statistics.pstdev(y_points[a])))

print("standard deviation")
print(std_deviation)

# Creating a list my_centroid to store the centroid coordinates for further processing
my_centroid = []
# Sorting the coordinates of centroids in ascending order with respect to 2nd value i.e. number of pullups performed by the athlete on daily basis
temp = []

for i in centroids.keys():
    my_centroid.append((centroids[i][0], centroids[i][1]))

for count in range(4):
    for counter in range(4):
        if my_centroid[count][1] < my_centroid[counter][1]:
            temp = my_centroid[counter]
            my_centroid[counter] = my_centroid[count]
            my_centroid[count] = temp

print("Centroids' coordinates are as follows")
for i in range(len(my_centroid)):
    print("Centroid ", i + 1, ":\t", my_centroid[i])

# Coordinates of centroids from our dataset.
centroid1 = [my_centroid[0][0], my_centroid[0][1]]
centroid2 = [my_centroid[1][0], my_centroid[1][1]]
centroid3 = [my_centroid[2][0], my_centroid[2][1]]
centroid4 = [my_centroid[3][0], my_centroid[3][1]]

print()
print()


for count, group in enumerate(scatter_groups):
    dist_list = []
    iteration = []
    RSS = 0.0
    RSS_list = []
    for c, point in enumerate(group):
        distance = np.sqrt((float(point[0]) - float(centroids[count + 1][0])) **2 + (float(point[1]) - float(centroids[count + 1][1])) **2)

        dist_list.append(distance)
        iteration.append(c+1)
        RSS = RSS + (distance ** 2)
        RSS_list.append(RSS)
    plt.scatter(*[iteration, RSS_list], color=colmap[random.randint(1, 4)])
    plt.show()


#####

for a in range(4):
    means.append((statistics.mean(x_points[a]), statistics.mean(y_points[a])))
    std_deviation.append((statistics.pstdev(x_points[a]), statistics.pstdev(y_points[a])))

meansX = []
meansY = []
stdDevX = []
stdDevY = []
for counter in range(4):
    meansX.append(means[counter][0])
    meansY.append(means[counter][1])

    stdDevX.append(std_deviation[counter][0])
    stdDevY.append(std_deviation[counter][1])

# Plotting Histograms for X mean and Y mean

N_points = 100000
n_bins = 20


fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

# We can set the number of bins with the *bins* keyword argument.
axs[0].hist(meansX, bins=n_bins)
axs[1].hist(meansY, bins=n_bins)

plt.show()


# Plotting Histograms for X Standard Deviation and Y Standard Deviation

N_points = 100000
n_bins = 20


fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

# We can set the number of bins with the *bins* keyword argument.
axs[0].hist(stdDevX, bins=n_bins)
axs[1].hist(stdDevY, bins=n_bins)

plt.show()

