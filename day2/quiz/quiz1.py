# 정수 배열/목록 []이(가) 주어진 경우, k maximum 숫자의 곱을 찾습니다.
# ex)
# max_product ([4, 3, 5], 2) ==>  return (20)
# 5 * 4 = 20
#
# max_product ([8, 10 , 9, 7], 3) ==>  return (720)
# 8 * 9 * 10 = 720
#
# max_product([10, 8, 3, 2, 1, 4, 10], 5) ==> return (9600)
# 10 * 10 * 8 * 4 * 3 = 9600
#
# max_product ([10, 3, -1, -27] , 3)  return (-30)
# 10 * 3 * -1 = -30

from functools import reduce


def max_product(obj, k):
    sorted_obj = sorted(obj)

    return reduce(lambda x, y: x * y, sorted_obj[-k:])
