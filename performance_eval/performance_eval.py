#
# filename: performance_eval.py
#
# discription: A python script to evaluate the performance of MDNet
#
# author: Santosh Purja Pun
#

import numpy as np
import json
import matplotlib.pyplot as plt

def overlap_ratio(rect1, rect2):

    left = np.maximum(rect1[0], rect2[0])
    right = np.minimum(rect1[0]+rect1[2], rect2[0]+rect2[2])
    top = np.maximum(rect1[1], rect2[1])
    bottom = np.minimum(rect1[1]+rect1[3], rect2[1]+rect2[3])

    intersect = np.maximum(0,right - left) * np.maximum(0,bottom - top)
    union = rect1[2]*rect1[3] + rect2[2]*rect2[3] - intersect
    iou = np.clip(intersect / union, 0, 1)
    return iou


# get the list of the names of all the sequences used;
seqs_list = 'seq_list.txt'

seqs = ''
with open(seqs_list, 'r') as seqs:
    seqs = seqs.read().replace('\n',',')

seqs = seqs.split(',')

n = len(seqs)

overlap = np.zeros(shape=(n,1))
fps = np.zeros(shape=(n,1))

for i in range(0,n):
    seq = seqs[i]

    # get the ground truth and predicted bounding box location
    gt = np.loadtxt('../dataset/OTB/'+seq+'/groundtruth_rect.txt', dtype= 'int', delimiter=',')
    bb_result = json.load(open('../result/'+seq+'/result.json', 'r'))
    bb_mdnet = bb_result['res']
    fps[i] = bb_result['fps']

    seq_length = len(gt)

    op = np.zeros(shape=(seq_length,1))

    for j in range(0,seq_length):
         op[j] = overlap_ratio(gt[j], bb_mdnet[j])

    overlap[i] = np.mean(op)

    # write the result in a file
    res = seq + '\t\t' + str(overlap[i]) + '\t\t' + str(fps[i]) + '\n'

    with open('./output/eval.txt', 'a+') as file:
        if i == 0:
            file.write('Sequence Title \t\t AOS \t\t FPS \n')
        file.write(res)

# success plot
overlap_threshold = [0, 0.2, 0.4, 0.8, 1.0]
y = []

for i in range(0, len(overlap_threshold)):
    y.append(sum(x > overlap_threshold[i] for x in overlap)/len(overlap))

plt.plot(overlap_threshold, y)
plt.xlabel('Overlap Threshold')
plt.ylabel('Success Rate')
plt.title('Success plot of OPE')

plt.savefig('./output/success_plot.png')