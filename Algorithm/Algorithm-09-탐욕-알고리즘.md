---
title: '[Algorithm] 09. 탐욕 알고리즘'
date: 2018-03-22 18:48:15
categories:
- TIL
- Algorithm
tags:
- python
- til
- algorithm
---

###### 2018. 03. 22

## 탐욕 알고리즘 (Greedy Algorithm)

> 출처: 
>
> Hello Coding 그림으로 개념을 이해하는 알고리즘(아디드야 바르가바, 김도형 역, 한빛미디어)
>
> [위키피디아 NP](https://goo.gl/V8sxh1)
>
> [위키피디아 탐욕 알고리즘](https://goo.gl/pLVoPp)

탐욕 알고리즘은 최적해를 구하는 데에 사용되는 근사적인 방법으로, 여러 경우 중 하나를 결정해야 할 때마다 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식으로 진행하여 최종적인 해답에 도달한다. 순간마다 하는 선택은 그 순간에 대해 지역적으로는 최적이지만, 그 선택들을 계속 수집하여 최종적(전역적)인 해답을 만들었다고 해서, 그것이 최적이라는 보장은 없다.

- 탐욕 알고리즘은 전역 최적화를 목표로 하지만 실제로는 국소 최적화를 한다.
- NP-완전 문제(NP-Complete)는 빠른 해답이 알려지지 않았다.
- 만약 NP-완전 문제가 주어지면 근사 알고리즘을 쓰는 것이 최선이다.
- 탐욕 알고리즘은 작성하기도 쉽고 빠르기 때문에 좋은 근사 알고리즘이 될 수 있다.

추가: **NP(복잡도)**

- NP는 비결정론적 튜링 기계(NTM)로 다항 시간 안에 풀 수 있는 판정 문제의 집합으로, NP는 비결정론적 다항시간(Non-deterministic Polynomial time)의 약자이다.

예) 라디오 쇼를 시작한다고 가정하자. 미국의 모든 주에 있는 사람에게 라디오 쇼를 들려주고 싶은데, 하나의 방송곡이 커버하는 지연은 한정되어 있기 때문에 전국의 몇 개의 라디오 방송국에 들러 라디오 쇼를 진행할 예정이다. 전국의 모든 사람들이 최소한 한번은 쇼를 들을 수 있도록 하려면 어떤 방송국을 방문해야 할까? 또한 최대한 적은 수의 방송국을 방문해야 한다.

풀이 방법은 다음과 같다.

- 가능한 모든 방송국의 부분 집합을 나열한다. (멱집합) 가능한 부분 집합의 개수는 ![2^{n}](https://latex.codecogs.com/svg.latex?2%5E%7Bn%7D)개이다.
- 이 부분 집합 중에 50개 주 전체를 커버할 수 있으면서 가장 원소의 수가 적은 부분 집합을 고른다.

해당 풀이의 문제는 가능한 부분 집합을 계산하는 데 시간이 오래 걸린다는 점이다. 부분 집합의 수가 ![2^{n}](https://latex.codecogs.com/svg.latex?2%5E%7Bn%7D)개이기 때문에 ![\text O(n^2)](https://latex.codecogs.com/svg.latex?%5Ctext%20O%28n%5E2%29)시간이 걸리기 때문이다. 방송국의 수가 100개만 되어도 전체 실행 시간은 ![4\times10^{21}](https://latex.codecogs.com/svg.latex?%5Cinline%204%5Ctimes10%5E%7B21%7D)년이나 된다.

이 떄는 탐욕 알고리즘을 사용한다.

**[근사 알고리즘]**

- 아직 방송하지 않은 지역 중 가장 많은 지역에 방송할 수 있는 방송국을 선택한다. 이미 방송되고 있는 지역이 일부 포함되어 있어도 상관없다.
- 모든 주에 방송이 될 때까지 선택을 반복한다.

이 경우에 탐욕 알고리즘의 실행 속도는 ![\text O(n^2)](https://latex.codecogs.com/svg.latex?%5Ctext%20O%28n%5E2%29)시간이다.

코드로 나타내면 다음과 같다. (50개의 주 중 일부 주만 사용한다.)

- 방송하고자 하는 주의 목록을 생성한다:  `states_needed`
- 선택된 방송국의 목록도 생성한다:  `stations` (key: 방송국 이름, value: 방송국이 커버하는 주)
- 방문할 방송국의 목록을 저장할 set 생성: `final_stations`

```python
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()

# 고려 대상인 주가 모두 커버될 때까지 반복
while states_needed:
    # 아직 방송이 되지 않는 주 중에서 가장 많은 주를 커버하고 있는 방송국
    best_station = None
    # 아직 방송되지 않은 주 중에서 해당 방송국이 커버하는 주의 집합
    states_covered = set()
    for station, states in stations.items():
        # 아직 방송되지 않는 주 중에서 현재 고려하고 있는 방송국이 커버하는 주의 집합
        covered = states_needed & states
        # 이 방송국이 현재의 best_station보다 더 많은 주를 커버하는지 확인
        if len(covered) > len(states_covered):
            # best_station보다 더 많은 주를 커버한다면 해당 방송국을 best_station으로 갱신
            best_station = station
            # 해당 방송국이 커버하는 주 갱신
            states_covered = covered
    
    # 해당 방송국에서 커버하는 주는 고려 대상이 아니므로 갱신        
    states_needed -= states_covered
    # final_station에 방송국을 추가
    final_stations.add(best_station)
```

**[결과]**

```python
print(final_stations)
```

```
{'kfive', 'ktwo', 'kthree', 'kone'}
```

