import os
from PIL import Image

def create_crop(path, width, height):
    """ Generates thumbs from given path and dimensions.

    Creates thumbnails from input path, dimensions are cropped from
    the middle so a portion of the image is always the thumbnail.

    Args:
        path: The path which contains images to be thumbnailed.
        width: Thumbnail width.
        height: Thumbnail height.

    Returns:
        Creates a folder called OUTPUT which contains the cropped
        thumbnails, with the same name as the input.


    """

    if not os.path.exists("OUTPUT"):
        print("Making folder")
        os.mkdir("OUTPUT")
        
    for root, dirs, files in os.walk(path):
            for f in files:
                im = Image.open(root + "\\" + f)
                outfile = os.path.join("OUTPUT", f)
                img_size = (
                    int(im.size[0]/2),
                    int(im.size[1]/2),
                    int(im.size[0]/2+width),
                    int(im.size[1]/2+height))
                cropped = im.crop(img_size)
                #print(cropped)
                cropped.save(outfile)


def create_thumb(src="content", dest="output"):
    """ Generates thumbnail from the designated thumb image.

    Creates thumbnails from specific image, thumbnail keeps the aspect
    ratio of the original image and outputs the image to the parent
    folder it is in.

    Args:
        path: The path which contains images to be thumbnailed.
        width: Thumbnail width.
        height: Thumbnail height.

    Returns:
        Creates thumbnails and put the saved thumbs in the destination 
        folder.


    """
    
    thumbs = []
    
    for root, dirs, files in os.walk(src):
        for f in files:
            if "thumb.jpg" in f:
                thumbs.append(os.path.join(root,f))
                
    print("Found thumbnails in {}".format(thumbs))

    for img in thumbs:
        im = Image.open(img)
        outfile = img.replace(src, dest)
        im.thumbnail((310, 310), Image.ANTIALIAS)
        im.save(outfile, quality=75, optimize=True)
        print("Saved thumbnail {0} to {1}".format(img, outfile))


def resize_images(src="content", dest="output"):
    """ Resizes image to required size for website, user can specify 
    size and destination.
    
    """
    
    images = []
    
    for root, dirs, files in os.walk(src):
        if "images" in root:
            for f in files:
                images.append(os.path.join(root, f))
                
    
    for img in images:
        outfile = img.replace(src, dest)
        im = Image.open(img)
        im.thumbnail((960, 960), Image.ANTIALIAS)
        im.save(outfile, quality=80, optimize=True)
        print("Resized and saved {0} to {1}".format(img, outfile))
        
