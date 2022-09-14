# AWS Sail을 이용한 pybo 배포하기
지금까지 데이터베이스에서 어떤 정보를 어떻게 화면에 띄울지와 그 화면을 어떻게 꾸밀지 다 정했다. 이제 이렇게 구현한 기능을 세상에 선보일 차례!

![image](https://user-images.githubusercontent.com/83996346/189043591-363284e3-7955-4b2f-8977-8d65c54f150b.png)

<br>

# 서버 접속을 위하여

## 고정 IP 
네트워킹 - `고정 IP 생성`

## 방화벽 설정
우리가 만들었던 파이보의 포트 번호는 5000 이었다. 외부에서 이 5000포트에 접속하려면 방화벽 해제를 위해   
네트워킹 - `규칙 추가` - `포트 번호에 5000 입력` - `생성` 을 해줘야 한다.   

## **SSH**
네트워킹 상의 **다른 컴퓨터에 로그인하거나 원격 시스템(서버)의 명령을 수행**하기 위한 프로토콜 (기본 포트 : 22)

<br>

기본적으로 AWS 프라이빗 키가 필요함

키를 다운 받고, root directory(`C:/`)에 넣고 이름을 우리 프로젝트 Folder와 동일하게 바꿔줌(지금 예시론 `myproject.pem`)

<br>

## SSH 클라이언트
서버에 접속하는 단말기 역할(== 터미널)
  
우리는 `MobaXterm` 라고 하는 SSH 터미널 프로그램을 이용할 것임

> 1. SSH 누르기
> 2. `Remote Host`에 서버의 고정 IP 입력
> 3. `Specify Username`에 `ubuntu` 입력
> 4. `Use Private Key` 체크, local에 있는 pem파일 (아까 myproject.pem)선택
> 5. OK

![image](https://user-images.githubusercontent.com/83996346/189042764-126971a1-6058-4077-991e-98f362b93402.png)

그럼 이렇게 MobaXterm으로 서버 작업을 진행할 수 있게 된다.

~~Mac은 기본적으로 ssh 터미널을 지원해준다.. 맥북을 사야하는 또 하나의 이유일지도?~~

<br>

# 서버에서 해야할 일
## Hostname 변경
`sudo hostnamectl set-hostname {name}`

`sudo reboot`

세션 종료하고 다시 들어오면 이름이 잘 바뀌어 있다.

이름 확인 : `hostname`  

<br>

## 서버 시간 설정
기본 설정은 `UTC` 시간으로 되어 있다. 아래의 명령어 실행
`sudo ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime`

시간 확인 : `date`

<br>

## 파이썬 설치 확인
설치 확인 : `python`

`python3`를 입력하면 파이썬 shell이 실행됨. 나갈 땐 `exit()`

<br>

## 가상 환경 설정
**우분투 패키지 최신 버전으로 업데이트**  
`sudo apt update`

**파이썬 가상환경 패키지 설치**  
`sudo apt intall python3-venv`

**필요한 하위 폴더 생성**  
`mkdir projects`  
`mkdir venvs`

**가상 환경 생성 (in venvs)**  
`python3 -m venv myproject`

**가상 환경 진입**  
`cd myproject`  
`cd bin`  
`. activate` (꼭 '.'과 activate를 띄워줘야한다!)

가상환경 나오기 : `deactivate`

# 프로젝트 관련 패키지 설치
## wheel 패키지 설치
그냥 pip 쓰면 에러 뜸 이걸 미리 깔아야 한다!  
`pip install wheel`

## Flask 및 필요한 패키지 설치
나중에 가면 이 부분은 그냥 `requirements.txt` 로 할 거 같다. 지금은 그냥 복습 차원에서 뭘 깔았었나 다시 봐보자.

`pip install flask`  
`pip install flask-migrate`  
`pip install flask-wtf`  
`pip install email_validator`  
`pip install flask-markdown`  

<br>

# 깃을 통하여 pybo 설치!!! 
**이래서 깃을 쓰는구나 싶다!!**  
진짜 버전관리와 저장에 있어 너무 유용하다..!  

`git clone {레파지토리} myproject`   

## pybo 실행
**변수 설정**  
`export FLASK_APP=pybo`  
`export FLASK_DEBUG=true`

**데이터 베이스 초기화**  
이 과정은 _프로젝트의 홈 디렉토리에서 해야됨_(여기선 myproejct)
`flask db init`  
`flask db migrate`  
`flask db upgrade`

**FLASK SERVER 실행**  
이 작업을 하기 전에는 ubuntu에 있는 db들을 지우고 

`flask db init`  
`flask db migrate`  
`flask db upgrade`  

를 해주는 게 좋음!! 그래야 깔끔하게 이용하지 ㅎㅎ


`flask run --host=0.0.0.0`  
0.0.0.0은 모든 외부 IP에서 이 서버로의 접속을 허용한다는 말(아이피 개방)

<br>

# 결과물

![image](https://user-images.githubusercontent.com/83996346/189058913-47a10d08-c83a-47a2-afb7-fd1a3a09da36.png)
![image](https://user-images.githubusercontent.com/83996346/189059180-55ea2e85-3bb2-46d6-a5d4-26c42d65513a.png)
![image](https://user-images.githubusercontent.com/83996346/189059079-8e6c4499-be9f-4c45-af84-2d33391bc5b6.png)

<br>

## 다시 실행 시킬 때.
```ubuntu
cd venvs
cd myptoject
cd bin
. activate
cd ~/projects
export FLASK_APP=pybo
export FLASK_DEBUG=true
cd myproject
flask run --host=0.0.0.0

my static ip (AWS) : 43.200.124.184
or click this url : http://43.200.124.184:5000/question/list/
```

**이게 귀찮으면? nano 편집기를 이용하자!**
> 1. `cd /home/ubuntu/venvs/`로 경로 이동
> 2. `nano myproject.sh`
> ![image](https://user-images.githubusercontent.com/83996346/190072776-d737d611-a7b3-483b-a2d1-5df6c5d27129.png)
이런 화면을 확인할 수 있다.
> 3. 아래의 코드 입력
```
#!bin/bash
cd ~/projects/myproject
export FLASK_APP=pybo
export FLASK_DEBUG=true
export APP_CONFIG_FILE=/home/ubuntu/projects/myproject/config/production.py
. ~/venvs/myproject/bin/activate
```
> 4. _Ctrl_ + o 그러고 enter -> _ctrl_ + x로 저장 후 나옴
> 5. `. myproject.sh`로 명령어 실행!!

<br>

# WSGI Server 구니콘 사용하기
- 우리가 지금까지 flask run 으로 한 건 플라스크 내장 서버! 그러나 이건 운영 및 배포용으로는 적절하지 않음!!  
`pip install gunicorn`  
설치되면 아래의 명령어 실행  
```
cd ~/projects/myproject/ (이미 여기면 뭐 안 써도 됨!)
gunicorn --bind 0:5000 "pybo:create_app()" 
```
5000번 포트로 WSGI 서버를 수행 -> pybo의 application factory인 create_app()을 호출!! (이게 WSGI Application 역할)  
그럼 flask run을 안 하더라도 gunicorn 이 서버를 띄워줌!! 와우!

## Gunicorn 소캣
Unix 계열은 소켓으로 서버를 띄우는 게 더 효율적!   
(Unix : OS의 가장 근간이 되는 디자인! ubuntu도 유닉스 계열이라 그럼)   
-> 이렇게 소켓으로 작동 시키면 단독으로는 실행 못 시킴..!   
    -> Nginx와 같은 웹 서버에서 WSGI 서버에 접속하도록 설정해줘야됨  
포트로 여는 거랑 비슷한데 살짝 다르다.   
`gunicorn --bind unix:/tmp/myproject.sock "pybo:create_app()"`

## AWS가 Gunicorn 자동 실행시키게 하기
**1. 환경 변수 파일 작성**  
    `/home/ubuntu/venvs/`로 이동!!!!  
    `nano myproject.env`로 편집기 들어가기.  
    아래의 코드 입력  

    FLASK_APP=pybo
    FLASK_DEBUG=true
    APP_CONFIG_FILE=/home/ubuntu/projects/myproject/config/production.py
    
**2. 서비스 파일 작성**  
    `/etc/systemd/system/`으로 이동  
    `sudo nano myproject.service` 로 편집기 실행(관리자 권한으로!)
    아래의 코드 입력

    [Unit]
    Description=gunicorn daemon
    After=network.target

    [Service]
    User=ubuntu
    Group=ubuntu
    WorkingDirectory=/home/ubuntu/projects/myproject
    EnvironmentFile=/home/ubuntu/venvs/myproject.env
    ExecStart=/home/ubuntu/venvs/myproject/bin/gunicorn \
            --workers 2 \
            --bind unix:/tmp/myproject.sock \
            "pybo:create_app()"
    [Install]
    WantedBy=multi-user.target

**3. 서비스 실행 및 등록**  
    `sudo systemctl start myproject.service`으로 실행  
    `sudo systemctl status myproject.service`로 정상작동 여부 확인  
> 경로 설정이 매우 중요합니다..!!  
  
**4. AWS 실행시 자동으로 Gunicorn 실행**  
    `sudo systemctl enable myproject.service`

**그 외**  
    서비스 종료  
    `sudo systemctl stop myproject.service`  
    서비스 재시작
    `sudo systemctl restart myproject.service`
