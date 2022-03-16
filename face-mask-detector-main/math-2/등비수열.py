# 등비수열
# 파이썬 내장 라이브러리인 math의 pow함수를 이용하는 방법
import math
n = int(input('구하고 싶은 몇 번째 수 : '))
r = int(input('이 식의 공비 : '))
a = int(input('이 첫 항: '))
def k(n):
    for i in range(n):
        an = a*(math.pow(r, n-1))
    return an
print(n,'번째 등비수열 결과 : ', int(k(n)))
ad =[k(n) for n in range(1, n+1)]
print(n, '번째 까지 등비수열', ad)
print(n, "번째 등비수열 결과 : ", r, "^", int(n-1))

# 4 7 10 13 16 19

