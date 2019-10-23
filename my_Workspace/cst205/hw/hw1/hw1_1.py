# Authors: Clyde Sumagang and Roy Morla
# Date: 9/22/ 2019
# Course: CST 205
# Abstract: This program will count the rgb values in a matrix and store them into a dictionary
#           with 4 bins based on color and intensity
import pickle

file = open('image_matrix', 'rb')
data = pickle.load(file)

def task1(data):

    #dictionary to hold levels respective rgb intensity values
    histo = {
            'red': [0,0,0,0],
            'green': [0,0,0,0],
            'blue': [0,0,0,0]
    }

    #for loop to iterate through length of the outer list
    for x in range(len(data)):
        #changes what values list comprehension statements use
        real_data = data[x]

        #list comprehension to split up rgb data from tuples
        red_data = [x[0] for x in real_data]
        green_data = [x[1] for x in real_data]
        blue_data = [x[2] for x in real_data]

        #logic for red data to increment dictionary list values
        for i in red_data:
            if (i <= 63):
                histo['red'][0] += 1
            elif (i <= 127 and i >= 64):
                histo['red'][1] += 1
            elif (i <= 191 and i >= 128):
                histo['red'][2] += 1
            elif (i <= 255 and i >= 192):
                histo['red'][3] += 1

        #logic for green data to increment dictionary list values
        for i in green_data:
            if (i <= 63):
                histo['green'][0] += 1
            elif (i <= 127 and i >= 64):
                histo['green'][1] += 1
            elif (i <= 191 and i >= 128):
                histo['green'][2] += 1
            elif (i <= 255 and i >= 192):
                histo['green'][3] += 1

        #logic for blue data to increment dictionary list values
        for i in blue_data:
            if (i <= 63):
                histo['blue'][0] += 1
            elif (i <= 127 and i > 64):
                histo['blue'][1] += 1
            elif (i <= 191 and i >= 128):
                histo['blue'][2] += 1
            elif (i <= 255 and i >= 192):
                histo['blue'][3] += 1

    return histo

print (task1(data))
