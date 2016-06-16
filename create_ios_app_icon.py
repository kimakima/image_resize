#coding:utf-8
import sys
import os
import glob
from PIL import Image
import csv

#ary_icon_dim = [[57,57,"icon-57.png"],[114,114,"icon-57@2x.png"],[120,120,"icon-60@2x.png"]]
ary_icon_dim = []
#for i in range(len(ary_icon_dim)):
#	print ary_icon_dim[i][0]
#	print ary_icon_dim[i][1]
#	print ary_icon_dim[i][2]

fr = open('icon_info.csv','r')
reader = csv.reader(fr)
for row in reader:
	ary_icon_dim.append(row)

print ary_icon_dim

argvs = sys.argv
if 2 <= len(argvs):
	st_src_img_filename = argvs[1]
else:
	sys.exit()

st_fn, st_ext = os.path.splitext(st_src_img_filename)

for i in range(len(ary_icon_dim)):
	image = Image.open(st_src_img_filename);

	icon_width = int(ary_icon_dim[i][0])
	icon_height = int(ary_icon_dim[i][1])
	st_dst_img_filename = ary_icon_dim[i][2]

	image.thumbnail((icon_width,icon_height), Image.ANTIALIAS)
	image.save(st_dst_img_filename, 'PNG', quality=80, optimize=True)
	print st_src_img_filename + '\t->\t' + st_dst_img_filename

print glob.glob('./*.png')

