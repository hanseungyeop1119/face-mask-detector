import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_circles
print("1. 7보다 작은 집합을 A 라고 할 때, ㅁ 안에 ∈ 또는 ∉ 중에 알맞은 기호를 써넣으시오.")
A = set([-2, -1, 0, 1, 2, 3, 4, 5, 6])
m2 = int(input('(1) X [] A\nX에2를 쓰세요. : '))
D = m2 in A
if D:
    print('답 = ', m2, '∈ A\n')
else:
    print('답 = ', m2, '∉ A\n')

m2 = int(input('(2) X [] A\nX에6을 쓰세요. : '))
D = m2 in A
if D:
    print('답 = ', m2, '∈ A\n')
else:
    print('답 = ', m2, '∉ A\n')

m2 = int(input('(3) X [] A\nX에0을 쓰세요. : '))
D = m2 in A
if D:
    print('답 = ', m2, '∈ A\n')
else:
    print('답 = ', m2, '∉ A\n')

m2 = int(input('(4) X [] A\nX에7을 쓰세요. : '))
D = m2 in A
if D:
    print('답 = ', m2, '∈ A\n')
else:
    print('답 = ', m2, '∉ A\n')

print('공집합이 맞는걸 고르시오.')
A = set(['ø', '[ ]', '{ ]', '{0}', '{ø}'])
'ø' == 1
'[ ]' == 2
'{ ]' == 3
'{0}' == 4
'{ø}' == 5
m1 = 1
m1 = int(input('공집합이 맞는걸 고르시오.\n1. ø\n2. []\n3. { ]\n4. {0}\n5.{ø}\n'))
if m1 == 1:
    print('정답')
else:
    print("틀림")


