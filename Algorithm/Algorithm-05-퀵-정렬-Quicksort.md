---
title: '[Algorithm] 05. 퀵 정렬(Quicksort)'
date: 2018-01-26 18:06:51
categories:
- TIL
- Algorithm
tags:
- python
- til
- algorithm
---

###### 2018. 01. 26

## 퀵 정렬 (Quicksort)

- 분할 정복을 사용
- 기본 단계: 정렬할 필요 없는 배열 (빈 배열, 원소가 하나인 배역)

```python
def quicksort(array):
    if len(array) < 2:
        return array
```

- 원소가 두 개인 경우
  - 첫 번쨰 원소가 두 번째 원소보다 작은지 확인
  - 첫 번째 원소가 두 번째 원소보다 크다면 두 원소를 교환
- 원소가 세 개인 경우
  - 기준 원소(pivot)를 선택
  - 모든 원소를 기준 원소보다 작은 원소와 큰 원소로 분류(분할, partitioning)
  - 하위 배열에 대해서도 원소가 두 개인 경우와 같은 정렬 사용
  - 하위 배열 + 기준 원소 + 하위 배열
- 위의 과정을 기본 단계를 만날 때까지 반복

```python
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        
        return quicksort(less) + [pivot] + quicksort(greater)
```

