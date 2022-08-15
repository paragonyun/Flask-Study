from flask import Blueprint

'''
__name__ : 이 모듈의 이름인 main_views
'main' : 이 블루프린트의 별칭(이름) 나중에 url_for에서 활용됨
url_prefix : 라우팅 함수 애너테이션 url 맨 앞에 붙을 접두어 url
'''
bp = Blueprint('main', __name__, url_prefix='/')

## 라우팅 함수 추가 전
# @bp.route('/') ## 이게 app.route 에서 bp.route로 바뀜!!
# def hello_pybo() :
#     return 'Hello, Pybo!!'

@bp.route('/hello') ## /hello 로 들어가면 아래의 문구가 뜸
def hello_pybo() :
    return 'Hello, Pybo!!'


@bp.route('/') ##  그냥 들어가을 때 뜰 문구
def index() :
    return 'Pybo index'

'''
이런 식으로 Blue Print는 루트 여러개를 편하게 관리할 수 있게 만들어준다.
괜히 __init__의 create_app 함수 안에 막 넣어줄 필요가 없다 !!
'''