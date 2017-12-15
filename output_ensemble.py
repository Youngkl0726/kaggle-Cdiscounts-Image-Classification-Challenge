import numpy as np
import csv

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

res_file_1 = open('result1.txt')
res_file_2 = open('result2.txt')
res_file_3 = open('result3.txt')
res_file_4 = open('result4.txt')
for i in xrange(1768182):
# for i in xrange(10):
    context = []
    line1 = res_file_1.readline()
    line1 = line1.strip()
    line1 = line1.split(" ")
    line2 = res_file_2.readline()
    line2 = line2.strip()
    line2 = line2.split(" ")
    line3 = res_file_3.readline()
    line3 = line3.strip()
    line3 = line3.split(" ")
    line4 = res_file_4.readline()
    line4 = line4.strip()
    line4 = line4.split(" ")
    # print line1, line2, line3
    prob = []
    prob.append(line1[0])
    prob.append(line2[0])
    prob.append(line3[0])
    prob.append(line4[0])
    id = []
    id.append(line1[1])
    id.append(line2[1])
    id.append(line3[1])
    id.append(line4[1])
    # print prob.index(max(prob))
    ans_id = int(id[prob.index(max(prob))])

    # if float(line1[0]) > float(line2[0]):
    #     ans_id = int(line1[1])
    # else:
    #     ans_id = int(line2[1])
    # print ans_id

    context.append(test_pic_name[i])
    context.append(id_cat[ans_id][1])
    writer.writerow(context)
csvfile.close()
print "over"
