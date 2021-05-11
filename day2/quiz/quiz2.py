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
from functools import reduce

def min_sum(lst):
    lst.sort(reverse=True)
    size = len(lst)
    return reduce(lambda acc, cur: acc + (lst[cur]*lst[size-1-cur]), range(0, (int)(size/2) ), 0)

