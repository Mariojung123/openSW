# 두 정수를 입력받는 함수
def get_numbers():
    x = int(input("첫 번째 정수를 입력하세요: "))
    y = int(input("두 번째 정수를 입력하세요: "))
    return x, y

# 합과 차를 계산하고 출력하는 함수
def calculate_and_display(x, y):
    plus_result = x + y
    minus_result = x - y
    print(f"{x} + {y} = {plus_result}")
    print(f"{x} - {y} = {minus_result}")

# 메인 프로그램 실행
if __name__ == "__main__":
    x, y = get_numbers()
    calculate_and_display(x, y)