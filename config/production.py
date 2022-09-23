## 서버 환경 담당
from config.default import *

SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'pybo.db')}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xf4\xe7\xd7\x00\xe6\xfc:n\x0c\x171\x164\xc2\x040'

from logging.config import dictConfig ## 파이선의 기본 logging 모듈

dictConfig({
    'version' : 1,

    ## 로그를 출력할 형식 정해줌
    'formatters' : {
        'default' : {   ## 현재 시간    ## 로그의 레벨  ## 모듈명   # 출력 내용
            'format' : '[%(asctime)s] %(levelname)s n %(module)s: %(message)s',
        }
    },

    ## 로그를 출력할 방법
    'handlers' : {
        'file' : {
            'level' : 'INFO',
            'class' : 'logging.handlers.RotatingFileHandler', # 파일 용량이 커지만 파일을 하나 더 만들어줌
            'filename' : os.path.join(BASE_DIR, 'logs/myproject.log'),
            'maxBytes' : 1024*1024*5, # 그 파일 용량 설정을 5MB 로 함 
            'backupCount' : 5, 
            'formatter' : 'default',
        },
    },
    'root' : {
        'level' : 'INFO',
        'handler' : ['file']
    }
})

