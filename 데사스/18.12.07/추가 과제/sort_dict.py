# 추가 과제 3

def solution(dic):
    # 딕셔너리를 value 기준으로 정렬
    return sorted(dic, key=lambda x: dic[x])

# 테스트 결과
test_dic = {"국어": 75, "수학": 56, "영어": 90, "과학": 60}
print(solution(test_dic))