# Import necessary modules/ libraries
import os
from pathlib import Path
import logging

# Configuring logging settings
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Logging a welcome message
logging.info("Hello all, welcome!")

# List of files to be processed
list_of_files = [
    "src/__init__.py", 
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "app.py"
]

# Iterating over each file in the list
for filepath in list_of_files:
    # converting filepath to a path object
    filepath = Path(filepath)
    # splitting the filepath into directory and filename
    filedir, filename = os.path.split(filepath)
    # printing the directory and filename
    print(filedir, filename)

# Checking if the file's directory is not empty
    if filedir!="":
        # creating directory if it doesn't exist
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory {filedir} for the files {filename}")
    
    # Checking if the file doesn't exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        # creating an empty file if it doesn't exist or is empty
        with open(filepath, "w") as f:
            pass
            # logging the creation of empty file
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")