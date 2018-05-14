---
title: '[Algorithm] 선택정렬: 가장 많이 들은 음악 순으로 정렬하기'
date: 2018-05-08 23:11:04
categories:
- TIL
- Algorithm
tags:
- python
- til
- algorithm
---

## 선택정렬: 가장 많이 들은 음악 순으로 정렬하기 

해당 코드는[ "Hello Coding 그림으로 개념을 이해하는 알고리즘 (아디트야 바르가바 저, 김도형 역)"](http://www.aladin.co.kr/shop/wproduct.aspx?ItemId=105982502) 2장 선택 정렬의 예시인 "음악 재생 횟수 목록을 가장 많이 들은 순으로 정렬하기"를 구현한 코드입니다. 책에는 해당 예시에 대한 코드는 나오지 않습니다.



코드 구현은 다음과 같다. 1) 원 목록에서 가장 많이 들은 항목의 인덱스를 리턴하는 함수 구현 2) 해당 함수와 `pop`을 이용해 정렬된 새 목록을 리턴하는 함수 구현. 여기서는 입력 목록이 `dict` 일 때와 `list of tuple`인 경우 2가지에 대해 구현했지만 리턴 형태는 모두 `list of tuple`이다. 이는 파이썬이 `dict` 타입을 리턴할 때 key를 알파벳 순서로 정렬해버리기 때문이다.  또한 파이썬은 자체적으로 stack을 제공하지 않기 때문에 리스트 형태로 구현해야 한다.

해당 사항에 대한 Quora: [Why does the dict function return values in alphabetical order?](https://www.quora.com/Why-does-the-dict-function-return-values-in-alphabetical-order)



### 1. 입력 재생 목록이 `dict` 형태일 때

재생 목록이 `dict` 형태일 때는 keys를 떼어내 해당 keys를 이용해 value를 호출해 구현했다.

```python
# 가장 많이 들은 음악의 가수를 리턴하는 함수
def find_most_played(playlist):
    keys = list(playlist.keys())
    # keys를 이용해 values를 호출
    most_played = playlist[keys[0]]
    # 시작 시 인덱스는 0
    most_played_idx = 0
    for i in range(1, len(playlist)):
        # 0번 째 이후의 values가 처음보다 크다면
        if playlist[keys[i]] > most_played:
            # 해당 인덱스가 가장 많이 들은 음악의 인덱스
            most_played = playlist[keys[i]]
            most_played_idx = i
    # 리턴하는 값은 가장 많이 들은 음악의 가수        
    return keys[most_played_idx]

# 가장 많이 들은 음악부터 정렬된 list of tuple을 리턴하는 함수
def sort_most_played(playlist):
    keys = list(playlist.keys())
    # 정렬된 (keys, values)를 담을 리스트
    new_playlist = []
    for i in range(len(playlist)):
        most_played = find_most_played(playlist)
        # index 메서드를 사용해 가장 많이 들은 음악의 인덱스
        idx = keys.index(most_played)
        # 많이 들은 음악과 가수부터 리스트에 추가한다.
        new_playlist.append((most_played, playlist[most_played]))
        # 리스트에 추가된 항목은 제거한다
        # 파이썬의 dict에도 pop 메서드가 존재한다.
        playlist.pop(most_played)
    return new_playlist
```

실행 결과는 다음과 같다.

```python
from pprint import pprint

playlist = {
    'RADIOHEAD': 156,
    'KISHORE KUMAR': 141,
    'THE BLACK KEYS': 35,
    'NEUTRAL MILK HOTEL': 94,
    'BECK': 88,
    'THE STROKES': 61,
    'WILCO': 111
}

sorted_playlist = sort_most_played(playlist)
pprint(sorted_playlist)
```

```python
[('RADIOHEAD', 156),
 ('KISHORE KUMAR', 141),
 ('WILCO', 111),
 ('NEUTRAL MILK HOTEL', 94),
 ('BECK', 88),
 ('THE STROKES', 61),
 ('THE BLACK KEYS', 35)]
```



### 2. 입력 재생 목록이 `list of tuple`일 때

이 경우에도 1번의 예와 거의 동일하지만, 훨씬 간단하게 구현했다.

```python
# 가장 많이 들은 음악의 인덱스(tuple의 인덱스)를 리턴하는 함수
# 입력 리스트의 각 value는 (가수, 재생 횟수)의 tuple로 되어있다.
def find_most_played(playlist):
    most_played = playlist[0][1]
    most_played_idx = 0
    for i in range(1, len(playlist)):
        if playlist[i][1] > most_played:
            most_played = playlist[i][1]
            most_played_idx = i
    return most_played_idx

# 가장 많이 들은 음악부터 정렬된 list of tuple을 리턴하는 함수
def sort_most_played(playlist):
    new_playlist = []
    for i in range(len(playlist)):
        most_played = find_most_played(playlist)
        # 간단하게 입력 리스트의 tuple을 그대로 새 리스트에 추가하면 된다.
        new_playlist.append(playlist.pop(most_played))        
    return new_playlist
```

실행 결과는 다음과 같다.

```python
playlist = [('RADIOHEAD', 156),
            ('KISHORE KUMAR', 141),
            ('THE BLACK KEYS', 35),
            ('NEUTRAL MILK HOTEL', 94),
            ('BECK', 88),
            ('THE STROKES', 61),
            ('WILCO', 111)]

sorted_playlist = sort_most_played(playlist)
pprint(sorted_playlist)
```

```python
[('RADIOHEAD', 156),
 ('KISHORE KUMAR', 141),
 ('WILCO', 111),
 ('NEUTRAL MILK HOTEL', 94),
 ('BECK', 88),
 ('THE STROKES', 61),
 ('THE BLACK KEYS', 35)]
```

