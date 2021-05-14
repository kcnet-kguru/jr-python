# 정수 배열이 있습니다. 배열의 첫 번째 큰 수와 두 번째 큰 수의 차이를 계산해야 합니다.
#  diffBig2([10, 5, 2]);
# 첫번째 큰수는 10, 두번째 큰수는 5, 10 - 5 = 5
# 입력 배열에 정렬() 메서드가 비활성화되어 있으므로 다른 방법으로 해결해야 합니다


def diffBig2(arr):
    for iter in range(len(arr)):
        idx = 0
        while idx < len(arr) - 1:
            temp = arr[idx]
            if temp > arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], temp
                temp = arr[idx + 1]
            idx += 1
    result = arr[-1] - arr[-2]

    return result
