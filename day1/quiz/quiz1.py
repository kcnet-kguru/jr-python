# 주어진 숫자를 10으로 나누어 나머지가 0인 가장 가까운 숫자를 반환합니다.
#
# Example input:
#
# 22
# 25
# 37
# Expected output:
#
# 20
# 30
# 40

import math


def closest_multiple_10_1(i):
    result = round(i, -1)

    return result

def closest_multiple_10_2(i):
    remains = 10 - int(str(i)[-1])
    if remains <= 5:
        result = i + remains
    else:
        result = i - (int(str(i)[-1]))

    return result