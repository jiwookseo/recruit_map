# Database settings

## DB Schema

### Company

| field        | type  | required | feature                                        |
| ------------ | ----- | -------- | ---------------------------------------------- |
| id           | int   | required | primary key                                    |
| name         | char  | required | 기업명                                         |
| href         | url   | option   | 홈페이지 주소                                  |
| saram_url    | url   | option   | 사람인 기업 정보 url                           |
| avg_salary   | int   | required | 평균 연봉, \* 만원 / 정보 없으면 0             |
| start_salary | int   | required | 대졸 초봉, * 만원 / 정보 없으면 0              |
| address      | char  | required | 기업 상세주소                                  |
| scale        | char  | required | 기업 규모, 분류                                |
| lat          | float | required | latitude, 위도                                 |
| lng          | float | required | longitude, 경도                                |
| viewport     | json  | required | {northeast: {lat, lng}, southwest: {lat, lng}} |
| place_id     | float | required | google map place id                            |
| ind_code     | char  | required | 업종 코드(쉼표로 구분, **하단 참고**)          |
| ind_name     | char  | required | 업종                                           |
| ind_key_code | char  | required | 업종 키워드 코드 (쉼표로 구분, **하단 참고**)  |

&nbsp;


### Job

| field | type | required | feature     |
| ----- | ---- | -------- | ----------- |
| id    | int  | required | primary key |
| company | FK | required | 채용 기업, foreign key |
| title | char | required | 채용 공고 제목 |
| saram_url | url | required | 사람인 공고 정보 url |
| job          | char      | required | 직종(쉼표로 구분)                                            |
| exp_min      | int       | required | 최소 경력                                               |
| exp_max      | int       | required | 최대 경력                                               |
| edu_code     | char      | required | 학력 코드(쉼표로 구분, **하단 참고**)                   |
| edu_name     | char      | required | 학력                                                    |
| open         | datetime | required | 접수 시작일                                             |
| close        | datetime | required | 접수 마감일                                             |
| close_type   | int       | required | 1: 접수 마감일<br />2: 채용시<br />3: 상시<br />4: 수시 |

&nbsp;

### Station

| field    | type | required | feature                                        |
| -------- | ---- | -------- | ---------------------------------------------- |
| id       | int  | required | primary key                                    |
| name     | char | required | 역명                                           |
| line     | char | required | 노선 번호(쉼표로 구분, **하단 참고**)          |
| address  | char | required | 역 상세주소                                    |
| lat      | int  | required | latitude, 위도                                 |
| lng      | int  | required | longitude, 경도                                |
| viewport | json | required | {northeast: {lat, lng}, southwest: {lat, lng}} |
| place_id | char | required | google map place id                            |

&nbsp;

### Route

| field   | type        | required | feature                      |
| ------- | ----------- | -------- | ---------------------------- |
| id      | int         | required | primary key                  |
| time    | int         | required | 역에서 기업까지 소요시간(분) |
| company | foreign key | required |                              |
| station | foreign key | required |                              |

&nbsp;

### User

| field           | type         | required | feature                            |
| --------------- | ------------ | -------- | ---------------------------------- |
| id              | int          | required | primary key                        |
| pw              | password     | required | 비밀번호                           |
| email           | email        | required | 이메일                             |
| liked_companies | many to many |          | 찜한 기업, related_name=like_users |

&nbsp;

## Code Table

### 학력

- #### 학력코드표

  | 코드 | 학력                |
  | :--- | :------------------ |
  | 0    | 학력무관            |
  | 1    | 고등학교졸업        |
  | 2    | 대학졸업(2,3년)     |
  | 3    | 대학교졸업(4년)     |
  | 4    | 석사졸업            |
  | 5    | 박사졸업            |
  | 6    | 고등학교졸업이상    |
  | 7    | 대학졸업(2,3년)이상 |
  | 8    | 대학교졸업(4년)이상 |
  | 9    | 석사졸업이상        |

&nbsp;

### 산업/업종

- #### 업종 코드표

  | 코드 | 산업/업종명          | 상위코드 |
  | :--- | :------------------- | :------- |
  | 301  | 솔루션·SI·ERP·CRM    | 3        |
  | 302  | 웹에이젼시           | 3        |
  | 304  | 쇼핑몰·오픈마켓      | 3        |
  | 305  | 포털·인터넷·컨텐츠   | 3        |
  | 306  | 네트워크·통신·모바일 | 3        |
  | 307  | 하드웨어·장비        | 3        |
  | 308  | 정보보안·백신        | 3        |
  | 313  | IT컨설팅             | 3        |
  | 314  | 게임                 | 3        |

