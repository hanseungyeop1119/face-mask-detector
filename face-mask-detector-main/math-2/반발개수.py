# math library import
# e = H 분의 h
# E 에다가 루트를 씌어주는 것
# H가 정수가 아닌지 맞는지를 판단하기 위한 코드
# h가 정수가 아닌지 맞는지 판단하기 위한 코드
import math
yes = input('H가 정수이면 y를 입력해 주세요')
No = input('h가 정수가 아니면 n를 입력해 주세요')
if yes == 'y':
    H = int(input('축구공을 떨어뜨린 높이 (단위 : m): '))
else:
    H = float(input('축구공을 떨어뜨린 높이 (단위 : m): '))
if No == 'n':
    h = float(input('축구공이 튀어오른 높이 (단위 : m) : '))
else:
    h = int(input('축구공이 튀어오른 높이 (단위 : m) : '))
e = h/H
E = math.sqrt(float(e))
print("반발계수는", round(E, 2), "입니다")


