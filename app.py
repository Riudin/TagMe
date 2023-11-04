# import libraries
import random
import json                         # to work with json files
import pandas as pd                 # dataframe to visualize data (mainly for testing and confirming if the code works and importing json as dataframes)
# import numpy as np                  # fundamental package for scientific computing. includes advanced mathematical methods like n-dimensional arrays and vectorization
# import matplotlib.pyplot as plt     # package for plotting data as graphs


# define data
path = 'TestData/'
tag_file = 'exampletags.json'
text_file = 'exampletexts.json'
output_file = 'output.json'


# define tags
tags = [
    "ableism", "classsism", "homophobia", "misogyny", "racism", "sexism", "transphobia",
    "violence", "animal-cruelty", "sexual-assault", "abuse", "child-abuse", "abduction", "kidnapping",
    "pregnancy", "miscarriages", "childbirth", "abortion",
    "dissection", "blood",
    "dying", "death", "animal-death",
    "mental-illness", "suicide", "eating-disorders", "fat-phobia", "body-hatred", "self-harm",
    "incest", "underage", "pornographic-content"
]


# function to write results in a new json file
def write_json(output_data, filename=path+output_file):
    with open(filename, "w") as f:
        json.dump(output_data, f, indent=4)


# read tags and texts from json file
tags_df = pd.read_json(path + tag_file)
text_df = pd.read_json(path + text_file)


# print one of the example tags and texts (for testing)
# print(tags_df['tag'][4])
# print(text_df)


# define output data
output_data = []

for t in text_df['work_id']:
    # get random tags from the list for testing
    # tag1 = tags_df['tag'][random.randrange(start=6)]
    # tag2 = tags_df['tag'][random.randrange(start=6)]
    tag1 = tags[random.randrange(start=31)]
    tag2 = tags[random.randrange(start=31)]
    output_data.append({"work_id": t, "labels": [tag1, tag2]})


# write output data in json file
write_json(output_data)
