import glob
import os

collected =""


for img in glob.iglob('./compressedimages/*'):
    # print(img)
    line = f'<img src="{img}">'
    collected += line
#print(collected) 
full_html = f"<html><body>{collected}</body></html>"
#print(full_html) 

#opens(or creates a file called 'gallery.html', if it doesn't exist, in write mode)
# 'with ... as f:" this is the pattern that handles "properly saving and closing the file" automatically
with open('gallery.html', 'w') as f:
    f.write(full_html)


