A = set([1, 2, 3, 4, 5, 6])
B = set([4, 5, 6, 7, 8, 9])

'''D = 2 in A
print(D)
D2 = 100 in A
print(D2)'''
O = int(input('A = {}'))
D = O in A
if D:
    print("A ⊂ {", O, "}")
else:
    print("A no {", O, "}")



