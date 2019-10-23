# Authors: Clyde Sumagang and Roy Morla
# Date: 9/22/ 2019
# Course: CST 205
# Abstract: This program will count the rgb values in a matrix and incriment the value in their respective index and list.

import pickle
import hw1_hist_plotter as hp


def task2(data):
    rgb_list = [0] * 3  # This creates a list containing 3 lists

    rgb_list[0] = [0] * 256     # This 256 indexes in the first list to 0
    rgb_list[1] = [0] * 256     # This 256 indexes in the second list to 0
    rgb_list[2] = [0] * 256     # This 256 indexes in the third list to 0
    for x in data:      # This gets the individual lists in the matrix
        for i in x:     # This then gets each individual tupple in the list
            rgb_list[0][i[0]] += 1     # This will add 1 to the the red list for whatever value the red is at
            rgb_list[1][i[1]] += 1     # This will add 1 to the the green list for whatever value the green is at
            rgb_list[2][i[2]] += 1     # This will add 1 to the the blue list for whatever value the blue is at
    return rgb_list


file = open('image_matrix', 'rb')     # We open the image_matrix in rb mode

data = pickle.load(file)    # We then load the contents into variable data

hp.hist_plotter(task2(data))    # We pass the data through the task2 function

file.close()    # We then close the image_matrix file
