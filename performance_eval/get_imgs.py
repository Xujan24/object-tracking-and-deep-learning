import os


def get_imgs(dir):
    data_dir = '../dataset/OTB/'

    imgDir = os.path.join(data_dir, dir, 'img')

    filenames = os.listdir(imgDir)
    filenames.sort()



    imgs = [0] * len(filenames)


    for i in range(0,len(filenames)):
        imgs[i] = os.path.join(imgDir, filenames[i])

    return(imgs)
