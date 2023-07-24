def solution(n):
    answer = 0
    temp = list(str(n))
    
    for i in temp:
        answer += int(i)    

    return answer

#  재귀함수를 사용한 풀이
def sum_digit(number):
    if number < 10:
        return number

    # number가 10 미만이 될때까지 재귀 실행
    return number%10 + sum_digit(number//10)



# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123)));

print(solution(987))