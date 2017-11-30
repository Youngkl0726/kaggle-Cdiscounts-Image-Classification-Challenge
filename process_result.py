import numpy as np
import csv
# total = 0
# txt_file = open('result.txt', 'wb')
# for i in xrange(36):
#     npy_name = './n1/prob_{:0}.npy'.format(i)
#     print npy_name
#     npy = np.load(npy_name)
#     len = npy.shape[0]
#     # print npy.shape[0]
#     total += npy.shape[0]
#     for j in xrange(len):
#         res = int(npy[j][0])
#         txt_file.write(str(res)+'\n')
#
# print total

def get_id(filename):
    file = open(filename)
    res_line = []
    for i in xrange(5270):
        line = file.readline()
        line = line.strip()
        line = line.split(" ")
        res_line.append(line)
    return res_line

def get_test_pic_name(filename):
    file = open(filename)
    res_line = []
    for i in xrange(1768182):
    # for i in xrange(10):
        line = file.readline()
        line = line.strip()
        line = line.split(" ")
        res_line.append(line[0])
    return res_line

csvfile = open("result.csv", "w")
fileheader = ["_id", "category_id"]
writer = csv.writer(csvfile)
writer.writerow(fileheader)
id_cat = get_id('pic2train.txt')
test_pic_name = get_test_pic_name('test111.txt')
# print test_pic_name
# print test_pic_name[2]
# print type(id_cat[0][1])
res_file = open('result.txt')
for i in xrange(1768182):
# for i in xrange(10):
    context = []
    line = res_file.readline()
    line = line.strip()
    line = line.split(" ")
    # print test_pic_name[i], line, id_cat[int(line[0])][1]
    context.append(test_pic_name[i])
    context.append(id_cat[int(line[0])][1])
    writer.writerow(context)
csvfile.close()
