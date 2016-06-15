#coding:utf-8
import sys
from PIL import Image

argvs = sys.argv
if 3 <= len(argvs):
	st_src_img_filename = argvs[1]
	st_dst_img_filename = argvs[2]
else:
	sys.exit()

image = Image.open(st_image_filename);
print image.__class__
image.thumbnail((480,480), Image.ANTIALIAS)
image.save(st_dst_img_filename, 'JPEG', quality=80, optimize=True)

