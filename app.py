# import libraries
import json                         # to work with json files
import pandas as pd                 # dataframe to visualize data (mainly for testing and confirming if the code works)
#import numpy as np                  # fundamental package for scientific computing. includes advanced mathematical methods like n-dimensional arrays and vectorization
#import matplotlib.pyplot as plt     # package for plotting data as graphs


# define variables
path = 'TestData/'
tag_file = 'exampletags.json'
text_file = 'exampletexts.json'
output_file = 'output.json'


# function to write results in a new json file
def write_json(output_data, filename=path+output_file):
    with open(filename, "w") as f:
        json.dump(output_data, f, indent=4)


# read tags and texts from json file
tags_df = pd.read_json(path + tag_file)
text_df = pd.read_json(path + text_file)


# print one of the example tags and texts
print(tags_df['Tag'][4])
print(text_df['Text'][2])


# define output data
output_data = ["Bob", "Cindy"]


# write output data in json file
write_json(output_data)
