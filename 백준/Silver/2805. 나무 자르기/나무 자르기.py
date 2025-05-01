n, need_height = map(int, input().split())  # 나무의 수, 필요한 나무의 길이
wood_heights = list(map(int, input().split()))  # 나무들의 높이

# 이분탐색
start = 0
end = max(wood_heights)
mid = (start + end) // 2

result_height = 0

while start <= end:
    result_height = 0
    mid = (start + end) // 2
    result_height = sum([wood_height - mid if mid < wood_height else 0 for wood_height in wood_heights])  # 설정된 mid 로 result_height 를 구함


    if result_height >= need_height:
        result = mid
        start = mid + 1
    elif result_height < need_height:
        end = mid - 1

print(result)