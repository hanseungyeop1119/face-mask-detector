"""U = ["{", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "}"]
A = [2, 4, 6, 8, 10]
B = [1, 2, 3, 5, 7, 9]
Z = A + B
Z.sort()
print(Z)"""
"""U = ["{", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "}"]
A = [2, 4, 6, 8, 10]
B = [1, 3, 5, 7, 9, 10]
Z = A + B
Z.sort()
Z_set = set(Z)
Z_list = list(Z_set)
print(Z_list)"""


'''A = set([2, 4, 6, 8, 10])
B = set([1, 10, 3, 5, 7, 9, 2])
Z = A & B
# Z.sort()
print(Z)'''

"""A = set([10, 2, 4, 6, 8])
B = set([1, 10, 3, 5, 7, 9, 2])
Z = A & B
print(Z)"""

# people = ['김가나', '한승엽', '박정호', '이미함', '최수혁', '장정우']

# print(sorted(people, key=lambda x: (x[-3], x[1], x[-1])))


import matplotlib.pyplot as plt
from matplotlib_venn import venn2
A = [1, 3, 5]
B = [2, 4, 6]
C = A & B
venn2(subsets=('A', 'C', 'B'))
plt.show()