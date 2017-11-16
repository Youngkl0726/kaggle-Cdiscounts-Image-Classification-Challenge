import csv

print 'hehe'
csv_file = csv.reader(open('test.csv', 'r'))
txt_file = open("test.txt", 'wb')
total_num = 0
for line in csv_file:
    total_num += 1
    # print line
    txt_file.write('{:0>11d}.png'.format(int(line[1])) + ' ' + '0' + '\n')

print total_num
txt_file.close()
