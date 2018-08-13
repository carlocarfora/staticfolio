#!/usr/bin/env python3

import os
import time

def print_hr(char="*", n=60):
    """ Prints a horizontal line and a line break in the console"""
    
    print("\n" + char * n)


def last_build(path):
    """ Takes a path as input, checks that it exists and the last time 
    it was modified. Returns time in D-M-Y format.
    
    """
    if os.path.isdir(path):
        epoch_secs = os.path.getmtime(path)
        time_tuple = time.localtime(epoch_secs)

        return ("{2}-{1}-{0}".format(
             time_tuple[0], time_tuple[1], time_tuple[2]))
    else:
        no_dir = "No output dir found"
        return no_dir

#~ 
#~ print("Reading template file")
#~ about = readfile.read_files("template/page.html")
#~ about_tags = readfile.replace_all(about, settings.tags)
#~ about_links = readfile.replace_all(about_tags, settings.links)
#~ 
#~ print("Converting markdown to html")
#~ about_md = parsemd.parse_markdown("content/contact.md")
#~ about_dic = {"(%_page_content_%)": about_md }
#~ 
#~ print("Building/Writing file")
#~ about_built = readfile.replace_all(about_links, about_dic)
#~ readfile.write_file(about_built, " ", "output/resources.html")
