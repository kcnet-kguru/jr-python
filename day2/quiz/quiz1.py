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
import numpy as np

def max_product_1(obj, k):
    target_list = obj
    default = 1

    for i in range(len(target_list)):
        for j in range(len(target_list) - 1):
            tmp = target_list[i]
            if target_list[i] > target_list[i + 1]:
                target_list[i] = target_list[i + 1]
                target_list[i + 1] = tmp

    for value in target_list[-k:]:
        default *= value

    return default


def max_product_2(obj, k):
    obj_array = np.array(obj)
    result = np.prod(obj_array[np.argsort(obj_array)[-3:][::-1]])

    return result