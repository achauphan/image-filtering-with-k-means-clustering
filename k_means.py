# Name: Anderson Chauphan
# Module containing the necessary functions to perform
# a k_means cluster of k colors of an image and output
# the final clusters.
from image_utils import *
import math


def k_means(image, k):
    """Creates k clusters of pixels in image that most resembles
    the cluster with the same color. Outputs an image based on the
    color of the assigned cluster that each pixel was assigned to
    as final_output.ppm.

    :param image: the original list tuples representing the r,g,b value of each pixel
    :param k: specified amount of clusters
    :return: a 2-length tuple with first element being the final means list and the second
            element being the final assignments list.
    """
    means = random_means(k)
    assignments = update_assignments(image, means)
    new_assignments = []
    while assignments != new_assignments:
        assignments = new_assignments
        means = update_means(image, assignments, k)
        new_assignments = update_assignments(image, means)

    return means, new_assignments


def update_means(image, assignments, k):
    """For each cluster, compute the average color of all the pixels assigned to that cluster.

    :param image: the original list tuples representing the r,g,b value of each pixel
    :param assignments: list of lists containing the exact cluster assignment for each pixel
    :param k: specified amount of clusters
    :return: k-sized list of tuples containing the newly averaged r,g,b for each cluster
    """
    means = []
    for mean_index in range(k):
        assigned_colors = []
        for x in range(len(assignments)):
            for y in range(len(assignments[x])):
                if assignments[x][y] == mean_index:
                    assigned_colors.append(image[x][y])
        if len(assigned_colors) >= 1:
            means.append(average_color(assigned_colors))
        else:
            means.append(BLACK)
    return means


def update_assignments(image, means):
    """For each pixel, reassign that pixel to the cluster that is most similar to the color of the pixel

    :param image: the original list tuples representing the r,g,b value of each pixel
    :param means: k-sized list of tuples containing the average color for each cluster
    :return: list of lists containing cluster assignments for each pixel in image
    """
    assignments = []
    for x in range(get_width_height(image)[0]):
        row = []
        for y in range(get_width_height(image)[1]):
            closest_mean = 0
            for i in range(len(means)):
                if distance(means[i], image[x][y]) < distance(means[closest_mean], image[x][y]):
                    closest_mean = i
            row.append(closest_mean)
        assignments.append(row)
    return assignments


def random_means(k):
    """Generates a list of tuples containing random r,g,b values

    :param k: specified amount of clusters to generate a random r,g,b color for
    :return: k-sized list of tuples of random r,g,b colors
    """
    means = []
    for i in range(k):
        means.append(random_color())
    return means


def distance(color1, color2):
    """Computes a value for the "distance/similarity" color1 is to color2

    :param color1: a list containing r,g,b values of the color
    :param color2: a list containing r,g,b values of the color
    :return: a value used to assess the distance/similarity color1 is to color2
    """
    return math.sqrt((color1[0] - color2[0]) * (color1[0] - color2[0])
                     + (color1[1] - color2[1]) * (color1[1] - color2[1])
                     + (color1[2] - color2[2]) * (color1[2] - color2[2]))


def average_color(colors):
    """Computes the average color from a given list of colors

    :param colors: a list of tuples containing r,g,b values for each color
    :return: a tuple containing the r,g,b color value of the average color in list colors
    """
    r, g, b = 0, 0, 0
    for color in colors:
        r += color[0]
        g += color[1]
        b += color[2]
    return r // len(colors), g // len(colors), b // len(colors)
