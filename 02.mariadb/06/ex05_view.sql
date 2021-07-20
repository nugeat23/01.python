drop table if exists buytbl, usertbl;

create table usertbl(             -- 회원 테이블
    userID char(8)      primary key, -- 사용자 아이디
    name varchar(10)    not null, -- 이름
    birthYear int       not null, -- 출생연도
    addr char(2)        not null, -- 지역(경기,서울,경남 등으로 글자만 입력)
    mobile1 char(3)     null,     -- 휴대폰의국번(011, 016, 017, 018, 019, 010 등)
    mobile2 char(8)     null,     -- 휴대폰의 나머지 전화번호(하이픈 제외)
    height smallint     null,     -- 키
    mDate date          null      -- 회원 가입일
);

-- select * from usertbl;

create table buytbl(              -- 구매 테이블
    num int             AUTO_INCREMENT primary key, -- 순번(PK)
    userid char(8)      not null, -- 아이디(FK)
    prodName char(6)    not null, -- 물품명
    groupName char(4)   null,     -- 분류
    price int           not null, -- 단가
    amount smallint     not null,  -- 수량
    FOREIGN KEY(userid) REFERENCES usertbl(userid)
);

-- select * from buytbl;

INSERT INTO userTBL VALUES
('LSG', '이승기', 1987, '서울', '011', '1111111', 182, '2008-8-8');
INSERT INTO userTBL VALUES
('KBS', '김범수', 1979, '경남', '011', '2222222', 173, '2012-4-4');
INSERT INTO userTBL VALUES
('KKH', '김경호', 1971, '전남', '019', '3333333', 177, '2007-7-7');
INSERT INTO userTBL VALUES
('JYP', '박진영', 1971, '전남', '019', '3333333', 177, '2007-7-7');


INSERT INTO buyTBL VALUES(NULL, 'KBS', '운동화', NULL , 30, 2);
INSERT INTO buyTBL VALUES(NULL, 'KBS', '노트북', '전자', 1000, 1);
INSERT INTO buyTBL VALUES(NULL, 'JYP', '모니터', '전자', 200, 1);


create view v_usertbl
as
    select userid, name, addr from usertbl;

select * from v_usertbl;

-- drop view v_usertbl;

-- join select 문에 대해서 view 생성하기
create or replace view v_usertbl
as
select U.userid, U.name, B.prodname, U.addr,
        concat(U.mobile1,'-',U.mobile2)  as '연락처'

from usertbl U
    inner join buytbl B
        on U.userid = B.userid;

select * from v_usertbl
where name = '김범수';



create or replace view v_userbuytbl
as
    select U.userid as 'USER ID',
           U.name as 'USER NAME',
           B.prodname as 'PRODUCT NAME',
           U.addr,
           concat(U.mobile1,U.mobile2)  as 'MOBILE PHONE'
    from usertbl U
inner join buytbl B
    on U.userid = B.userid;

select * from v_usertbl;

select 'USER ID', 'USER NAME' from v_userbuytbl;
select `USER ID`, `USER NAME` from v_userbuytbl; -- 컬럼명에 space를 주고 싶을 땐 ``으로 표현