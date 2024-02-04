#!/usr/bin/env/ python

import os
import datetime

print(os.path.getsize("spider.txt"))
#This code will provide the file size
print(os.path.getmtime("spider.txt"))
#This code will provide a timestamp for the file
timestamp = os.path.getmtime("spider.txt")
print(datetime.datetime.fromtimestamp(timestamp))
#This code will provide the date and time for the file in an easy too understand format
print(os.path.abspath("spider.txt"))
#This code takes the file name and turns it into an absolute path
