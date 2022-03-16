n = int(input('n번째 피보나치 수 : '))
def fib(n): #Fibonacci
    a, b = 1, 1
    for i in range(2, n):
        print('A')
        a, b = b, a + b
    return a

print(n, '번째 피보나치 수 결과 : ', fib(n))
n1 = [fib(x)for x in range(1, n+1)]
print(n, '번째까지 피보나치 수열 : ', fib(n))
print(n1)