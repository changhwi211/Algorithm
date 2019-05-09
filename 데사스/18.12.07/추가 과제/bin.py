# 추가 과제 4
# 2진법

def solution(n):
    # 2진법을 저장할 리스트
    bin_li = list()
    
    # n이 1이상일 때까지 반복
    while n >= 1:
        # n을 2로 나눈 나머지를 문자열로 변환하여 리스트의 맨 앞에 추가
        bin_li.insert(0, str(n % 2))
        # n을 2로 나눈 몫으로 변환
        n = n // 2
    # 리스트를 변환된 2진법 문자열로 출력
    return "".join(bin_li)

# 테스트 1
print(solution(154))

# 테스트 2
print(solution(3485))