# Imagine Color Filtering using k-means Clustering Algorithm

(**Project 1 for CSCI1913**) This project aimed to have to student write a k-means clustering algorithm and to implement the algorithm by doing image color filtering.

## The Project

### k-means Clustering Algorithm
Given a k amount of clusters and a set of data, seperate the set of data into whichever k cluster the data point is closest to. 

The starting value of each k cluster is determined randomly. Once the first cycle of categorizing data points into their respective clusters is complete, the value of each k cluster is re-evaluated to the average value of all the data points belonging to that cluster. The loop of categorizing data points and re-evaluating k cluster values is repeated until the value of the clusters do not change. Once the values of k clusters stop changing, then you have your k clusters containing their closet representing data points.

### Image Filtering using k-means Clustering
Image color filtering is implemented by having k representing the amount of colors to be had from the original image (big numbers take longer to filter). Each cluster will then have a random r,g,b value assigned and each pixel position of the image is assigned to the cluster that is the closes to in r,g,b value. This is repeated until the cluster values do not change. After the cluster values are finalized and each cluster contains the pixel positions of that most represent the cluster color value, the imagine is then reconstructed with each pixel representing the color value of the cluster it was assigned to.

### Filtering Progression Example of k = 4
![x](https://i.imgur.com/HJJ0Hgj.png) ![x](https://media0.giphy.com/media/Mb4qsTqblEdZKv7Y3r/giphy.gif)

Top image is the input image as a ppm file (ppm was easy to build and read). Bottom gif is a visualization of each pixel's corresponding k cluster color after every loop until the clusters are finalized.

## What I learned
- Given a description of an algorithm and scenario, interpret and attempt to write a *solution.
- Manage deadlines
- An idea to how advanced modern day image filter is and how complex facial filter must be.
