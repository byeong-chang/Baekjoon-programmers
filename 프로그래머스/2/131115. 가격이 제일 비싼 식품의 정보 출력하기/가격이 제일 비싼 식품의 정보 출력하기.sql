-- 코드를 입력하세요
SELECT PRODUCT_ID,PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE
FROM FOOD_PRODUCT
WHERE PRICE = 
(SELECT max(PRICE) FROM FOOD_PRODUCT)


# P0051	맛있는배추김치	CD_KC00001	김치	19000