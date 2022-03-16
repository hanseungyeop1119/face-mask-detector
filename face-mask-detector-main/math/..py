import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_circles

A = set([1, 2, 3, 4, 5, 6])
B = set([])

v = venn2(subsets=[A, B], set_labels=('A', 'Number of Set A'))
c = venn2_circles(subsets=[A, B], linestyle='solid')
plt.show()

