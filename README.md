![logo image](assets/image/og_image.png)

&nbsp;

# 길잡이 / Gil-Job-E 

>  IT 관련 채용과 회사 정보를 지도에서 보여주자

- Nuxt.js를 활용하여 SSR을 지원하자.

  Nuxt.js에서 이미 built-in 된 기능이기에, nuxt.js를 build하고, build 된 디렉토리를 Nginx로 배포합니다.

- 서버가 변경되어도 클라이언트는 별 문제없이 돌아가야 한다. 

  HATEOAS를 활용한 self-descriptive한 RESTFUL API구현.

&nbsp;

##### Use our service. [http://recruitmap.ninja/](http://recruitmap.ninja/)

&nbsp;

## 1. Service Feature

#### 1) 지도에서 회사 위치 바로 확인

- Marker를 Hover 하게 되면 자신이 정한 지하철 역에서 회사까지 걸리는 시간과 평균 연봉을 확인 할 수 있습니다.

#### 2) 원 터치로 구체적인 정보 확인 가능

- 사람인 API를 활용하여 회사 정보 및 채용에 대한 정보를 제공 합니다. 마커 또는 왼쪽 메뉴바에 나오는 회사를 클릭하면 관련된 정보를 확인 할 수 있습니다.

#### 3) 매일 업데이트 되는 회사 정보

- VM을 활용하여 매일 정해진 시간에 API 요청을 보내고, 새로운 데이터가 있으면 데이터 베이스에 추가하여 새로운 회사 공고를 제공 합니다.

#### 4) 길찾기

- 자신이 지정한 역에서 회사까지 어떻게 가는지 GOOGLE MAP에 길찾기 URL을 활용하여 새 탭에서 구글맵을 통해 확인 할 수 있습니다.

#### 5) 지하철 역 기반

- 대부분 통근을 지하철로 하게 됩니다. 그렇기에 우리는 지하철 역을 변경하게 되면 변경된 지하철역을 기준으로 회사까지 걸리는 시간을 보여줍니다.

&nbsp;

## 2. Tech Stack

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

       `yarn` 명령어를 통해 의존성 패키지를 설치하고 Nuxt 서버를 실행합니다.
       
       ```bash
       yarn
       yarn dev
       ```
       


