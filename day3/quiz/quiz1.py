# 정수 배열이 있습니다. 배열의 첫 번째 큰 수와 두 번째 큰 수의 차이를 계산해야 합니다.
#  diffBig2([10, 5, 2]);
# 첫번째 큰수는 10, 두번째 큰수는 5, 10 - 5 = 5
# 입력 배열에 정렬() 메서드가 비활성화되어 있으므로 다른 방법으로 해결해야 합니다

import heapq

def diffBig2(arr):
    heap = []
    for num in arr:
        heapq.heappush(heap, (-num, num))

    return heapq.heappop(heap)[1] - heapq.heappop(heap)[1]