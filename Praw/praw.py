from os.path import isfile
import praw
import pandas as pd 
from time import sleep

#get credentiald from DEFAULT instance of praw.ini
reddit = praw.Reddit()
