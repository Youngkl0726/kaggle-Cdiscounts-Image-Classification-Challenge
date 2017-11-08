import csv

csv_file = csv.reader(open('train.csv', 'r'))
total_num = 0
id_list = []
id_num = 0
txt_file = open("train.txt", 'wb')
index = 0
for line in csv_file:
    # print line[0], line[1]
    total_num += 1

    if total_num == 1:
        id_list.append(int(line[1]))
        index = id_num
        id_num += 1
    else:
        if int(line[1]) in id_list:
            index = id_list.index(int(line[1]))
            # print "index ", total_num, index
        else:
            index = id_num
            id_num += 1
            id_list.append(int(line[1]))
            # print id_num
    txt_file.write('{:0}.png'.format(int(line[0])) + ' ' + str(index) + '\n')
    # if id_num == 100:
    #     break

print "total_num", total_num
print "id_num", id_num
txt_file.close()
