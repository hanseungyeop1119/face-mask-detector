# -*- coding: CP949 -*-
#  �Ǻ���ġ ���� n��° �� ã��
# 1. n�Է��� �ް� �迭 ������ n+2��ŭ �Ҵ����ش�.
# 2. dynamic programming�� �̿��Ѵ�.
# 3. �� ����Ʈ�� �Ǻ���ġ �Ϲ����� �̿��Ͽ� ������ ���ش�.
# 4. �ش��ϴ� n��° ���� ����
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
n = int(input('n��° �Ǻ���ġ �� : '))
if n <= 0:
    print
    'wrong input'
else:
    dp = [0] * (n + 2)
    print
    n, '��° �Ǻ���ġ �� ��� : ', seq3(n)