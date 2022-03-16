#방법 1. 일반 함수 사용 방식 (Function)
#가장 일반적인 함수로 코딩한 경우 입니다. 입력값을 n을 넣어주면, loop문을 통하여 피보나치를 계산하고 결과값을 반환해 주는 방식입니다.
n = int(input('n번째 피보나치 수 : '))
def fib(n):
    a, b = 1, 1
    for i in range(1, n):
        a, b = b, a + b
    return a
print(n, '번째 피보나치 수 결과 : ', fib(n))

# n번째 까지 출력
x = int(input('n번째 피보나치 수 : '))
def fib(x):
    c, d = 1, 1
    if x == 1 or x == 2:
        return 1
    for i in range(1, x):
        c, d = d, c + d
    return c

x1 = [fib(x)for x in range(1,x+1)]
print(x, '번째까지 피보나치 수열 : ', fib(x))
print(x1)