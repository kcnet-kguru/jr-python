# 주어진 리스트를 임의의 사람들이 차례로 리스트에서 제일 높은 값을 가져가 누적시키는 게임을 진행하고 있다.
# 예를 들어 [1, 2, 3, 4, 5] 리스트가 주어졌을 때 두사람이 게임을 치른 결과는  [9, 6] 이다.
# 만약 세사람일 경우의 결과는 [5, 7, 3] 이다. <- 요거 [7, 5, 3] 인거 같습니다
# 리스트에서 값을 가져가는 형태이므로 리스트보다 사람 수가 많을 경우 값을 가져가지 못할 경우에는 0을 리턴한다.


def beggars(values, n):
    values = sorted(values, reverse=True)
    gamers = [0] * n

    for i in range(len(values)):
        gamers[i % n] += values[i]

    return gamers
