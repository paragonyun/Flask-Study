from re import M
from flask import Flask

## 1차 코드 (bp 전)
# def create_app() :
#     app = Flask(__name__)

#     @app.route('/') ## 이런 걸 '라우팅 함수'라고 한다. [url을 매핑하는 함수]
#     def hello_pybo() :
#         return 'Hello, Pybo!!'

#     return app


# def create_app() :
#     app = Flask(__name__)

#     from .views import main_views ## 모듈을 불러옴
#     app.register_blueprint(main_views.bp) ## 블루프린트 객체 bp를 등록 !!
    
#     '''
#     이렇게 하면 hello_pybo 함수는 필요가 없어짐
#     '''

#     return app


## ORM 적용 후
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy ## 얘는 Python Code로 SQL 할 수 있게 해주는 녀석임


import config
from pybo.filter import format_datetime

db = SQLAlchemy()
migrate = Migrate()

def create_app() :
    app = Flask(__name__)
    app.config.from_object(config) ## config에 작성했던 항목을 읽어옴

    ### ORM
    db.init_app(app)
    migrate.init_app(app, db) ## app에 db 등록!!
    ## 여기가 새로 추가됨 (model import)##
    from . import models 
    ## 이후 (Terminal) flask db migrate
    ## 이후 (Terminal) flask db upgrade => pybo.db 생성
    ## 이후 SQLite 깔아서 db 까지 확인
    ## 이후 (Terminal) flask shell 실행


    ## 블루 프린트 !!
    from .views import main_views , question_views, answer_views, auth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)
    ## Filter 추가
    from.filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    return app

##(Terminal)flask db init으로 migrations 폴더 생성##
## 굳이 얘네들에 대해 알 필요는 없음 ##

'''
꼭 알아야 하는 DB 관리 명령어
flask db migrate : 모델을 새로 생성 및 변경할 때 사용
flask db upgrade : 모델의 변경 내용을 실제 db에 적용할 때
'''

