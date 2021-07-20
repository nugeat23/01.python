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

delete from usertbl
where userid = 'kkh';   -- 성공

delete from usertbl
where userid = 'kbs';   -- 실패, 자식 테이블에서 kbs를 참조하는 데이터가 있음.

delete from buytbl
where userid = 'kbs';

drop table if exists usertbl2;
create table usertbl2(
    userid char(8)      not null,
    name varchar(10)    not null,
    birthyear int       not null,
    constraint primary key pk_usertbl_userid(userid)
);

-- alter table 테이블명
-- add constaint [제약조건명] primary key(컬럼명)

drop table if exists prodtbl;
create table prodtbl(
    prodcode char(3)    not null,
    prodid   char(4)    not null,
    proddate datetime   not null,
    prodcur  char(10)   null
);

alter table prodtbl
add constraint primary key(prodcode, prodid); -- 복합키

drop table if exists prodtbl;
create table prodtbl(
    prodcode char(3) not null,
    prodid   char(4) not null,
    proddate datetime not null,
    prodcur  char(10) null,
    constraint pk_prodtbl_prodcode_prodid primary key (prodcode, prodid)
);

show index from prodtbl;

show index from usertbl;

DROP TABLE IF EXISTS buyTBL, userTBL;
CREATE TABLE userTBL( 
    userID CHAR(8)      NOT NULL PRIMARY KEY, 
    name VARCHAR(10)    NOT NULL, 
    birthYear INT       NOT NULL 
);
CREATE TABLE buyTBL( 
    num INT AUTO_INCREMENT  NOT NULL PRIMARY KEY , 
    userID CHAR(8)          NOT NULL, 
    prodName CHAR(6)        NOT NULL,
    FOREIGN KEY(userID) REFERENCES userTBL(userID)
);

DROP TABLE IF EXISTS buyTBL;
CREATE TABLE buyTBL(  
    num INT AUTO_INCREMENT  NOT NULL PRIMARY KEY , 
    userID CHAR(8)          NOT NULL, 
    prodName CHAR(6)        NOT NULL,
    CONSTRAINT FK_userTBL_buyTBL FOREIGN KEY(userID) REFERENCES userTBL(userID)
        on update CASCADE
        on delete CASCADE
        -- on delete set null -- 부모가 삭제될 때 null로 설정
);

insert into usertbl
values('kbs','김범수',2000);

insert into buytbl
values(null, 'kbs', '모니터');

select * from buytbl;
-- 부모의 키가 변경되는 경우
-- on update cascade 설정에 의해
-- 자식도 같은 값으로 변경됨

update usertbl
set userid = 'kb'
where userid = 'kbs';

select * from buytbl;

-- 부모의 행이 삭제되는 경우
-- on delete cascade 설정에 의해
-- 참조하는 자식 행도 같이 삭제됨

delete from usertbl
where userid = 'kb';

select * from buytbl;

DROP TABLE IF EXISTS buyTBL;
CREATE TABLE buyTBL( 
    num INT AUTO_INCREMENT  NOT NULL PRIMARY KEY,
    userID CHAR(8)          NOT NULL, 
    prodName CHAR(6)        NOT NULL 
);

ALTER TABLE buyTBL
ADD CONSTRAINT FK_userTBL_buyTBL
FOREIGN KEY (userID) REFERENCES userTBL(userID);

SHOW INDEX FROM buyTBL;

drop table if exists buytbl, usertbl;
create table usertbl(
    userid      char(8)        not null     primary key,
    name        varchar(10)    not null,
    birthyear   int            not null,
    email       char(30)       null,
    constraint AK_email unique (email)
);

insert into usertbl
values
    ('hong','홍길동',2000,'hong@gmail.com'),
    ('go','고길동',2000,null),
    ('micol','마이콜',2000,'micol@gmail.com'),
    ('dooli','둘리',2000,null);

select * from usertbl;

-- email 중복인 경우 에러
insert into usertbl
values ('hong2','홍길동2',2000,'hong@gmail.com');

DROP TABLE IF EXISTS userTBL;
CREATE TABLE userTBL( 
    userID      CHAR(8)     PRIMARY KEY,
    name        VARCHAR(10), 
    birthYear   INT         CHECK (birthYear >= 1900 AND birthYear <= 2020),
    mobile1     CHAR(3)     NULL, 
    CONSTRAINT CK_name CHECK ( name IS NOT NULL) 
);

ALTER TABLE userTbl
ADD CONSTRAINT CK_mobile1
CHECK (mobile1 IN ('010','011','016','017','018','019'));

insert into usertbl
values ('hong','홍길동',2000, '010'); -- 성공

insert into usertbl
values ('hong2','홍길동2',2021, '010'); -- 실패

DROP TABLE IF EXISTS userTBL;
CREATE TABLE userTBL(
    userID      char(8)     NOT NULL    PRIMARY KEY, 
    name        varchar(10) NOT NULL, 
    birthYear   int NOT     NULL        DEFAULT -1,
    addr        char(2)     NOT NULL    DEFAULT '서울',
    mobile1     char(3)     NULL, 
    mobile2     char(8)     NULL, 
    height      smallint    NULL        DEFAULT 170, 
    mDate       date        NULL        DEFAULT sysdate()
);

insert into usertbl(userid, name)
values ('hong','홍길동');

select * from usertbl;

create temporary table usertbl; -- 임시 테이블