* #### 업종 키워드

  | 코드  | 업종키워드명    |
  | ----- | --------------- |
  | 30101 | SI·시스템통합   |
  | 30102 | ERP             |
  | 30103 | CRM             |
  | 30104 | DRM             |
  | 30105 | DW              |
  | 30106 | KMS             |
  | 30107 | NI·네트워크통합 |
  | 30108 | DataMining      |
  | 30110 | OLAP            |
  | 30111 | SCM             |
  | 30112 | DBMS            |
  | 30113 | 시스템관리      |
  | 30114 | BPR             |
  | 30115 | BSC             |
  | 30116 | 솔루션업체      |
  | 30117 | ASP             |
  | 30118 | 소프트웨어개발  |
  | 30119 | SEM             |
  | 30120 | SM              |
  | 30201 | 웹에이전시      |
  | 30202 | 웹프로덕션      |
  | 30203 | 웹스튜디오      |
  | 30401 | 전자상거래      |
  | 30403 | 쇼핑몰          |
  | 30404 | B2B             |
  | 30405 | 옥션·경매       |
  | 30406 | B2C             |
  | 30407 | 오픈마켓        |
  | 30408 | 가격비교        |
  | 30501 | 종합포털        |
  | 30502 | 컨텐츠제공      |
  | 30503 | 취업포털        |
  | 30504 | 여성포털        |
  | 30505 | 인터넷영화      |
  | 30506 | 인터넷방송      |
  | 30507 | 인터넷금융      |
  | 30508 | 인터넷교육      |
  | 30509 | 인터넷만화      |
  | 30510 | 인터넷부동산    |
  | 30512 | 게임포털        |
  | 30513 | 인터넷여행      |
  | 30514 | 인터넷법률      |
  | 30515 | 인터넷생활정보  |
  | 30516 | 커뮤니티        |
  | 30517 | 인터넷뉴스·신문 |
  | 30518 | 인터넷건강·의학 |
  | 30519 | 종교포털        |
  | 30520 | 인터넷서점      |
  | 30521 | 인터넷음악      |
  | 30601 | 네트웍구축      |
  | 30602 | 통신            |
  | 30603 | 텔레콤          |
  | 30607 | 와이브로        |
  | 30608 | 모바일          |
  | 30609 | 유비쿼터스      |
  | 30610 | 블루투스        |
  | 30612 | WIPI            |
  | 30613 | WAP             |
  | 30614 | PDA·스마트폰    |
  | 30615 | 모바일게임      |
  | 30616 | 뱅킹·빌링       |
  | 30617 | CDN             |
  | 30618 | 웹호스팅        |
  | 30619 | 인터넷전화      |
  | 30620 | 아이폰          |
  | 30621 | 안드로이드      |
  | 30622 | 윈도우모바일    |
  | 30623 | 텔레매틱스      |
  | 30624 | HDML            |
  | 30625 | mHTML           |
  | 30626 | cHTML           |
  | 30627 | GSM·GVM         |
  | 30628 | SKVM            |
  | 30629 | BREW            |
  | 30630 | CDMA            |
  | 30631 | 모바일APP       |
  | 30632 | Phone           |
  | 30633 | 무선통신        |
  | 30701 | 하드웨어        |
  | 30702 | 펌웨어          |
  | 30703 | 장비구축        |
  | 30704 | 유지보수        |
  | 30705 | 코덱·인코딩     |
  | 30706 | 스토리지        |
  | 30707 | AS              |
  | 30801 | 보안            |
  | 30802 | 백신            |
  | 30803 | 방화벽          |
  | 30804 | IDS·IPS         |
  | 30805 | 보안컨설팅      |
  | 30806 | ESM             |
  | 30808 | SSL             |
  | 30809 | 바이러스        |
  | 30810 | 네트워크보안    |
  | 30811 | 정보보안        |
  | 30812 | 해킹            |
  | 30813 | 스팸·웜         |
  | 30814 | 보안ASP         |
  | 31301 | IT컨설팅        |
  | 31302 | 인큐베이팅      |
  | 31303 | 셋업            |
  | 31304 | IFRS            |
  | 31305 | SAP             |
  | 31306 | ERP             |
  | 31307 | SCM             |
  | 31308 | CRM             |
  | 31309 | Oracle          |
  | 31310 | BPM             |
  | 31311 | KMS             |
  | 31312 | DW              |
  | 31401 | 게임개발        |
  | 31402 | 게임기획·마케팅 |
  | 31403 | 게임디자인      |
  | 31404 | 게임음향        |
  | 31405 | 게임운영        |
  | 31406 | 게임            |
  | 31407 | GM·CS           |
  | 31408 | 게임시나리오    |
  | 31409 | 3D온라인게임    |
  | 31410 | RPG             |
  | 31411 | 2D온라인게임    |
  | 31412 | Flash게임       |
  | 31413 | 웹게임          |
  | 31414 | 베타테스터      |

&nbsp;

### 지하철

* #### 노선코드

  | 코드  | 노선명       |
  | ----- | ------------ |
  | 1 - 9 | 1 - 9 호선   |
  | A     | 공항철도     |
  | B     | 분당선       |
  | E     | 용인경전철   |
  | G     | 경춘선       |
  | I1    | 인천1호선    |
  | I2    | 인천2호선    |
  | K     | 경의중앙선   |
  | KK    | 경강선       |
  | S     | 신분당선     |
  | SU    | 수인선       |
  | U     | 의정부경전철 |

  