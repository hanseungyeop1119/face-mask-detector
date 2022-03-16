from matplotlib import pyplot as plt
import math as m

def drawGraph(x, y):
    plt.plot(x, y)
    plt.xlabel('Horizontal displacement (m)')
    plt.ylabel('Vertical displacement (m)')
    plt.title('Projectile motion of a howitzer')

def frange(start, final, dt):    # 미세한 시간 차이로 만든 지난 시간 배열 생성
    numbers = []                 # 참고: dt는 미세한 시간 차이
    while start < final:
        numbers.append(start)
        start = start + dt

    return numbers

def drawTrajectory(V0, theta, g):    #곡사포 궤적 그리기
    theta = m.radians(theta)

    Tflight = 2 * V0 * m.sin(theta)/g       #곡사포의 체공시간 계산
    intervals = frange(0, Tflight, 0.001)   #frange()로 시간 배열 생성
    x = []          #x[], y[]는 각각 시간별
    y = []          #x좌표와 y좌표 목록
    for t in intervals:
        x.append(V0 * m.cos(theta) * t)
        y.append(V0 * m.sin(theta) * t - g*(t**2)/2)

    drawGraph(x, y)
    print('최고 높이: {}m'.format(max(y)))
    print('이동 거리: {}m'.format(max(x)))

if __name__ == '__main__':
    try:
        V0 = float(input('곡사포의 초기 속력을 입력하세요 (﻿㎧): '))
        deg = float(input('곡사포의 발사 각도를 입력하세요 (º): '))
        planet = int(input('발사 행성의 번호를 입력하세요(수성: 0, 금성: 1, 지구: 2, 화성: 3, \
목성: 4, 토성: 5, 천왕성: 6, 해왕성: 7): '))
        if (planet < 0) or (planet > 7):
            divby0 = 1 / 0      #잘못된 행성 번호가 입력되면 강제로 에러를 발생
        Gcs = [3.61, 8.83, 9.80, 3.75, 25.0, 11.2, 10.5, 13.3] #행성 번호별 중력가속도 목록
    except:
        print('잘못된 값입니다.')
    else:
        drawTrajectory(V0, deg, Gcs[planet])
        axis = plt.gca()
        axis.set_aspect('equal')  #x좌표와 t좌표의 비율 같게 함
        plt.show()
