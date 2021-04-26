# 당신은 마법의 우물에 서 있습니다. 두 개의 양의 정수가 기록되어 있습니다
# a와 b. 마법 구슬을 우물에 던질 때마다 a * b 달러를주고 a와 b 모두 1 씩 증가합니다.
# 마법 구슬이 n 개 있습니다. 당신은 얼마나 많은 돈을 벌 것입니까?

# Example
# For a = 1, b = 2 and n = 2, the output should be 8


def magical_well(a, b, n):
    result = 0
    for i in range(0,n):
        result += a*b
        a += 1
        b += 1
    return result
