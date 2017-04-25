Overview
========
Staticfolio is a static site generator which is focused on being minimal yet 
functional for the end user. It frees up the need to rely on a bloated 
platform for simply doing one thing which is to display artwork.

The main features of staticfolio are it's minimal design, easy to use system 
and it's been written to do only what it's designed to do and nothing more. 

Staticfolio will be a **command line** program so there'll be no GUI. It's meant to be a first serious project in Python so it'll be evolving as my understanding of the language improves.

This spec is a work in progress, it'll be edited and written as the project goes on.

Features
========
Features of staticfolio include:

- Minimal front-end design
- Modern browser support
- Auto project page creation
- Auto image resizing
- Twitter feed
- Add as many projects as you wish
- Bloat free

Usage
=====
Staticfolio will read a directory which adheres to the programs directory structure. It will take all the information from the directories and build an output directory which is the website. This output directory can be uploaded to the web server and it should be a fully functional website.
The website can be rebuilt over and over when updates are needed and this new output can be uploaded to the users server.
The website will be a portfolio with various project thumbnails that can be clicked on and they will lead to a project page with more information.

Details
=======

Common/Shared Things
--------------------

All pages will show the following items: 

- Page Title
- Logo
- Tag line
- Twitter feed
- Vimeo, Twitter, Flickr and LinkedIn icons
- Footer
- Navigation

Navigation
----------
The navigation on the left will initially be hardcoded, so the projects link will look for **projects.html** and contact will look for **contact.html**. The blog link will be read from the **settings.py** file and inject the relevant link.

At some point this may change to a dynamic navigation so additional pages can be added.

Index Page
----------
The index page will have an isotope grid that dynamically resizes like those cool jquery mason grids. Thumbnails will be resized automatically via staticfolio and be picked up from project folders. Project names will pop up when rolled over the thumbnail (I think).

Project Page
------------
The project pages will have to be built from folders, each project will be housed in a folder and need to have some files in it to work: 

- **text file** which has the content written in markdown, this will be parsed and added to the website
- **images folder** which has all the projects images, the images inside this folder will be resized to fit the template properly so any size image can be dropped in
- **thumbnail file**, which can be any size and this will also get resized to fit the grid properly

Contact Page
------------
The contact page will read a markdown file and parse the content into it. Any optional images can be read from a folder.

Folder Structures
=================

The basic folder structure will be as follows, this can and probably will change as the project progresses:

    Root
        + Template
        + Output
        + Projects
            + project_01
                + images
                    - image_1.jpg
                    - image_2.jpg
                - content.md
                - thumb.jpg
        - settings.py
        + lib
        + doc
        
Basic Program Outline
=====================

This is a basic outline of using the program and from this I can see roughly how the project needs to be structured and what needs to be made.

- Run program
- Display last date site was rebuilt
- Ask if site needs rebuilding
- If No, just exit but if yes
- Build output directory folders
- Read project folders
- Create project thumbnails
- Resize project images
- Create index page
- Create project pages
- Create Contact page




> Written with [StackEdit](https://stackedit.io/).
