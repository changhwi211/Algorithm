# 추가 과제 4
# 16진법

def solution(n):
    # 16진법의 요소 리스트
    hex_elem = list(str(i) for i in range(10)) + ["a", "b", "c", "d", "e", "f"]
    # 16진법을 저장할 리스트
    hex_li = list()
    
    # n이 1이상일 때까지 반복
    while n >= 1:
        # n을 16로 나눈 나머지를 인덱스로하여 16진법 요소 문자열로 변환하여 리스트의 맨 앞에 추가
        hex_li.insert(0, hex_elem[n % 16])
        # n을 16로 나눈 몫으로 변환
        n = n // 16
    # 리스트를 변환된 16진법 문자열로 출력
    return "".join(hex_li)

# 테스트 1
print(solution(154))

# 테스트 2
print(solution(3485))