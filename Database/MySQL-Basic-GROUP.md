---
title: '[TIL] MySQL Basic - GROUP'
date: 2018-03-22 11:25:13
categories:
- TIL
tags:
- sql
- til
---

###### 2018. 03. 22

## MySQL Basic - GROUP

**Sample Database**: [world, sakila](https://dev.mysql.com/doc/index-other.html)

- tables of sakila: actor, addressm category, city, country, customer, film, film_actor, file_category, file_text, inventory, language, payment, rental, staff, store

### GROUP

**1) GROUP BY**

여러 개의 동일한 데이터를 가지는 특정 컬럼을 합쳐준다. SQL에는 아래와 같은 그룹함수가 있다.

`COUNT`, `MIN`, `MAX`, `SUM`, `AVG`

- `COUNT`

payment 테이블에서 staff_id 당 몇 건의 payment가 발생했는지 조회

```mysql
SELECT staff_id, COUNT(amount) AS count
FROM payment
GROUP BY staff_id
```

- `MIN`

각 staff_id당 payment 최솟값 조회

```mysql
SELECT staff_id, MIN(amount) AS min
FROM payment
GROUP BY staff_id
```

- `MAX`

각 staff_id당 payment 최댓값 조회

```mysql
SELECT staff_id, MAX(amount) AS max
FROM payment
GROUP BY staff_id
```

- `SUM`

각 staff_id당 payment 합 조회

```mysql
SELECT staff_id, SUM(amount) AS sum
FROM payment
GROUP BY staff_id
```

- `AVG`

각 staff_id당 payment 평균 조회

```mysql
SELECT staff_id, AVG(amount) AS avg
FROM payment
GROUP BY staff_id
```

**2) HAVING**

GROUP BY로 반환되는 결과에 조건을 줄 수 있다.

- 대륙별 전체인구를 구하고 인구수 5억 이상인 대륙만 조회

```mysql
SELECT Continent, SUM(Population) AS Population 
FROM country
GROUP BY Continent
HAVING Population >= 500000000
```

- 대륙별 평균 인구수, 평균 GNP, 1인당 GNP를 조회한 결과에서 1인당 GNP가 0.01 이상인 데이터를 조회하고 1인당 GNP를 내림차순으로 정렬

```mysql
SELECT Continent, AVG(Population) AS Population, AVG(GNP) AS GNP,
AVG(GNP) / AVG(Population) * 1000 AS AVG
FROM country
WHERE GNP != 0 AND Population != 0
GROUP BY Continent
HAVING AVG > 0.01
ORDER BY AVG DESC
```

