---
title: '[Algorithm] 08. 다익스트라 알고리즘'
date: 2018-02-06 14:07:52
categories:
- TIL
- Algorithm
tags:
- python
- til
- algorithm
---

###### 2018. 02. 06

## 다익스트라 알고리즘

- 그래프의 간선에 가중치를 둔 가중 그래프
- 가중 그래프에서 X까지의 최단 경로를 구하는 다익스트라 알고리즘
- 다익스트라 알고리즘은 모든 가중치가 양수일 때만 정상적으로 동작
- 가중치가 음수이면 벨만-포드 알고리즘 사용
- 너비 우선 탐색은 가중치가 없는 균일 그래프에서 최단 경로를 계산하는 데 사용



**[다익스트라 알고리즘 단계]**

1. 가장 가격이 싼 정점, 도달하는 데 시간이 가장 적게 걸리는 정점 탐색
2. 해당 정점의 이웃 정점에 대해 현재의 가격보다 더 싼 경로가 존재하는지 확인. 존재 시 가격 수정
3. 그래프 상의 모든 정점에 대해 이러한 작업 반복
4. 최종 경로 계산

**[파이썬으로 다익스트라 알고리즘 구현]**

``` python
node = find_lowest_cost_node(costs) # 아직 처리하지 않은 가장 싼 정점 탐색
while node is not None: # 모든 정점을 처리하면 반복문 종료
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys(): # 모든 이웃에 대해 반복
        new_cost = cost + neighbors[n]
        if costs[n] < new_cost: # 정점을 지나는 것이 가격이 더 싸면 가격 갱신
            costs[n] = new_cost
            parents[n] = node # 부모를 이 정점으로 새로 설정
        processed.append(node) # 정점 처리 사실 기록
        node = find_lowest_cost_node(costs) # 다음으로 처리할 정점을 찾아 반복
        
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs: # 모든 정점을 확인
        cost = costs[node] # 아직 처리하지 않은 정점 중 더 싼 것이 있으면
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost # 새로운 최저 정점으로 설정
            lowest_cost_node = node
        return lowest_cost_node
```

