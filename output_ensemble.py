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

res_file_1 = open('./result/result1.txt')
res_file_2 = open('./result/result2.txt')
res_file_3 = open('./result/result3.txt')
res_file_4 = open('./result/result4.txt')
res_file_5 = open('./result/result5.txt')
res_file_6 = open('./result/result6.txt')
res_file_7 = open('./result/result7.txt')
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
    line5 = res_file_5.readline()
    line5 = line5.strip()
    line5 = line5.split(" ")
    line6 = res_file_6.readline()
    line6 = line6.strip()
    line6 = line6.split(" ")
    line7 = res_file_7.readline()
    line7 = line7.strip()
    line7 = line7.split(" ")
    # print line1, line2, line3
    prob = []
    prob.append(float(line1[0]))
    # print type(line2[0])
    prob.append(float(line2[0]))
    prob.append(float(line3[0]))
    prob.append(float(line4[0]))
    prob.append(float(line5[0]))
    prob.append(float(line6[0]))
    prob.append(float(line7[0]))
    id = []
    id.append(line1[1])
    id.append(line2[1])
    id.append(line3[1])
    id.append(line4[1])
    id.append(line5[1])
    id.append(line6[1])
    id.append(line7[1])
    # print prob.index(max(prob))
    ans_id = int(id[prob.index(max(prob))])

    context.append(test_pic_name[i])
    context.append(id_cat[ans_id][1])
    writer.writerow(context)
csvfile.close()
print "over"
