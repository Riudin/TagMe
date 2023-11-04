### Useful Libraries ###
# installs
! pip install langdetect
! pip install contractions

# Libraries for general purpose
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Text cleaning
import re
import string
import emoji
import nltk
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.corpus import stopwords

# Data preprocessing
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler
from langdetect import detect, LangDetectException
import contractions
from nltk.tokenize import word_tokenize

# Pytorch
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader, RandomSampler, SequentialSampler

# Transformers library for BERT
import transformers
from transformers import BertModel
from transformers import BertTokenizer
from transformers import AdamW, get_linear_schedule_with_warmup
from sklearn.metrics import classification_report, confusion_matrix

import time

### Preparation ###

# Set seed for reproducibility
import random
seed_value = 2042
random.seed(seed_value)
np.random.seed(seed_value)
torch.manual_seed(seed_value)
torch.cuda.manual_seed_all(seed_value)

# Set style for plots
sns.set_style("whitegrid")
sns.despine()
plt.style.use("seaborn-whitegrid")
plt.rc("figure", autolayout=True)
plt.rc("axes", labelweight="bold", labelsize="large", titleweight="bold", titlepad=10)

# Define stop words for text cleaning
stop_words = set(stopwords.words('english'))

# Initialize lemmatizer for text cleaning
lemmatizer = WordNetLemmatizer()


### Data Cleaning ###

# Clean emojis from text
# Remove punctuations, stopwords, links, mentions and new line characters
# Clean hashtags at the end of the sentence, and keep those in the middle of the sentence by removing just the # symbol
# Filter special characters such as & and $ present in some words
# Remove multiple spaces
# Function to check if the text is in English, and return an empty string if it's not
# Expand contractions
# Remove numbers
# Lemmatize words
# Remove short words
# Replace elongated words with their base form
# Remove repeated punctuation
# Remove extra whitespace
# Remove spaces at the beginning and end of the text
# Function to call all the cleaning functions in the correct order
def clean_text(text):
    text = strip_emoji(text)
    text = expand_contractions(text)
    text = filter_non_english(text)
    text = strip_all_entities(text)
    text = clean_hashtags(text)
    text = filter_chars(text)
    text = remove_mult_spaces(text)
    text = remove_numbers(text)
    text = lemmatize(text)
    text = remove_short_words(text)
    text = replace_elongated_words(text)
    text = remove_repeated_punctuation(text)
    text = remove_extra_whitespace(text)
    text = remove_url_shorteners(text)
    text = remove_spaces_texts(text)
    text = ' '.join(text.split())  # Remove multiple spaces between words
    return text

#check duplicates after cleaning
#drop duplicates


### Tekenization ###

### Modeling ###

### Training ###

### Prediction ###

### Examples ###