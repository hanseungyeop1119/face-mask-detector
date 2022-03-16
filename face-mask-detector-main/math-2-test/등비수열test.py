def seq2(start, difference, n):
    cnt = 1
    ans = start
    while True:
        cnt += 1
        ans *= difference

        if cnt == n:
            return ans
start = int(input('초항 : '))
difference = int(input('공비 : '))
n = int(input('몇 번째 항 : '))

print
n, '번째 항의 값 :: ', seq2(start, difference, n)
