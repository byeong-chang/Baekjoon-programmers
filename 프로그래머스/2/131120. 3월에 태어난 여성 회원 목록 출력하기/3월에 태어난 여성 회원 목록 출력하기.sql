-- 코드를 입력하세요
SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH,"%Y-%m-%d") AS DATE_OF_BIRTH
FROM MEMBER_PROFILE 
WHERE TLNO is not NULL and DATE_FORMAT(DATE_OF_BIRTH,"%m") = '03' and GENDER = "W"
ORDER BY MEMBER_ID ASC;
