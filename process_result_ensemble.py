import numpy as np
import csv

total = 0
txt_file = open('./test_result_finetune/result.txt', 'wb')
for i in xrange(36):
    npy_name = './test_result_finetune/prob_{:0}.npy'.format(i)
    print npy_name
    npy = np.load(npy_name)
    len = npy.shape[0]
    # print npy.shape[0]
    total += npy.shape[0]
    for j in xrange(len):
        max_prob = npy[j].max()
        # print max_prob
        res = np.where(npy[j] == np.max(npy[j]))[0][0]
        txt_file.write(str(max_prob)+' '+str(res)+'\n')
    print total
print total
