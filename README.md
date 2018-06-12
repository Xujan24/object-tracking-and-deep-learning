# Object Tracking and Deep Learning
This repo contains the code and results used to evaluate the performance of the visual object tracking algorithm.

## Instructions:
1. Download the MDNet source code available at: [here](https://github.com/liulj13/pyMDNet-VOT2OTB).
2. Unzip the file in a directory
3. download the performance_eval folder from this repo and extract it inside the root of the MDNet directory.
4. Download the OTB dataset and save it in the dataset directory.

## Usage:
First, run the pre-trained MDNet tracker using

`cd tracking` <br />
`python run_tracker.py -s DragonBaby [-d (display fig)] [-f (save fig)]`

To create a video from the image sequences, go inside the performance_eval directory and run the command:

`python generateVideo.py -d [Sequence Name] -c [value for the size of the frame counter] -f [frame per second]`

To generate the Average overlap Score (AOS) and the success plot run

`python performance_eval.py`

**Note: to generate the report create a text file containing the name of all sequences and save it as `seq_list.txt`**

`@InProceedings{nam2016mdnet,`<br />
`author = {Nam, Hyeonseob and Han, Bohyung},`<br />
`title = {Learning Multi-Domain Convolutional Neural Networks for Visual Tracking},`<br />
`booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},`<br />
`month = {June},`<br />
`year = {2016}`<br />
`}`
