# 피보나치수열
n = int(input('n번째 피보나치 수 : '))
def fibonacci(n):
    a, b = 1, 1
    for i in range(1, n):
        a, b = b, a + b
    return a
print(n, '번째 피보나치 수 결과 : ', fibonacci(n))
x1 = [fibonacci(n) for n in range(1, n+1)]
print(n, '번째까지 피보나치 수열 : ', x1)


