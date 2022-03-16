'''import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 2, figsize=(10, 5))# 1행2열

for i in range(2):
    ax_i = ax[i]


    def draw_ellipse(ax, x, y, w, h, a, fillcolor):
        e = patches.Ellipse(
            xy=(x, y),
            width=w,
            height=h,
            angle=a,
            color=fillcolor)
        ax.add_patch(e)


    def draw_text(ax, x, y, text, color=[0, 0, 0, 1], fontsize=14):
        ax.text(
            x, y, text,
            horizontalalignment='center',
            verticalalignment='center',
            fontsize=fontsize,
            color=color)


    def venn2(ax, labels, names=['A', 'B'], **options):
        colors = options.get('colors', [default_colors[i] for i in range(2)])
        fontsize = options.get('fontsize', 14)

        ax.set_axis_off()
        ax.set_ylim(bottom=0.0, top=0.7)
        ax.set_xlim(left=0.0, right=1.0)

        # body
        draw_ellipse(ax, 0.375, 0.3, 0.5, 0.5, 0.0, colors[0])
        draw_ellipse(ax, 0.625, 0.3, 0.5, 0.5, 0.0, colors[1])
        draw_text(ax, 0.74, 0.30, labels.get('01', ''), fontsize=fontsize)
        draw_text(ax, 0.26, 0.30, labels.get('10', ''), fontsize=fontsize)
        draw_text(ax, 0.50, 0.30, labels.get('11', ''), fontsize=fontsize)

        # legend
        draw_text(ax, 0.20, 0.56, names[0], 'k', fontsize=fontsize)
        draw_text(ax, 0.80, 0.56, names[1], 'k', fontsize=fontsize)'''
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

## 1. Example
ex_1 = [[1,2,3,4], [3,4,5,6,7]]
ex_2 = [['a','b','c'], ['a','c']]
ex = [ex_1, ex_2]

## 2. Make venn diagrams
fig, ax = plt.subplots(1,2,figsize=(15,5))
for i in range(2):
    ax_i = ax[i]
    labels = venn2.get_labels(ex[i])
    venn2.venn2(ax_i, labels, names=['hello', 'world'])

## 3. Save and show the plots
plt.savefig('ex_venn2.png')
plt.show()
plt.close()