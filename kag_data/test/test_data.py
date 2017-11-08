import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import io
import bson                       # this is installed with the pymongo package
import matplotlib.pyplot as plt
from skimage.data import imread   # or, whatever image library you prefer
import multiprocessing as mp      # will come in handy due to the size of the data
from os import path

data = bson.decode_file_iter(open('test.bson', 'rb'))
prod_to_category = dict()
index = 0
save_dir = './test_data/'
for c, d in enumerate(data):
    # if index>10:
    #     break
    print index
    # plt.pause(0.001)
    # plt.clf()
    product_id = d['_id']
    # category_id = d['category_id'] # This won't be in Test data
    # print product_id
    file_name = '{:0>11d}.png'.format(product_id)
    # print file_name
    # save_train_dir = path.join(save_dir, file_name)
    prod_to_category[index] = product_id
    for e, pic in enumerate(d['imgs']):
        picture = imread(io.BytesIO(pic['picture']))
        plt.imsave(file_name, picture)
        # plt.imshow(picture)
    index += 1
    # if index == 10:
    #     break
        # do something with the picture, etc
prod_to_category = pd.DataFrame.from_dict(prod_to_category, orient='index')
prod_to_category.index.name = '_id'
prod_to_category.rename(columns={0: 'name_id'}, inplace=True)
prod_to_category.to_csv('/mnt/lustre/yangkunlin/kaggle/test.csv', header=False)
print "over"
# print prod_to_category
