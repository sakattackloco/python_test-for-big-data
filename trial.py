import pandas as pd
import numpy as np
import matplotlib as mat
import matplotlib.pyplot as plt

#read all data from the csv files
course_info = pd.read_csv("course_information.csv")
course_threads = pd.read_csv("course_threads.csv")
course_posts = pd.read_csv("course_posts.csv")

#concetrate all threads and posts of the lesson 'Big data analysis'
threads = course_threads.loc[(course_threads["course_id"]=="bigdata-edu-001")]
posts = course_posts.loc[(course_posts["course_id"]=="bigdata-edu-001")& (course_posts["user_type"]=="Student")]

#concetrate all unique users and forums
user_ids = posts['user_id'].unique()
forum_ids = threads['og_forum_id'].unique()

#for each forum id count his number of threads (no comments)
for specific_forum_id in forum_ids:
    specific_threads = threads.loc[(threads["og_forum_id"]==specific_forum_id)]
    print(specific_threads['thread_id'].describe())
