# 추가 과제 1
# 딕셔너리 리스트 => csv 포맷

def solution(li):
    # 변환될 csv 문자열
    csv = ""
    # key row 추가
    csv += ", ".join(li[0].keys()) + "\n"
    
    # value row 추가(딕셔너리의 개수 만큼)
    for dic in li:
        # 각 딕셔너리를 value row로 변환
        for i, value in enumerate(dic.values()):
            # 각 딕셔너리의 요소의 끝에 붙는 문자열
            # 마지막 요소 전까지는 ",", 마지막 요소에는 개행
            tail_str = ", " if i < len(dic) - 1 else "\n"
            try:
                csv += value
            # 딕셔너리의 요소가 문자열이 아니라면 문자열로 변환 후 csv 문자열에 추가
            except TypeError:
                csv += str(value)
            csv += tail_str
    return csv

# 테스트용 딕셔너리 리스트
test_li =[
    {"name":"홍길동", "age": 20, "nickname": "길동", "email": "gildong@gmail.com"},
    {"name":"김민수", "age": 40, "nickname": "김미", "email": "gild@naver.com"},
    {"name":"김철수", "age": 30, "nickname": "철광", "email": "mado@daum.net"},
    {"name":"유재혁", "age": 50, "nickname": "재석", "email": "sarang@gmail.com"},
]

# 테스트 결과
print(solution(test_li))

