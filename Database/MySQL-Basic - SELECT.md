---
title: '[TIL] MySQL Basic - SELECT'
date: 2018-03-21 22:00:08
categories:
- TIL
tags:
- sql
- til
---

###### 2018. 03. 21

## MySQL Basic - SELECT

**Sample Database**: [world database](https://dev.mysql.com/doc/index-other.html)

- table: city, country, countrylanguage

**사용 프로그램: Sequel Pro**

### SELECT

**1) 기본 쿼리문법**

```mysql
SELECT <컬럼 1>, <컬럼 2>, ....
FROM <테이블>
```

- country 전체 컬럼 데이터 조회

```mysql
SELECT *
FROM country
```

- Name, Continent, Region 컬럼 조회

```mysql
SELECT Name, Continent, Region
FROM country
```

**2) ALIAS**

alias를 이용해서 컬럼명을 변경할 수 있다.

```mysql
SELECT Name AS "country_name", SurfaceArea AS "surface"
FROM country
```

**3) DISTINCT**

특정 컬럼의 중복 데이터를 제거할 수 있다.

```mysql
SELECT DISTINCT(Continent)
FROM country
```

**4) WHERE**

`WHERE`절을 이용해 검색 조건을 추가할 수 있다.

```mysql
-- 인구 5000000 이상 도시 조회
SELECT Name, Population
FROM city
WHERE Population >= 5000000

-- 인구 1000000 이상, 5000000 이하 도시 조회
SELECT Name, Population
FROM city
WHERE Population BETWEEN 1000000 AND 5000000

-- 위의 쿼리문은 아래와 동일하다. (BETWEEN 사용 X)
SELECT Name, Population
FROM city
WHERE Population >= 1000000 AND Population <= 5000000
```

**5) ORDER BY**

특정 컬럼으로 데이터 정렬이 가능하다.

```mysql
-- 인구수 내림차순 정렬
SELECT Name, Population
FROM city
ORDER BY Population DESC

-- 인구수 오름차순 정렬 (ASC는 생략 가능)
SELECT Name, Population
FROM city
ORDER BY Population ASC
```

**6) CONCAT**

컬럼을 합쳐 새로운 컬럼으로 보여줄 수 있다.

```mysql
SELECT CONCAT(Name, "(", Continent, ")") AS name_continent
FROM country
```

**7) LIKE**

특정 문자열이 들어간 데이터를 조회할 수 있다. `%`는 아무 문자나 올 수 있음을 의미한다. `NOT LIKE`로 특정 문자가 들어가지 않은 데이터를 조회할 수도 있다.

```mysql
-- 정부 형태에 "Republic"이 포함된 국가 조회
SELECT Name, Continent, GovernmentForm
FROM country
WHERE GovernmentForm LIKE "%Republic%"

-- 정부 형태에 "Republic"이 포함되지 않은 국가 조회
SELECT Name, Continent, GovernmentForm
FROM country
WHERE GovernmentForm NOT LIKE "%Republic%"
```

**8) IN**

여러 개의 조건을 만족하는 데이터를 조회하고 싶을 때 사용한다. `WHERE`절의 여러 조건을 간단하게 만들 수 있다.

```mysql
-- 스페인어, 한국어, 영어를 사용하는 국가 조회
SELECT CountryCode, Language, Percentage
FROM countrylanguage
WHERE Language IN ("Spanish", "Korean", "English")
```

**9) LIMIT**

조회하는 데이터의 수를 제한할 수 있다. (조회 시작 인덱스, 조회 개수)로 사용한다. 인덱스는 0부터 시작한다.

```mysql
-- 영어 사용률이 높은 국가 5위부터 10위까지 조회
SELECT CountryCode, Language, Percentage
FROM countrylanguage
WHERE Language="English"
ORDER BY Percentage DESC
LIMIT 4, 6
```

