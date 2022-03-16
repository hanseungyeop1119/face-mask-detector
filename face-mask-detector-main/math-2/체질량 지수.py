# 체질량 지수
# E = 키^2/체중
# h = 체충
# t = 키
# round = 반올림
h = float(input("키를 입력하세요 (단 m 단위로): "))
w = float(input("체중을 입력하세요."))
h2 = h*h
E = w/h2
print(round(E, 2))


