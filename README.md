# Object-Oriented-Programming-Study

## 프로그래밍 종류
- 절차지향 - 무엇을 어떤 순으로 할지 (함수 나열)
  - 프로그램을 순차적인 절차로 구성
  - 데이터를 함수에 전달, 데이터와 함수가 분리
  ```
  # 절차지향 예시
  def input_number():
    return int(input("숫자를 입력하세요:"))
  def square(x):
    return x * x
  def print_result(result):
    print(f"결과: {result}")
  
  num = input_number()
  result = square(num)
  print_result(result)
  ```
- 객체지향 - 누가 뭘 할지 (메소드 나열)
  - 프로그램을 객체들의 상호작용으로 구성
  - 각 객체는 속성(attribute)과 행동(method)을 가짐
  
