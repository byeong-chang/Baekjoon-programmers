-- 코드를 작성해주세요
SELECT CONCAT(ceil(month(DIFFERENTIATION_DATE)/3),"Q") as QUARTER, count(ID) as ECOLI_COUNT
FROM ECOLI_DATA 
GROUP BY QUARTER
ORDER BY QUARTER