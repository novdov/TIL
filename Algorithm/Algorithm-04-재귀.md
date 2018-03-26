---
title: '[Algorithm] 04. 재귀(Recursion)'
date: 2018-01-25 20:08:17
categories:
- TIL
- Algorithm
tags:
- python
- til
- algorithm
---

###### 2018. 01. 25

## 재귀

**[재귀]**

**함수가 자기 자신을 호출하는 것**

예) 여러 상자가 들어있는 큰 상자 속에서 열쇠를 찾을 때

- 첫 번째 방법 (반복문)

  1) 내부를 확인할 상자를 쌓아놓는다.
  2) 상자를 하나 집어서 내부를 살핀다.
  3) 만약 안에 상자가 있다면 꺼내서 나중에 확인할 상자 더미에 놓는다.
  4) 만약 열쇠가 있으면 작업 종료
  4) 반복

  - 코드 예시

```python
def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                plie.aplpend(item)
            elif item.is_a_key():
                print("열쇠를 찾았어요!")
```

- 두 번째 방법 (재귀)

  1) 상자 안을 확인한다.
  2) 만약 상자를 발견하면 1단계로 간다.
  3) 만약 열쇠를 발견하면 작업 종료

  - 코드 예시

```python
def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item) # 함수 반복
        elif item.is_a_key():
            print("열쇠를 찾았어요!")
```

재귀 함수는 무한 루프에 빠질 가능성이 큼

[무한 루프 예]

```python
def countdown(i):
    print(i)
    countdown(i-1)
```

위의 함수는 i-1로 계속해서 함수가 실행된다. 무한 루프를 막기 위해 브레이크를 걸어주어야 한다.

```python
def countdown(i):
    print(i)
    if i <= 1: # 기본 단계
        return
	else: # 재귀 단계
        countdown(i-1) 
```

재귀 함수는 기본 단계(base case)와 재귀 단계(recursive case)로 나누어져 있음. 재귀 단계는 함수가 자기 자신을 호출하는 단계. 기본 단계는 함수가 자기 자신을 호출하지 않는 경우, 즉 무한 루프에 빠지지 않게 하는 부분.

**[스택]**

예) 접착식 메모지

- 새 항목을 추가할 때는 기존의 목록에 덧붙임 (push)
- 항목을 읽을 때는 가장 위에 있는 항목만 읽고 떼어낼 수 있음 (pop)

컴퓨터는 호출 스택이라는 스택을 사용함

예)

```python
def greet(name):
    print("hello,   " + name + "!")
    greet2(name)
    print("getting ready to say bye...")
    bye()
    
def greet2(name):
    print("how are you, " + name + "?")
    
def bye():
    print("ok bye!")
```

- `greet('maggie')`를 선언하면 컴퓨터에 `greet`함수 호출을 위한 메모리가 할당되며, `name`이란 변수의 값이 `maggie`란 것도 함께 저장됨
- 함수 중간의 `greet2('maggie')` 호출을 위해 `greet2('maggie')`가 스택으로 쌓아짐. "how are you maggie?" 반환 후 `pop`연산으로 사라짐.
- 다시 `bye()`함수가 스택으로 쌓아지며, "ok bye!"를 실행한 후 사라짐

이런 방식으로 여러 개의 함수를 호출하면서 함수에 사용되는 변수를 저장하는 스택을 호출 스택이라고 함

**[재귀 함수에서의 호출 스택 사용]**

예) 팩토리얼 함수

```python
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)
```

`fact(3)`을 호출하면 `fact(3)`, `fact(2)`, `fact(1)`이 차례로 스택에 쌓이며, `fact(1)`부터 차례로 실행되며 스택에서 없어진다.

**[정리]**

- 재귀는 함수가 스스로를 호출하는 것
- 모든 재귀 함수는 기본 단계와 재귀 단계라는 두 부분으로 나누어져 있음
- 스택에는 push와 pop 두 가지 연산이 존재
- 모든 함수 호출은 호출 스택을 사용
- 호출 스택은 너무 커져서 메모리를 심하게 소비할 수도 있음