import os


## DB 접속 주소 ##
BASE_DIR = os.path.dirname(__file__)

## SQLite DB 를 사용, pybo.db에 저장됨 ##
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))

## SQL Alchemy의 이벤트를 처리하는 옵션 ##
## 필요 없으니 False 로 비활성화 ##
SQLALCHEMY_TRACK_MODIFICATIONS = False

## CSRF 방어를 위한 secret_key
SECRET_KEY = "dev" ## 약간 비밀번호 같은 느낌 !!