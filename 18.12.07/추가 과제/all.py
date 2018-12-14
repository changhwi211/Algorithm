# 추가 과제 2
# all

def all(li):
    # 모든 리스트의 요소 순차 탐색
    # 리스트 내 하나라도 False가 있으면 False 반환
    # 리스트 내에 False가 하나도 없으면 True 반환
    for elem in li:
        if not elem:
            return False
    return True

# 테스트 1
print(all([True, True, True]))

# 테스트 2
print(all([True, False, True]))