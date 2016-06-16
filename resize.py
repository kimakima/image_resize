#coding:utf-8
import sys
import os
import glob
from PIL import Image

LONG_SIDE = 640

argvs = sys.argv
if 2 <= len(argvs):
	st_src_img_filename = argvs[1]
else:
	sys.exit()

st_fn, st_ext = os.path.splitext(st_src_img_filename)
st_dst_img_filename = st_fn + 's' + st_ext

image = Image.open(st_src_img_filename);
#print image.__class__
image.thumbnail((LONG_SIDE,LONG_SIDE), Image.ANTIALIAS)
image.save(st_dst_img_filename, 'JPEG', quality=80, optimize=True)
print st_src_img_filename + '\t->\t' + st_dst_img_filename

print glob.glob('./*.JPG')
