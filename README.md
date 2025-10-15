# Object-Oriented-Programming-Study

## 프로그래밍 방식의 종류
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
  
  num = input_number()  # 데이터 (data)
  result = square(num)  # 함수에 전달
  print_result(result)
  ```
- 객체지향 - 누가 뭘 할지 (메소드 나열)
  - 프로그램을 객체들의 상호작용으로 구성
  - 각 객체는 속성(attribute)과 행동(method)을 가짐
  - Attribute: 객체가 가지고 있는 속성, 데이터
  - Method: 객체가 할 수 있는 행동, 기능
  
  ```
  # 객체지향 예시
  
  class Calculator:
      def __init__(self, number):
          self.number = number  # 속성 (attribute)

      def square(self):         # 메소드 (method)
          return self.number * self.number

  calc = Calculator(5)
  print(calc.square())
  ```
## Function vs Method
- Function
  - 소속: 클래스 외부에서 정의
  - 호출방식: function()
  - 호출대상: 독립적인 코드 블록
- Method
  - 소속: 클래스 내부에서 정의
  - 호출방식: object.method()
  - 호출대상: 특정 객체의 데이터에 적용

## Class vs Instance
- Class
  - 의미: 객체를 만들기 위한 설계도. 즉, 객체가 어떤 속성(Attribute)과 기능(Method)을 가져야 하는지를 정의한 추상적인 틀.
  - 본질: 추상적 개념
  - 역할: 속성과 행동을 정의
  - 메모리 존재여부: 코드 영역에 정의
 
- Method
  - 의미: 클래스로부터 만들어진 실제 객체
  - 본질: 구체적 실체
  - 역할: 정의된 속성과 행동을 사용
  - 메모리 존재여부: 메모리에 생성되어 존재

## 객체지향 프로그래밍의 핵심 4대 개념
1. 캡슐화 (Encapsulation)
    - 정의: 외부에서 직접 접근하지 못하게 보호하는 것
    - Public
      - 어디서나 접근 가능
      - ex) name
    
    - Protected
      - 외부접근이 가능하지만 내부 전용임을 약속
      - 내부 및 상속받은 클래스 내에서만 접근 권장
      - ex) _name
    
    - Private
      - 클래스 내부에서만 접근 가능
      - 외부와 상속 클래스 접근 불가
      - ex) __name
    ```
    # 캡슐화 예시
    
    class Account:
        def __init__(self, owner, balance):
            self.owner = owner          # Public
            self._interest_rate = 0.03  # Protected
            self.__balance = balance    # Private
  
        def deposit(self, amount):
            if amount > 0:
              self.__balance += amount
  
        def __calculate_interest(self):  # Private method
            return self.__balance * self._interest_rate
  
        def get_balance(self):
            return self.__balance
  
    acc = Account("홍길동", 1000)
    print(acc.get_balance())  # 접근 가능
    #print(acc.__balance)     # 접근 불가
    ```
2. 상속 (Inheritance)
   - 정의: 기존 클래스(부모, Super class)의 속성과 메소드를 자식(Sub class) 클래스가 물려받는 것
   - 코드 재사용성, 확장성. 자식 클래스에서 재정의(override) 가능
   - super()를 통해 부모 클래스의 메소드를 호출

   ```
   # 상속 예시
   
   class Animal:
       def __init__(self, name):
           self.name = name

       def speak(self):
           print("소리를 냅니다.")

   class Dog(Animal):
       def speak(self):  # Overriding
           print(f"{self.name}가 짖습니다!")

   dog = Dog("바둑이")
   dog.speak()  # 바둑이가 짖습니다!

   class Puppy(Dog):
       def __init__(self, name, age):
           super().__init__(name)  # 부모 생성자 호출
           self.age = age
   ```
  
3. 추상화 (Abstraction)
   - 정의: 핵심적인 부분만 구현, 자주 바뀌는 부분은 비워둠(추상화)
   - 상속을 통해 하위 클래스에서 구체화(override)
   ```
   from abc import ABC, abstractmethod

   class Animal(ABC):
       @abstractmethod
       def speak(self):
           pass  # 추상 메소드

    class Dog(Animal):
         def speak(self):
             print("멍멍!")
   ```
   - ABC (Abstract Base Class): 추상 클래스 선언용
   - @abstractmethod: 하위 클래스에서 반드시 구현
  
4. 다형성 (Polymorphism)
   - 정의: 같은 이름의 메소드라도 객체에 따라 다르게 동작하는 것
   - 여러 클래스가 동일한 메소드 이름을 사용해도 각 클래스마다 다른 동작 수행
   - 코드의 유연성, 확장성
   ```
   class Cat:
       def speak(self):
           print("야옹!")

   class Dog:
       def speak(self):
           print("멍멍!")

   def animal_sound(animal):
       animal.speak()

   cat = Cat()
   dog = Dog()

   animal_sound(cat)  # 야옹!
   animal_sound(dog)  # 멍멍!
   ```

## 특수 메소드 (Magic / Dunder Method)
  - 정의: 객체의 생성과 소멸, 연산자 동작, 출력 형식 등을 커스터마이징
  - 메소드 종류
    - ```__init__(self)```: 인스턴스가 생성될 때 자동 호출되는 생성자(Constructor)
    - ```__del__(self)```: 인스턴스가 메모리에서 제거될 때 호출되는 소멸자(destructor)
    - ```__str__(self)```: print()로 객체를 출력할 때 호출
    - ```__add__(self, other)```: + 연산자 오버로딩
    - ```__len__(self)```: len() 호출 시 동작

  ```
  class Example:
      def __init__(self, name):
          self.name = name
          print(f"{self.name} 생성됨")

      def __del__(self):
          print(f"{self.name} 소멸됨")

  ex = Example("객체1")
  del ex  # __del__ 자동 호출
  ```
