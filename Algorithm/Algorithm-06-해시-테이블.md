---
title: '[Algorithm] 06. 해시 테이블'
date: 2018-01-28 20:07:20
categories:
- TIL
- Algorithm
tags:
- python
- til
- algorithm
---

###### 2018. 01. 28

## 해시 테이블

가격 장부를 배열로 구현하면 배열에 있는 각가의 항목은 두 개의 항목으로 이루어져 있음

(사과, 1000), (배, 1500), (우유, 2000)

- 배열을 이름순으로 정렬, 이진 탐색으로 물건의 가격을 찾아내면 O(log n) 시간이 걸림
- O(1) 시간에 물건을 찾아내고 싶음 -> **해시 함수(Hash function)**의 역할



**해시 함수**: 문자열을 받아서 숫자를 반환하는 함수

- 해시 함수는 일관성이 있어야 함
- 다른 단어가 들어가면 다른 숫자가 나와야 함 (best: 모든 단어가 다른 숫자로 나옴)
- 파이썬에서의 해시 테이블: Dictionary 자료형
- 해시 테이블은 Key와 Value를 가짐

```python
book = {}
book['apple'] = 0.67
book['milk'] = 1.49
book['avocado'] = 1.49
print(book)
```

```pytohn
{'avocado': 1.49, 'apple': 0.67, 'milk': 1.49}
```



해시 테이블 사용 예

- 중복된 항목 방지

  투표 여부 파악하기

```python
voted = {}

def check_voter(name):
    if voted.get(name): # dict의 get은 요소가 없으면 None 리턴
        print("돌려 보내세요!")
    else:
        voted[name] = True # voted에 이름이 없으면 이름 추가
        print("투표하게 하세요.")
```

- 해시 테이블을 캐시로 사용하기

```python
cache = {}

def get_page(url):
    if cache.get(url):
        return cache[url] # 캐싱된 자료를 전송
    else:
        data = get_date_from_server(url)
        cache[url] = data # 캐시에 처음으로 자료를 저장
        return data
```

**해시 테이블의 장점**

- 어떤 것과 다르 것 사이의 관계를 모형화할 수 있음
- 중복을 막을 수 있음
- 서버에 작업을 시키지 않고도 자료를 캐싱할 수 있음



**[충돌]**

- 두 개의 키가 같은 공간에 할당되면 나중에 입력된 데이터가 기존 데이터를 덮어씀
- 가장 간단한 해결법은 같은 공간에 여러 개의 키를 연결 리스트로 만들어 놓는 것
- 한 공간에 있는 연결 리스트가 커지면 해시 테이블이 느려짐

**[성능]**

해시 테이블에서 충돌의 피하기 위해서는 다음과 같은 것들이 필요함

- 낮은 사용률
- 좋은 해시 함수

해시 함수의 사용률 = 해시 테이블에 있는 항목의 수 / 해시 테이블에 있는 공간의 수