# 각 두 정수 곱의 합에서 얻은 최소 합계를 구합니다.
# ex)
# minSum([5,4,2,3]) ==> return (22)
# 5*2 + 3*4 = 22
#
# minSum([12,6,10,26,3,24]) ==> return (342)
# 26*3 + 24*6 + 12*10 = 342
#
# minSum([9,2,8,7,5,4,0,6]) ==> return (74)
# 9*0 + 8*2 +7*4 +6*5 = 74
import numpy as np

def min_sum(lst):
    obj_array = np.array(lst)
    sorted = obj_array[np.argsort(obj_array)]
    sum = 0

    for idx in range(len(sorted)//2):
        sum += sorted[idx] * sorted[-idx - 1]

    return sum
