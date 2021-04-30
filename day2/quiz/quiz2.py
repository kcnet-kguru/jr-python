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

def min_sum(lst):
    result = 0
    while lst:
        mmin = lst.pop(lst.index(min(lst)))
        mmax = lst.pop(lst.index(max(lst)))
        result += mmin * mmax
    return result

print(min_sum([5,4,2,3]))
print(min_sum([12,6,10,26,3,24]))
print(min_sum([9,2,8,7,5,4,0,6]))
