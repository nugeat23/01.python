select sum(amount) '총 구매 개수'
from buytbl;

SELECT avg(amount) '평균 구매 개수'
from buytbl;

SELECT userid,avg(amount) '평균 구매 개수'
from buytbl
GROUP BY userid;

SELECT count(*)
from usertbl;

SELECT count(mobile1) '휴대폰이 있는 사용자'
from usertbl;