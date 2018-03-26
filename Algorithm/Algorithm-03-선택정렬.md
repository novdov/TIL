---
title: '[Algorithm] 03. 선택정렬'
date: 2018-01-22 21:18:49
categories:
- TIL
- Algorithm
tags:
- python
- til
- algorithm
---

###### 2018. 01. 22

## 선택 정렬

**선택 정렬 코드 구현**

[배열을 작은 정수에서 큰 정수 순서로 정렬하는 코드]

```python
def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
```

[위의 함수를 이용한 선택 정렬 코드]

```python
def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr
```

