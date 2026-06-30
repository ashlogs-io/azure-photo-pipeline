import os
import glob
from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener() #this is the plugin so Pillow understand HEIF/HEIC
COMPRESSED_IMAGE_SIZE = (400, 400) #the dimension of the compressed image I want
VALID_IMAGE_EXTENSION = ['.jpg', '.jpeg', '.heif', '.heic', '.png']

#check if compressedimages directory exists or not
if not os.path.exists("./compressedimages"):
    #if compressedimages directory does not exist, create it
    os.makedirs("./compressedimages")

for img in glob.iglob('./rawimages/**/*.*', recursive=True):

    file_extension = os.path.splitext(img)
        
    if file_extension[1].lower() not in VALID_IMAGE_EXTENSION:
        continue
    
    image = Image.open(img)
    image.thumbnail(COMPRESSED_IMAGE_SIZE)
    #filename = os.path.basename(img) #strips off any folder path and gives just the filename, eg, if 'img' is 'subfolder/testimg.jpeg', this gives 'testimg.jpeg'
    input_path = os.path.relpath(img, './rawimages')
    filename = input_path.replace('/', '_')
    output_path = os.path.join("./compressedimages", filename) # glues the output folder and that filename together properly eg, './compressedimages/testimg.jpeg'
    image.save(output_path) #saves images to output folder
    