import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_circles
# 집합 A와 B의 원소들
A = set([1, 2, 3, 4, 5, 6])
B = set([4, 5, 6, 7, 8, 9])
print('집합 A = {1, 2, 3, 4, 5, 6}')
print('집합 B = {4, 5, 6, 7, 8, 9}')
# 1. 교집합
m99 = A & B
print('교집합 A ∩ B =', m99)

# 2. 합집합
m98 = A | B
print('합집합 A ∪ B = ', m98)

# 3. 차집합
m = A - B
print('차집합 A - B = ', m)
m1 = B - A
print('차집합 B - A = ', m1)

# 4. 원소 판별
m2 = int(input('X [] A\nX에10를 쓰세요. : '))
D = m2 in A
if D:
    print('답 = ', m2, '∈ A\n')
else:
    print('답 = ', m2, '∉ A\n')

m2 = int(input('X [] B\nX에2를 쓰세요. : '))
D = m2 in B
if D:
    print('답 = ', m2, '∈ B\n')
else:
    print('답 = ', m2, '∉ B\n')

# 5. 밴다이어 그램
v = venn2(subsets=[A, B], set_labels=('A', 'B'))
c = venn2_circles(subsets=[A, B], linestyle='solid')

# 6.

plt.show()

