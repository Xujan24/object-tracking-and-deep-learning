# Object Tracking and Deep Learning
This repo contains the code and results used to evaluate the performance of the visual object tracking algorithm.

## Instructions:
1. Download the MDNet source code available at: [here](https://github.com/liulj13/pyMDNet-VOT2OTB).
2. Unzip the file in a directory
3. download the performance_eval folder from this repo and extract it inside the root of the MDNet directory.
4. Download the OTB dataset and save it in the dataset directory.

## Usage:
To create a video from the image sequences, go inside the performance_eval directory and run the command:
`python generateVideo.py -d [Sequence Name] -c [value for the size of the frame counter] -f [frame per second]`
