#!/usr/bin/env python3

import os
import shutil


def setup_template_dirs(destination=None):
    """ Copies template directories to output folder for deployment.

    Copies the folders plus contents inside the template directory so 
    that the generated website has the relevant folders and scripts 
    needed to function.

    Args: 
        destination: the output folder, defaults to a dir called output

    """

    if destination is None:
        destination = "output"

    try:
        os.mkdir(destination)
    except OSError:
        print(destination + " already exists, can't create!")

    for root, dirs, files in os.walk("template"):
        for folder in dirs:
            # try:
            #   os.makedirs(os.path.join(destination, folder))

            #except FileExistsError:
                #print("Can't make path, already exists!")

            source = os.path.join(root,folder)
            output = os.path.join(destination, folder)
            try:
                shutil.copytree(source, output)
            except OSError:
                "Can't copy to output, template folders already exist"

    print(destination + " has finished.")


def setup_project_dirs(src=None, dest=None):
    """ Creates project directories from walking through content folder 
    and creating the same name directories.
    
    Walks through the content folder, takes the name of each project 
    folder and creates the same folder in the output directory. Also 
    creates the image folder in each project folder, set up for 
    resized photos.
    
    Args:
        src: the folder to search for project directories
        dest: the output folder for the new directories
    
    """
    
    if src is None:
        src = "content"
        
    if dest is None:
        dest = "output"
    
    folders = []
    
    for items in os.listdir(src):
        if os.path.isdir(os.path.join(src, items)):
            folders.append(items)
    
    print("Found folders: {}".format(folders))
    
    for folder in folders:
        if not os.path.exists(os.path.join(dest, folder)):
            os.mkdir(os.path.join(dest, folder))
            os.mkdir(os.path.join(dest, folder, "images"))
            print("Created folder: {}".format(folder))
        else:
            print("Skipped folder {}, already exists!".format(folder))
    

def create_blog_folder(blog_dir=None):
    """ Creates blog folder in output folder 
    
    Args: 
        blog_dir: set this to be the blog post output folder
        
    """
    
    if blog_dir is None:
        blog_dir = "output/blog"

    try:
        os.mkdir(blog_dir)
    except OSError:
        print("blog folder already exists, can't create!")
