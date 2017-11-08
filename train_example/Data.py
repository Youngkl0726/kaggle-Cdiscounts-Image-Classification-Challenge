import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import io
import bson                       # this is installed with the pymongo package
import matplotlib.pyplot as plt
from skimage.data import imread   # or, whatever image library you prefer
import multiprocessing as mp      # will come in handy due to the size of the data
from os import path
# Simple data processing

# data = bson.decode_file_iter(open('train_example.bson', 'rb'))
#
# prod_to_category = dict()
#
# index = 0
# fig = plt.figure()
# save_dir = './train_example/'
# for c, d in enumerate(data):
#     # if index>10:
#     #     break
#     # index += 1
#     plt.pause(0.001)
#     plt.clf()
#     product_id = d['_id']
#     category_id = d['category_id'] # This won't be in Test data
#     print product_id, category_id
#     file_name = '{:0}.png'.format(product_id)
#     print file_name
#     # save_train_dir = path.join(save_dir, file_name)
#     prod_to_category[product_id] = category_id
#     for e, pic in enumerate(d['imgs']):
#         picture = imread(io.BytesIO(pic['picture']))
#         plt.imsave(file_name, picture)
#         # plt.imshow(picture)
#
#         # do something with the picture, etc
# # plt.show()
# prod_to_category = pd.DataFrame.from_dict(prod_to_category, orient='index')
# prod_to_category.index.name = '_id'
# prod_to_category.rename(columns={0: 'category_id'}, inplace=True)
# prod_to_category.to_csv('train_example.csv', header=False)
# print prod_to_category




NCORE = 8

prod_to_category = mp.Manager().dict()  # note the difference


def process(q, iolock):
    while True:
        d = q.get()
        if d is None:
            break
        product_id = d['_id']
        category_id = d['category_id']
        prod_to_category[product_id] = category_id
        file_name = '{:0}.png'.format(product_id)
        print file_name, category_id
        for e, pic in enumerate(d['imgs']):
            picture = imread(io.BytesIO(pic['picture']))
            plt.imsave(file_name, picture)
            # do something with the picture, etc


q = mp.Queue(maxsize=NCORE)
iolock = mp.Lock()
pool = mp.Pool(NCORE, initializer=process, initargs=(q, iolock))

# process the file

data = bson.decode_file_iter(open('train_example.bson', 'rb'))
for c, d in enumerate(data):
    q.put(d)  # blocks until q below its max size

# tell workers we're done

for _ in range(NCORE):
    q.put(None)
pool.close()
pool.join()

# convert back to normal dictionary
prod_to_category = dict(prod_to_category)

prod_to_category = pd.DataFrame.from_dict(prod_to_category, orient='index')
prod_to_category.index.name = '_id'
prod_to_category.rename(columns={0: 'category_id'}, inplace=True)
prod_to_category.to_csv('train_example.csv', header=False)
# print prod_to_category
