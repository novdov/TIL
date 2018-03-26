---
title: '[Algorithm] 07. 너비 우선 탐색'
date: 2018-02-02 20:17:52
categories:
- TIL
- Algorithm
tags:
- python
- til
- algorithm
---

###### 2018. 02. 02

## 너비 우선 탐색

**그래프**

- 연결의 집합을 모형화한 것
- 그래프는 정점(node)과 간선(edge)로 이루어짐
- 정점은 여러 개의 다른 정점과 이어질 수 있으며, 바로 이어진 정점을 이웃(neighbor)이라고 함

**너비 우선 탐색**

- 그래프를 대상으로 하는 다른 종류의 탐색 알고리즘
- 다음과 같은 두 가지 종류의 질문에 대답하는 데 도움이 됨
    - 질문 유형 1: 정점 A에서 정점B로 가는 경로가 존재하는가?
    - 질문 유형 2: 정점 A에서 정정B로 가는 최단 경로는 무엇인가?

예) 망고 판매상 탐색
- 친구 중에 망고 판매상이 있을 경우
  - 친구 목록을 살펴봄
    - 각각의 친구가 망고 판매상인지 판단
    - 망고 판매상인 친구 목록을 만나면 종료
- 친구 중에 망고 판매상이 없을 경우

  - 친구의 친구를 살펴봄


- 목록에서 누군가를 찾아볼 때마다 목록에 그 사람의 친구들을 추가
- 목록에 폐기를 추가

망고 판매상에 도달할 때까지 전체 네트워크를 탐색함
- 질문 유형 1: 정점 A에서 정점B로 가는 경로가 존재하는가? (네트워크에 망고 판매상이 있는가?)
- 질문 유형 2: 정점 A에서 정정B로 가는 최단 경로는 무엇인가? (누가 가장 가까운 망고 판매상인가?)

**큐**

- 삽입 (enqueue) / 제거 (dequeue) 두 가지 연산을 가짐
- 선입선출 자료구조 (스택: 후입선출)

**그래프의 구현**

- 그래프는 해시 테이블(dict형)으로 구현함

```pytohn
graph = {}
graph["you"]: ["alice", "bob", "claire"]
```

**알고리즘 구현 방식 정리**

- 확인할 사람의 멍단을 넣을 큐를 준비
- 큐에서 한 사람을 꺼냄
- 이 사람이 망고 판매상인지 확인
- 예 -> 작업 완료 / 아니오 -> 그 사람의 이웃을 모두 큐에 추가
- 반복문
- 만약 큐가 비어 있으면 네트워크에는 망고 판매상이 없음

**파이썬으로 너비 우선 탐색 구현**

```python
from collections import deque # 양방향 큐인 deque 함수를 사용
search_queue = deque()  # 새 큐를 생성
search_queue += graph["you"] # 모든 이웃을 탐색 큐에 추가

while search_queue: # 큐가 비어있지 않으면 계속 실행
    person = search_queue.popleft() # 큐의 첫 번째 사람을 꺼냄
    if person_is_seller(person): # 망고 판매상인지 확인
        print(person + "is a mango seller!") # 망고 판매상일 경우
        return True
    else: 
        search_queue += graph[person] # 망고 판매상이 아니므로 모든 이웃을 탐색 목록에 추가
return False # 여기에 도달했다는 것은 망고 판매상이 없다는 의미
```

```python
def person_is_seller(name):
    return name[-1] == 'm' # 이름이 m으로 끝나는 사람이 망고 판매상 (예)
```

사람을 확인하기 전에 이미 확인한 사람인지 확실해 해두지 않으면 무한 루프에 빠질 수 있음

**[최종 코드]**

```python
def search(name):
    search_queue = deque()  # 새 큐를 생성
    search_queue += graph[name] # 모든 이웃을 탐색 큐에 추가
    searched = [] # 이미 확인한 사람을 추적하기 위함
    
    while search_queue: # 큐가 비어있지 않으면 계속 실행
        person = search_queue.popleft() # 큐의 첫 번째 사람을 꺼냄
        if not person in searched:
            if person_is_seller(person): # 망고 판매상인지 확인
                print(person + "is a mango seller!") # 망고 판매상
                return True
            else: 
                search_queue += graph[person] # 망고 판매상이 아니므로 모든 이웃을 탐색 목록에 추가
                searched.append(person) # 확인한 목록에 추가
    return False # 여기에 도달했다는 것은 망고 판매상이 없다는 의미
```

