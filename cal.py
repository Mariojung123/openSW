# 두 정수를 입력받는 함수
def get_numbers():
    x = int(input("첫 번째 정수를 입력하세요: "))
    y = int(input("두 번째 정수를 입력하세요: "))
    return x, y

# 합, 차, 곱, 나눗셈을 계산하고 출력하는 함수
def calculate_and_display(x, y):
    plus_result = x + y
    minus_result = x - y
    multiply_result = x * y
    
    # 나눗셈은 0으로 나누는 경우를 처리
    if y != 0:
        divide_result = x / y
    else:
        divide_result = "정의되지 않음 (0으로 나눌 수 없습니다.)"

    print(f"{x} + {y} = {plus_result}")
    print(f"{x} - {y} = {minus_result}")
    print(f"{x} * {y} = {multiply_result}")
    print(f"{x} / {y} = {divide_result}")

# 충돌을 위한 코드 블럭
def conflict_one():
    print("make conflict_one")

# 메인 프로그램 실행
if __name__ == "__main__":
    x, y = get_numbers()
    calculate_and_display(x, y)
    conflict_one()
