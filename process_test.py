import csv

print 'hehe'
csv_file = csv.reader(open('test.csv', 'r'))
txt_file = open("test111.txt", 'wb')
total_num = 0
for line in csv_file:
    total_num += 1
    # print line
    txt_file.write('{:0}'.format(int(line[1])) + ' ' + '0' + '\n')

print total_num
txt_file.close()

# import csv
# csv_file = csv.reader(open('test.csv', 'r'))
# for i in xrange(36):
#     txt_name = 'test{:0}.txt'.format(i)
#     print txt_name
#     txt_file = open(txt_name, 'wb')
#     cnt = 0
#     for line in csv_file:
#         txt_file.write('{:0>11d}.png'.format(int(line[1])) + ' ' + '0' + '\n')
#         cnt += 1
#         if cnt == 50000:
#             break
#     txt_file.close()
