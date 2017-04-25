#!/usr/bin/env python3

import mistune


def parse_markdown(filename):
    
    """ Takes a .md file and returns a parsed version in HTML.

    Parses a markdown file using mistune, returns a string which 
    contains the parsed information in HTML.

    Args: 
        filename: the file to be parse, must be a .md file.

    Returns: 
        Variable which contains the parsed markdown as HTML.

    """


    with open(filename, mode="r", encoding="utf8") as f:
        file_md = [lines for lines in f]
        file_string = " ".join(file_md)
        markdown = mistune.markdown(file_string)
    
    return markdown


