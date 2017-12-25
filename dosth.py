# coding:utf-8

# import matplotlib.pyplot as plt
# import numpy as np
#
# values = [[1, 2, 3, 4], [3, 4, 5, 6], [6, 7, 8, 9]]
# cols = ['d', 'e', 'f', 'g']
# rows = ['a', 'b', 'c']
# # print(np.arange(0, 1, .1))
# # print(np.arange(100000, 400000, 30000))
# # plt.figure(1)
# # plt.subplot()
# # plt.table(cellText=values, colWidths=[0.1] * len(cols), colLabels=cols, rowLabels=rows, loc='upper center')
# # plt.subplot(212)
# # plt.plot(np.arange(100000, 400000, 30000), np.arange(0, 1, .1), 'bs')
# # plt.plot(np.arange(100000, 400000, 30000), np.arange(0, 2, .2), 'g^')
# # plt.plot(np.arange(100000, 400000, 30000), np.arange(0, 1, .1))
# # plt.plot(np.arange(100000, 400000, 30000), np.arange(0, 2, .2))
# # plt.show()
# plt.figure(1)
# flag = 0
# for value in values:
#     flag += 1
#     plt.plot([1, 2, 3, 4], value)
#     plt.set_xlabel("hehe")
#     plt.set_ylabel("haha")
#     plt.legend(cols, loc='upper right')
# plt.show()

# a,b = (2,2)
# print(a,b)
import numpy as np

a = np.array([1, 2, 3, 4])
index = np.array([3, 2, 1, 4])
a = a[index]
print a
