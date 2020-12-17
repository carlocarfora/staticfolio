#!/usr/bin/env python3

import sys
import os
import time
import mistune
import imaging
import directories
import readfile
import settings
import parsemd
import staticfunc


last_build_date = staticfunc.last_build("./output")
print(last_build_date)

staticfunc.print_hr()

print(' '.join([
      "Welcome to staticfolio, last time a build of your site was \n"
      "generated was: "
      , last_build_date ]))

staticfunc.print_hr()

build_bool = input("Generate new build? Y/N ")

print(build_bool)

if build_bool.upper() != "Y":
    print("Exiting staticfolio now!")
    sys.exit(0)
print("*")


staticfunc.print_hr()
print("Setting up Directories")
staticfunc.print_hr()

directories.setup_template_dirs("output")
directories.setup_project_dirs()

staticfunc.print_hr()
print("Resizing Images")
staticfunc.print_hr()

imaging.create_thumb()
imaging.resize_images()


staticfunc.print_hr()
print("Building Index")
staticfunc.print_hr()

print("Reading template file")
index = readfile.read_files("template/index.html")
index_tags = readfile.replace_all(index, settings.tags)
index_links = readfile.replace_all(index_tags, settings.links)

print("Building portfolio grid")
index_grid = readfile.portfolio_grid()
index_built = readfile.replace_all(index_links, index_grid)

print("Writing file")
readfile.write_file(index_built, " ", "output/index.html")


staticfunc.print_hr()
print("Building About")
staticfunc.print_hr()

print("Reading template file")
about = readfile.read_files("template/page.html")
about_tags = readfile.replace_all(about, settings.tags)
about_links = readfile.replace_all(about_tags, settings.links)

print("Converting markdown to html")
about_md = parsemd.parse_markdown("content/about.md")
about_dic = {"(%_page_content_%)": about_md }

print("Building/Writing file")
about_built = readfile.replace_all(about_links, about_dic)
readfile.write_file(about_built, " ", "output/about.html")


staticfunc.print_hr()
print("Building Code")
staticfunc.print_hr()

print("Reading template file")
resources = readfile.read_files("template/page.html")
resources_tags = readfile.replace_all(resources, settings.tags)
resources_links = readfile.replace_all(resources_tags, settings.links)

print("Converting markdown to html")
resources_md = parsemd.parse_markdown("content/code.md")
resources_dic = {"(%_page_content_%)": resources_md }

print("Building/Writing file")
resources_built = readfile.replace_all(resources_links, resources_dic)
readfile.write_file(resources_built, " ", "output/code.html")


staticfunc.print_hr()
print("Building Contact")
staticfunc.print_hr()

print("Reading template file")
contact = readfile.read_files("template/page.html")
contact_tags = readfile.replace_all(contact, settings.tags)
contact_links = readfile.replace_all(contact_tags, settings.links)

print("Converting markdown to html")
contact_md = parsemd.parse_markdown("content/contact.md")
contact_dic = {"(%_page_content_%)": contact_md }

print("Building/Writing file")
contact_built = readfile.replace_all(contact_links, contact_dic)
readfile.write_file(contact_built, " ", "output/contact.html")


staticfunc.print_hr()
print("Building Project Pages")
staticfunc.print_hr()

print("Getting all projects")
projects = readfile.get_project_dirs()

for proj in projects:

    print("Reading template files")
    project_page = readfile.read_files("template/project.html")
    project_tags = readfile.replace_all(project_page, settings.tags)
    project_links = readfile.replace_all(project_tags, settings.links)

    print("Building image paths")
    image_path = []

    for root, dirs, files in os.walk("output/{}".format(proj)):
        if "images" in root:
            for f in files:
                img_path_t = os.path.join(proj, "images")
                img_path = os.path.join(img_path_t, f)
                #print(img_path)
                #~ (head, tail) = os.path.split(root)
                #~ while len(tail)
                #~ print(head)
                #~ print(tail)
                image_path.append(
                    "<img class='img-responsive' src='{}'/><br />".format(img_path))
            
    image_dic = {"(%_project_images_%)": "\n".join(image_path)}
    project_images = readfile.replace_all(project_links, image_dic)

    print("Converting markdown to html")
    project_md = (
        parsemd.parse_markdown("content/{}/content.md".format(proj))
    )
    project_dic = {"(%_page_content_%)": project_md}
    
    # print("Adding sidebar information")
    # project_info = (
    #     readfile.read_sidebar("content/{}/sidecontent.txt".format(proj))
    # )
    # project_sidebar = readfile.replace_all(project_images, project_info)

    print("Building/Writing file")
    project_built = readfile.replace_all(project_images, project_dic )
    readfile.write_file(
        project_built, " ", "output/{p}.html".format(p=proj))



staticfunc.print_hr()
print("Building Blog Posts")
staticfunc.print_hr()

print("Fetch blog post directory")
blog_post_dir = readfile.get_project_dirs("blog")

print("Create blog post directory")
directories.create_blog_folder()
directories.setup_project_dirs("blog", "output/blog")

print("Resizing Images")
imaging.resize_images("blog", "output/blog")

print("Creating blog posts")

for post in blog_post_dir:
    
    print("Reading template file")
    blog_post = readfile.read_files("template/blog_post.html")
    blog_tags = readfile.replace_all(blog_post, settings.tags)
    blog_links = readfile.replace_all(blog_tags, settings.links)

    print("Converting markdown to html")
    blog_md = (
        parsemd.parse_markdown("blog/{0}/{0}.md".format(post))
    )
    blog_dic = {"(%_blog_post_%)": blog_md}
    
    print("Adding post title and date")
    post_split = post.split("_")
    post_date = post_split[0]
    post_title = post_split[1].replace("-", " ")
    
    date_dic = {"(%_blog_date_%)": post_date}
    title_dic = {"(%_blog_title_%)": post_title}
    
    print("Building/Writing post:" + post)
    blog_date = readfile.replace_all(blog_links, date_dic)
    blog_title = readfile.replace_all(blog_date, title_dic)
    blog_built = readfile.replace_all(blog_title, blog_dic)
    readfile.write_file(
        blog_built, " ", "output/blog/{0}/{0}.html".format(post))
        
print("Creating blog listing")

blog_listing = []

for post in blog_post_dir:
    
    post_split = post.split("_")
    post_date = post_split[0]
    post_title = post_split[1].replace("-", " ")
    
    blog_listing.append(
        '<p><a href="blog/{2}/{2}.html">{0}</a> - Posted on {1} </p>'
        .format(post_title, post_date, post)
    )

blog_listing.sort(reverse=True)
listing_as_str = "".join(blog_listing)
post_dic = {"(%_blog_listing_%)": listing_as_str}

print("Reading blog list template")
blog_list_template = readfile.read_files("template/blog_listing.html")
list_tags = readfile.replace_all(blog_list_template, settings.tags)
list_links = readfile.replace_all(list_tags, settings.links)

print("Writing blog listing page")
post_page = readfile.replace_all(list_links, post_dic)
readfile.write_file(
    post_page, " ", "output/blog.html")
