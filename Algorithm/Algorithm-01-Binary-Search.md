---
title: "[Algorithm] 01. Binary Search"
date: 2018-01-21 13:06:20
categories:
- TIL
- Algorithm
tags:
- python
- til
- algorithm
---

###### 2018. 01. 21

## 이진 탐색 (binary search)

**[단순 탐색 vs 이진 탐색]**
- 100개를 탐색할 때 단순 탐색은 100번, 이진 탐색은 7번 추측
- O(n) vs O(log n)



**[이진 탐색 코드 구현]**
- low, high: 전체 리스트 중 어떤 부분을 탐색해야 하는지 알려줌
- 탐색 범위를 하나로 줄이지 못하면 계속 실행
- 가운데 숫자를 확인
- 아이템을 찾으면 리턴
- 추측한 숫자가 너무 크면 high를 1 감소
- 추측한 숫자가 너무 작으면 low를 1 증가
- 아이템이 리스트에 없으면 None 리턴

```python
def binary_search(lst, item):
    low = 0
    high = len(lst) - 1
    
    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]
        
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
```

```python
my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
```

```
1
None
```



**[핵심 내용]**

- 이진 탐색은 단순 탐색보다 아주 빠름
- O(log n)은 O(n)보다 빠름. 리스트 원소 개수가 증가하면 상대적으로 더 빨라짐
- 알고리즘의 속도는 시간이 아닌 연산 횟수로 측정
- 알고리즘의 시간은 어떻게 증가하는가로 측정
- 알고리즘의 시간은 빅오 표기법으로 나타냄