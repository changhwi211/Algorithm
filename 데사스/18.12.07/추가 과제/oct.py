# 추가 과제 4
# 8진법

def solution(n):
    # 8진법을 저장할 리스트
    oct_li = list()
    
    # n이 1이상일 때까지 반복
    while n >= 1:
        # n을 8로 나눈 나머지를 문자열로 변환하여 리스트의 맨 앞에 추가
        oct_li.insert(0, str(n % 8))
        # n을 8로 나눈 몫으로 변환
        n = n // 8
    # 리스트를 변환된 8진법 문자열로 출력
    return "".join(oct_li)

# 테스트 1
print(solution(154))

# 테스트 2
print(solution(3485))