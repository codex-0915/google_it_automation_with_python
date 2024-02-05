#!/usr/bin/env python

# Create a directory and move a file from one directory to another
# using Pathlib.

from pathlib import Path

# Check to see if the "test1" subdirectory exists. If not, create it:
dest_dir = Path("./test1/")
# Construct source path:
src_file = Path("./sample_data/test-file.txt")

if not dest_dir.exists() or not Path.exists(src_file):
    dest_dir.mkdir()
    # Create the txt file if file doesn't exist
    with open(src_file, "w") as file:
        file.write("Sample file to be moved from one directory to another")
    file.close()

# Construct destination paths:
dest_file = dest_dir / "test-file.txt"

# Move the file from its original location to the destination:
src_file.rename(dest_file)

# Read the file content from the new location
file = open(dest_file)
print(file.read())
file.close()
