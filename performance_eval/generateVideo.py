#
# filename: generateVideo.py
#
# discription: A python script to combine the sequence of images into a video using openCV.
#
# author: Santosh Purja Pun
#

import json
import numpy as np
import cv2 as cv
from optparse import OptionParser

from get_imgs import *

#defining options
parser = OptionParser()
parser.add_option('-d', '--dir', default='', type='string',\
                  help='input the directory containing image sequences')

parser.add_option('-c','--cex', default=0.7, type='float', help='input the font size')

parser.add_option('-f', '--fps', type='int', default = 20, help='input the frame rate i.e. frame-per-second')
(options, args) = parser.parse_args()
assert(options.dir != '')

imgPaths = get_imgs(options.dir) # get the path for the image sequences;

# read all the images
imgs=[0] * len(imgPaths)
for i in range(0, len(imgPaths)):
    imgs[i] = cv.imread(imgPaths[i])


# get the predicted bounding box
result_path = '../result/'+options.dir+'/result.json'
# get the ground truth annotations for the target object
gt_bb = '../dataset/OTB/'+options.dir+'/groundtruth_rect.txt'

bbox = json.load(open(result_path, 'r'))['res']
gt = np.loadtxt(gt_bb, delimiter=',', dtype=int)
h, w, layers = imgs[1].shape # set the height and width for the video corresponding tho the size of img seq.

# set the directory for saving output file
save_dir = './output/'+options.dir+'.avi'


for i in range(1,len(imgs)):
    rect = bbox[i]
    gt_rect = gt[i]
    text = '#' + str(i)
    cv.rectangle(imgs[i], (int(gt_rect[0]), int(gt_rect[1])), (int(gt_rect[0] + gt_rect[2]), int(gt_rect[1] + gt_rect[3])), (0, 0, 255),2)
    cv.rectangle(imgs[i],(int(rect[0]),int(rect[1])),(int(rect[0]+rect[2]),int(rect[1]+rect[3])),(0,255,0),2)
    cv.putText(imgs[i], text , (0,20), cv.FONT_HERSHEY_SIMPLEX, options.cex, (255,255,255), 2, cv.LINE_AA)

video = cv.VideoWriter(save_dir,-1, options.fps, (w, h))

for i in range(0, len(imgPaths)):
    video.write(imgs[i])

cv.destroyAllWindows()
video.release()



