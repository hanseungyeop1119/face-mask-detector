# -*- coding: CP949 -*-
#  피보나치 수열 n번째 항 찾기
# 1. n입력을 받고 배열 공간을 n+2만큼 할당해준다.
# 2. dynamic programming을 이용한다.
# 3. 각 리스트에 피보나치 일반항을 이용하여 연산을 해준다.
# 4. 해당하는 n번째 값을 리턴
import sys
import rawpy

def seq3(n):
    global dp
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    for i in range(n + 1)[3:]:
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
n = int(input('n번째 피보나치 수 : '))
if n <= 0:
    print
    'wrong input'
else:
    dp = [0] * (n + 2)
    print
    n, '번째 피보나치 수 결과 : ', seq3(n)