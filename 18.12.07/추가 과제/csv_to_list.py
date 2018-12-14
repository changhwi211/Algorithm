# 추가 과제 1
# csv 포맷 => 딕셔너리 리스트

def solution(csv):
    li = []
    key = []
    # csv의 각 라인별로 파싱
    for i, line in enumerate(csv.splitlines()):
        row = dict()
        # 첫 번째 행에서 key 추출
        if i == 0:
            key = line.split(",")
            key = [i.strip() for i in key]
        # 두 번째 행 이후 라인
        else:
            # 각 행을 ","을 기준으로 파싱
            for j, value in enumerate(line.split(",")):
                # 각 행의 파싱된 요소가 숫자로 변환 가능한 경우
                value = value.strip()
                if value.isnumeric():
                    # 우선 int형으로 변환하여 딕셔너리에 추가
                    try:
                        row[key[j]] = int(value)
                    # int형으로 변환되지 않으면 float형으로 변환하여 딕셔너리에 추가
                    except ValueError:
                        row[key[j]] = float(value)
                # 각 행의 파싱된 요소가 문자열일 경우는 단순히 딕셔너리에 추가
                else:
                    row[key[j]] = value
            li.append(row)
    return li

# 테스트용 csv 포맷
test_csv = "nickname, name, email, age\n길동, 홍길동, gildong@gmail.com, 20\n김미, 김민수, gild@naver.com, 40\n철광, 김철수, mado@daum.net, 30\n재석, 유재혁, sarang@gmail.com, 50\n"

# 테스트 결과
print(solution(test_csv))