#coding:utf-8
import sys
import os
import glob
import time
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS

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

src_img_width = image.size[0]
src_img_height = image.size[1]
if src_img_width < src_img_height:
	src_img_long_side = src_img_height
else:
	src_img_long_side = src_img_width

dst_img_long_side = src_img_long_side/2

def get_exif(image):
	try:
		exif = image._getexif()
	except AttributeError:
		return {}

	exif_table = {}
	for tag_id, value in exif.items():
		tag = TAGS.get(tag_id, tag_id)
		exif_table[tag] = value

	return exif_table

get_exif(image)

dic_exif = get_exif(image)
print dic_exif
print dic_exif['DateTimeOriginal']
exif_datetimeoriginal = datetime.strptime(dic_exif['DateTimeOriginal'], '%Y:%m:%d %H:%M:%S')

image.thumbnail((dst_img_long_side,dst_img_long_side), Image.ANTIALIAS)
image.save(st_dst_img_filename, 'JPEG', quality=80, optimize=True)

os.utime(st_dst_img_filename,(int(time.mktime(exif_datetimeoriginal.timetuple())), int(time.mktime(exif_datetimeoriginal.timetuple()))))

print st_src_img_filename + '\t->\t' + st_dst_img_filename

print glob.glob('./*.JPG')
