import os
import caffe
import numpy as np
import cv2
import fnmatch

export PYTHONPATH=/mnt/lustre/yangkunlin/sensenet/example/core/python
caffe.set_mode_gpu()
model_def = '/home/yangkunlin/storage/kaggle/normal_model/normal_deploy.prototxt'
model_pretrained = '/home/yangkunlin/storage/kaggle/normal_model/normal_kaggel_iter_300000.caffemodel'
net = caffe.Classifier(model_def, model_pretrained)

img_dir='/home/yangkunlin/storage/kaggle/test_data/'
filelist = []
filenames = fnmatch.filter(os.listdir(img_dir), '*.png')
total_num = len(filenames)
out = np.empty([total_num, 2], dtype=object)
for idx, fn in enumerate(filenames):
    out[idx, 0] = fn
    fullfilename=os.path.join(imgdir,fn)
    filelist.append(fullfilename)

batch_size = 60
iters = total_num / batch_size
mod = np.mod(num, batch_size)
averageImg = np.array([103.939,116.779,123.68])

if mod != 0:
    iter += 1
for i in xrange(iters):
    batch_data = np.zeros((batch_size, 3, 96, 96))
    print "Processing %d/%d" % (i, iters)
    idx0 = i * batch_size
    if i == (iters - 1) and mod != 0:
        idx1 = i * batch_size + mod
    else:
        idx1 = (i + 1) * batch_size
    ind = 0
    for j in xrange(idx0,idx1):
        img = cv2.imread(filelist[j])
        if img.shape[2] == 1:
            tmp = cv2.resize(img,(96,96))
            image[:,:,0] = tmp
            image[:,:,1] = tmp
            image[:,:,2] = tmp
        elif img.shape[2] == 3:
            tmp = cv2.resize(img,(96,96))
            image = tmp[:,:,::-1]
        else:
            print('channel must be 1 for grayscale or 3 for rgb')
            raise ValueError
        image = image - averageImg
        image = image.transpose((2,0,1))
        batch_data[ind] = iamge
        ind += 1
    batch_prob = net.forward_all(data=batch_data, blobs=['prob'])['prob']
    ind = 0
    for j in xrange(idx0, idx1):
        tmpp = batch_prob[ind]
        out[j,1] = tmpp.argsort()[-1]
        ind += 1


np.save('out.npy', out)
print "Done!"  