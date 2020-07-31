# Name: Anderson Chauphan
# run_k_means.py is the program used to run a k_means filter on an image
from image_utils import *
from k_means import *


def create_image(image, file_name, means, new_assignments):
    """Function that creates an image from a means and assignments list from a k_means algorithm

    :param image: the original list tuples representing the r,g,b value of each pixel
    :param means: a k-sized list containing tuples of the avg. r,g,b values of pixels assigned to that cluster
    :param new_assignments: list of lists containing the exact cluster assignment for each pixel
    :return: None
    """
    new_image = image
    for x in range(get_width_height(image)[0]):
        for y in range(get_width_height(image)[1]):
            new_image[x][y] = means[new_assignments[x][y]]
    save_ppm(file_name, new_image)


if __name__ == "__main__":
    """Takes in input from the user which is the file-name of the ppm image, along
    with k amount of colors wanting to be representing by the final result
    
    When k_means() is finished running returned the expected values, create_image() is called
    to formulate and output an image.
    """
    input_image = input("Image file-name:> ")
    try:
        file = open(input_image, 'r').readlines()
    except (FileNotFoundError, IOError):
        print("Warning: File not found.")

    k = int(input("k amount of colors: > "))
    file_name = input("Output file name:>")
    image = read_ppm("input_images/" + input_image)
    means, assignments = k_means(image, k)
    create_image(image, file_name, means, assignments)
