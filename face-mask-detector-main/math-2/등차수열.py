# 등차수열
n = int(input('구하고 싶은 몇 번째 수 : '))
d = int(input('이 식의 공차 : '))
a = int(input('이 첫 항: '))

def k(n):
    for i in range(n):
        an = a + (n-1)*d
    return an
print(n,'번째 등차수열 결과 : ',k(n))
ad = [k(n) for n in range(1, n+1)]
print(n, '번째 까지 등차수열', ad)
# 4 7 10 13 16 19


