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
def closest_multiple_10(i):
    return round((i-1) / 10) * 10
