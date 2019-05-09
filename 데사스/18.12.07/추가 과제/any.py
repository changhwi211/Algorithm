# 추가 과제 2
# any

def any(li):
    # 모든 리스트의 요소 순차 탐색
    # 리스트 내 하나라도 True가 있으면 True 반환
    # 리스트 내에 True가 하나도 없으면 False 반환
    for elem in li:
        if elem:
            return True
    return False

# 테스트 1
print(any([False, False, False]))

# 테스트 2
print(any([False, False, True]))

