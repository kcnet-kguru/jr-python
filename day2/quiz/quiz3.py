# 주어진 배열을 정렬하여 이웃한 숫자와의 갭 차이가 제일 큰 수를 리턴하시오
# ex)
# max_gap ([13,10,5,2,9]) ==> return (4)
# 9 - 5 = 4
#
# max_gap ([-3,-27,-4,-2]) ==> return (23)
# |-4- (-27) | = 23
#
# max_gap ([-7,-42,-809,-14,-12]) ==> return (767)
# | -809- (-42) | = 767
#
# max_gap ([-54,37,0,64,640,0,-15]) ==> return (576)
# | 64 - 640 | = 576

def max_gap(lst):
    lst.sort()
    result = 0

    for idx in range(len(lst)-1):
        if result < abs(lst[idx+1] - lst[idx]):
            result = abs(lst[idx+1] - lst[idx])

    return result
