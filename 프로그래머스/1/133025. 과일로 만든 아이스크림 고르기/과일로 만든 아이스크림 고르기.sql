-- 코드를 입력하세요
SELECT ICECREAM_INFO.FLAVOR
FROM ICECREAM_INFO, FIRST_HALF 
WHERE INGREDIENT_TYPE = "fruit_based" and ICECREAM_INFO.FLAVOR = FIRST_HALF.FLAVOR and TOTAL_ORDER > 3000
ORDER BY TOTAL_ORDER DESC