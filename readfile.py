#!/usr/bin/env python3

import os
import settings
import ast
import math

def read_sidebar(filename):
    """ Reads a text file and evaluates it as a python dict.
    
    Takes a file, reads it line by line and evaluates it so that the 
    dictionary it holds can be initialised.
    
    """
    
    with open(filename, "r") as f:
        s = f.read()
        sidebar = ast.literal_eval(s)
    
    return sidebar


def read_files(filename):
    """ Reads a file line by line and commits it to a variable.

    Takes a file and reads it line by line, commiting each line to
    memory. Returns the variable as a tuple with each line as an item.

    Args:
        filename: the location of the file to be read.

    Returns:
        Returns the file as a tuple with each line stored as a value.

    """

    with open(filename, mode="r", encoding="utf-8") as f:
        file_memory = [lines for lines in f]

    return file_memory


def replace_all(text, dic, filtered=None):
    """ Searches for specific keys in TEXT and replaces them with the
    value from DIC.

    Uses a dictionary to find specific keys and replace them with the
    relevant value pair. DIC holds the key:value look up information.

    Args:
        text: is an iterable data set that holds the text search through
        dic: holds the dictionary that contains the key:value to search
        filtered: ensures that the list is initialised empty each time

    """
    
    if filtered is None:
        filtered = []

    for line in text:
        for key, value in dic.items():
            line = line.replace(key, value)
        filtered.append(line)

    return filtered


def write_file(file_to_write, separator, file_out="output"):
    """ Takes a list/tupule, joins using a custom separator and writes 
    it to disk with a custom name.
    
    Takes a list or tuple, and writes it to a text file using the join 
    command, with the separator as custom input.

    Args:
        file_to_write: the list/tuple to write
        separator: the join separator
        file_out: the name of the file to write out

    """
    
    with open(file_out, mode="w", encoding="utf-8") as f:
        f.write(separator.join(file_to_write))


def portfolio_grid(src="output"):
    """ Scans for thumbnails, creates thumbnail path and generates the
    correct html for the portfolio grid as well as the a href link in a 
    dictionary.
    
    Args:
        src: the root path for the function to walk through and search
   
    """
    
    thumbs = []
    html = []

    for root, dirs, files in os.walk(src):
        for f in files:
            if "thumb.jpg" in f:
                thumbs.append(os.path.join(root,f))

    thumbs.sort(reverse=True)
    
    no_of_thumbs = len(thumbs)
    thumbs_per_col = math.ceil(no_of_thumbs/3)

    for index, item in enumerate(thumbs):
        item_split = (item.split("/"))
        item_slice = item_split[1][3:]
        alt_text = item_slice.replace("_", " ")
        
        project_name = item_split[1] + ".html"
        
        image_src = (
            os.path.join(item_split[1], item_split[2])
        )

        html.append(
            """
                <div class='col-xs-12 col-sm-6 col-md-4 col-lg-3 masonry-item'> 
                  <div class='box-masonry'><a href='{0}' title='' class='box-masonry-image with-hover-overlay'><img src='{1}' alt='{2}' class='img-responsive'></a>
                    <div class='box-masonry-hover-text-header'> 
                      <h4> <a href='{0}'>{2}</a></h4>
                    </div>
                  </div>
                </div>
            """.format(
                project_name, image_src, alt_text
            )
        )

        if index == no_of_thumbs:
            html.append("")
        
        
    html_joined = " ".join(html)
    html_dic = {"(%_portfolio_grid_%)": html_joined}

    return html_dic

#~ def insert_img(src="content"):
    #~ for root, dirs, files in os.walk(src):
        #~ print(dirs)

def get_project_dirs(path="content"):
    """ Returns project directory names from content folder.
    
    Scans given path one level deep for folders, and returns all 
    the folder names as a list of folder names.
    
    Args:
        path: path to search, defaults to "content"
    
    
    """
    projects = []

    for items in os.listdir(path):
        if os.path.isdir(os.path.join(path, items)):
            projects.append(items)
    
    return projects


def get_project_imgs(projects):
    """ Returns a tuple of image paths from the given directory.
    
    
    
    """
    
    image_path = []

    for root, dirs, files in os.walk("output/{}".format(proj)):
        if "images" and proj in root:
            print(root)
            print(files)
            
