---
title: '[TIL] MySQL BASIC - Condition, JOIN, Sub-Query'
date: 2018-03-26 22:22:26
categories:
- TIL
tags:
- sql
- til
---

##### 2018. 03. 26

## MySQL Basic - Condition, JOIN, Sub-Query 

**Sample Database: world**



### Condition - IF / IFNULL / CASE

**1) IF**

```mysql
IF(조건, 참, 거짓)
```

국가의 인구가 5천만이 넘으면 "big country", 그렇지 않으면 "small country"를 출력하는 "country_scale" 컬럼을 추가

```mysql
SELECT Name, Population,
IF(Population > 50000000, "big country", "small country") AS country_scale
FROM country
```

**2) IFNULL**

```mysql
IFNULL(참, 거짓)
```

독립연도가 없는 데이터는 0으로 출력

```mysql
SELECT IndepYear, IFNULL(IndepYear, 0) AS IndepYear
FROM country
```

**3) CASE**

```Mysql
CASE
    WHEN (condition 1) THEN (result 1)
    WHEN (condition 2) THEN (result 2)
END AS (column name)
```



### JOIN

- `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`

**1) INNER JOIN**

도시 이름과 그 도시가 속한 대륙 이름을 출력

```mysql
SELECT city.Name AS city_name, country.Continent AS continent
FROM country
JOIN city
ON city.CountryCode = country.Code
```

**2) LEFT JOIN**

```mysql
SELECT city.Name AS city, country.Continent AS Continent
FROM city
LEFT JOIN country
ON city.CountryCode = country.Code
```

**3) RIGHT JOIN**

```mysql
SELECT city.Name AS city, country.Continent AS Continent
FROM city
RIGHT JOIN country
ON city.CountryCode = country.Code
```



### Sub-Query

전체 국가 수, 전체 도시 수, 전체 언어 수를 출력 (SELECT절에 사용)

```mysql
SELECT
    (SELECT COUNT(Name) FROM city) AS total_city,
    (SELECT COUNT(Name) FROM country) AS total_country,
    (SELECT COUNT(DISTINCT(Language)) FROM countrylanguage) AS total_language
FROM DUAL
```

인구 800만 이상의 도시의 국가코드, 이름, 도시인구 수를 출력 (FROM절에 사용)

```mysql
SELECT *
FROM
    (SELECT CountryCode, Name, Population
    FROM city
    WHERE Population > 8000000) AS city
JOIN
    (SELECT Code, Name
    FROM country) AS country
ON city.CountryCode = country.Code
```

인구 800만 이상 도시의 국가코드, 국가 이름, 대표 이름을 출력 (WHERE절에 사용)

```mysql
SELECT Code, Name, HeadOfState
FROM country
WHERE Code IN (
    SELECT DISTINCT(CountryCode) FROM city WHERE Population > 8000000
)
```

