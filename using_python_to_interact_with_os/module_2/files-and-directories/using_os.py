#!/usr/bin/env python

# Create a directory and move a file from one directory to another
# using low-level OS functions.

import os

# Check to see if a directory named "test1" exists under the current
# directory. If not, create it:
dest_dir = os.path.join(os.getcwd(), "test1")
# Construct source path:
src_file = os.path.join(os.getcwd(), "sample_data", "test-file.txt")

if not os.path.exists(dest_dir) and not os.path.exists(src_file):
    os.mkdir(dest_dir)
    # Create the txt file if file doesn't exist
    with open(src_file, "w") as file:
        file.write("Sample file to be moved from one directory to another")
    file.close()


# Construct destination paths:
dest_file = os.path.join(os.getcwd(), "test1", "test-file.txt")


# Move the file from its original location to the destination:
os.rename(src_file, dest_file)

# Read the file content from the new location
file = open(dest_file)
print(file.read())