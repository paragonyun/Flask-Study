from flask import Flask

## 1차 코드 (bp 전)
# def create_app() :
#     app = Flask(__name__)

#     @app.route('/') ## 이런 걸 '라우팅 함수'라고 한다. [url을 매핑하는 함수]
#     def hello_pybo() :
#         return 'Hello, Pybo!!'

#     return app


def create_app() :
    app = Flask(__name__)

    from .views import main_views ## 모듈을 불러옴
    app.register_blueprint(main_views.bp) ## 블루프린트 객체 bp를 등록 !!
    
    '''
    이렇게 하면 hello_pybo 함수는 필요가 없어짐
    '''

    return app