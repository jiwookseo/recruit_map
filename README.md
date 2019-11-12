![logo image](assets/image/og_image.png)

# 길잡이 <small>Recruit Map</small>

### Service

- Google Maps API 를 이용한 통근 시간 정보와 취업 컨텐츠를 지도에서 보여주는 통합 서비스

#### Architecture

- 검색엔진 최적화를 위한 Server-side rendering 클라이언트

  Nuxt.js 를 이용한 SSR / SPA 클라이언트 구현

- 서버와 클라이언트의 완전한 분리

  DRF 를 이용해 HATEOAS 를 적용한 self-descriptive한 RESTful API 구현

&nbsp;

### Use our service. [http://recruitmap.ninja/](http://recruitmap.ninja/)

![service_gif](https://media.giphy.com/media/cm5DC2PAKRN6kaHKZh/giphy.gif)

&nbsp;

## 1. Detail Feature

#### 1) 지도를 통한 채용 진행 기업 시각화

- 출발지로 지정한 지하철 역에서 부터 기업까지 걸리는 시간과 평균 연봉 등을 확인 할 수 있습니다.

![hover_company](https://media.giphy.com/media/cnKe9HtfqAZRbEbXck/giphy.gif)

* 출발 지하철 역을 변경 시 변경된 지하철 역을 기준으로 기업까지 걸리는 시간을 실시간으로 변경됩니다.

  ![change_subway](https://media.giphy.com/media/dxZYqrYQPWDBNUR4Mg/giphy.gif)

&nbsp;

#### 2) 구체적인 정보와 채공 공고 제공

- 사람인 API를 활용하여 회사 정보 및 채용에 대한 정보를 제공합니다.

  마커 또는 왼쪽 사이드바에 보여지는 근처 회사를 클릭하면 관련된 정보를 확인 할 수 있습니다.
  
  ![click_company](https://media.giphy.com/media/joeAQy9poQoVJwE2kd/giphy.gif)
  
* 소요 시간 정보와 채용 공고에 대한 구체적인 정보는 Google Map 과 사람인 링크를 통해 제공합니다.

  ![route_find](https://media.giphy.com/media/SYF1DYl01qvUWSViMV/giphy.gif)

&nbsp;

#### 3) 매일 업데이트 되는 채용 정보

- 매일 2회의 스케쥴링된 API 요청과 크롤링을 통해 채용 정보를 업데이트 합니다.

&nbsp;

## 2. Built With

![frontend stack image](assets/image/deploy_stack.png)

#### Deploy

Deploying separated Server & Client & DB

* AWS EC2
* AWS RDS
* Nginx
* uWSGI

&nbsp;

![frontend stack image](assets/image/fe_stack.png)

#### Frontend

Search engine optimized SSR / SPA with Nuxt.js

- Vue.js
- Nuxt.js
- Vuex
- Sass
- Google Maps

&nbsp;

![backend stack image](assets/image/be_stack.png)

#### Backend

 Hypermedia-driven REST API with Django REST framework 

- Django
- Django REST framework
- MySQL
- Google Maps
- Redoc(drf-yasg)

&nbsp;

## 3. Deployed Service or Local Install

#### 1) Deployed Service

[AWS](https://aws.amazon.com/) 을 이용해 배포했습니다.

- [Go to Gil-Job-E](http://recruitmap.ninja/)

#### 2) Local Installation and Run Server

1. Installation

   - Git Clone

       ```bash
        git clone https://github.com/jiwookseo/gil-job-e.git
       ```

   - or [Download ZIP](https://github.com/jiwookseo/gil-job-e/archive/develop.zip)

   &nbsp;
   
2. Settings

   *  환경 변수 설정

        아래와 같은 사람인, Google API key 와 MySQL 비밀번호를
   
         `~/.bashrc` ,  `~/.zshrc` 같은 Shell environment 에 추가해줍니다.
        
        ```
	    export SARAMIN_KEY="<your-key>"
	    export GOOGLE_MAPS_KEY="<your-key>"
	    export DJANGO_SECRET_KEY="<your-key>"
	    export MYSQL_PASSWORD="<your-password>" # SQLite3 사용 시 없어도 됩니다.
	    ```
	
	    &nbsp;
	
	* Backend 설정
	
	    backend directory 로 이동합니다.
	
	    ```bash
	    cd backend
	    ```
	
	    &nbsp;
	
	    `backend/backend/settings.py` 의 `DATABASES` 의 default host 부분을 알맞게 수정해줍니다.
	
	    MySQL 사용 시 주석 처리된 SQLite3 설정을 사용합니다.
	
	    ```python
	    DATABASES = {
	        # 'default': {
	        #     'ENGINE': 'django.db.backends.sqlite3',
	        #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	        # }
	        'default': {
	            'ENGINE': 'django.db.backends.mysql',
	            'NAME': 'nonamed',
	            'USER': 'root',
	            'PASSWORD': os.getenv('MYSQL_PASSWORD'),
	            'HOST': 'nonamed.cf94mqktvsr3.ap-northeast-2.rds.amazonaws.com',
	            'PORT': '3306',
	            'OPTIONS': {
	                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
	            }
	        }
	    }
	    ```
	
	    &nbsp;

	    `pip install` 명령어를 통해 `requirements.txt` 에 저장된 의존성 패키지를 설치합니다.
   
	    ```bash
       pip install -r requirements.txt
       ```
   
       &nbsp;
   
       migrate를 한 뒤 Django 프로젝트를 실행합니다.
   
       ```bash
       python manage.py makemigrations
       python manage.py migrate
       python manage.py runserver
       ```
   
   &nbsp;
   
   *  Frontend 설정
   
       frontend directory 로 이동합니다.
   
       ```bash
       cd frontend
       ```
   
       &nbsp;
   
       `api/company.js` ,  `api/station.js` 의 `BASE_URL`을 `localhost` 로 변경해줍니다.

	    ```js
	    const BASE_URL = 'http://recruitmap.ninja:8000/api/' // from
      const BASE_URL = 'http://localhost:8000/api/' // to
      ```

		&nbsp;
		`frontend` 디렉토리에서 `.env` 파일을 만들고, 구글맵에서 발급받은 API KEY를 입력 합니다.

		```bash
		touch .env
		GOOGLE_MAP="YOUR_GOOGLE_MAP_KEY"
		```

      &nbsp;
      
       `yarn` 명령어를 통해 의존성 패키지를 설치하고 Nuxt 서버를 실행합니다.
      
       ```bash
       yarn
       yarn dev
       ```
      

&nbsp;

## 4. Authors

* Frontend
  * [Dowoo Kim](https://github.com/dowookims)
  * [Jiwon Juliet Yoon](https://github.com/jiwonjulietyoon)

* Backend and Deploy
  * [Jiwook Seo](https://github.com/jiwookseo)