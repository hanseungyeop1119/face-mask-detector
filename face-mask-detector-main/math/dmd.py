'''import matplotlib.pyplot as plt
from matplotlib_venn import venn2

A = set([1, 2, 3, 4, 5, 6])
B = set([4, 5, 6, 7, 8, 9])
C = A & B
venn2(subsets=(list(A), list(B), list(C)))
plt.show()'''

import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_circles

A = set({1, 2, 4})
B = set({4, 5, 7})

v = venn2(subsets=[A], set_labels=('A', 'B'))
c = venn2_circles(subsets=[B], linestyle='solid')
# v = venn2(subsets=[B], set_labels=('A', 'B'))
c = venn2_circles(subsets=[B], linestyle='solid')

# v = venn2(subsets=[A, B], set_labels=('setA', 'setB'))

# c = venn2_circles(subsets=[A, B], linestyle='solid')
# v = venn2(subsets=[A, B], set_labels=('A', 'B'))
# c = venn2_circles(subsets=[A, B], linestyle='solid')
plt.show()

