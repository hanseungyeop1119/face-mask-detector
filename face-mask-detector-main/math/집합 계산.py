# import matplotlib.pyplot as plt
# from matplotlib_venn import venn2
import matplotlib.pyplot as plt
from matplotlib_venn import venn3


'''R = set('red')
O = set('blue')
Y = set('yellow')
# G = set(12, 14, 16, 18, 20)
v_test1 = venn3([R, O, Y], ('A', 'B', 'C'))
# v_test1 = venn3([s1, s3, s4], ('set1', 'set3', 'set4'))
for t in v_test1.set_labels: t.set_fontsize(22)
# for t in v_test1.subset_labels: t.set_fontsize(20)
label = v_test1.get_label_by_id('111')
label.set_fontsize(10)'''
'''a = [10, 1, 1, 2, 4, 5, 6, 6, 7, 9]
a = list(set(a))
print(a)'''
A = set([1, 2, 3, 4, 5, 6])
B = set([4, 5, 6, 7, 8, 9])

# 1. 교집합
n = A & B
print('A ∩ B =', n)

# 2. 합집합
u = A | B
print('A ∪ B = ', u)

# 3. 차집합
m = A - B
print('A - B = ', m)
m1 = B - A
print('B - A = ', m1)
# venn2(subsets=(11, 1, 1))
plt.show()