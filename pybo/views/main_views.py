from flask import Blueprint
from flask import render_template

from pybo.models import Question

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

# @bp.route('/hello') ## /hello 로 들어가면 아래의 문구가 뜸
# def hello_pybo() :
#     return 'Hello, Pybo!!'



# @bp.route('/') ##  그냥 들어가을 때 뜰 문구
# def index() :
#     return 'Pybo index'

'''
이런 식으로 Blue Print는 루트 여러개를 편하게 관리할 수 있게 만들어준다.
괜히 __init__의 create_app 함수 안에 막 넣어줄 필요가 없다 !!
'''


## 게시판 질문 목록 출력 (8.17)
@bp.route('/hello') ## /hello 로 들어가면 아래의 문구가 뜸
def hello_pybo() :
    return 'Hello, Pybo!!'


## question view와 겹치기 때문에 주석으로 처리!

# @bp.route('/') ##  그냥 들어가을 때 뜰 문구
# def index() :
#     ## 질문 목록 데이터 얻어오기
#     ## order by : 작성일시 기준의 역순으로 정렬 
#     question_list = Question.query.order_by(Question.create_date.desc())

#     ## render_template : 데이터를 템플릿으로 화면에 띄워줌
#     ## 템플릿 : 파이썬 문법을 사용할 수 있는 HTML
#     return render_template('question/question_list.html', question_list = question_list)


# ## 질문 목록에 들어갔을 때 나올 화면 정의
# @bp.route('/detail/<int:question_id>')  ## type hint와 비슷하게 int로 지정해줄 수 있음
# def detail(question_id) :
#     question = Question.query.get_or_404(question_id) ## get_or_404는 데이터가 없으면 404notfound를 출력해줌
#     return render_template('question/question_detail.html', question=question)

'''
이렇게 하면 물론 나쁘지는 않지만 기능마다 모듈을 분리시키는 게 유지보수 측면에선 훨씬 나음!!
블루프린트로 분리시켜버릴 거임~
'''

## url_for로 리다이렉팅 기능 추가
from flask import url_for, current_app
from werkzeug.utils import redirect

@bp.route('/')
def index() :                                  ## url_for : 라우팅 함수에 매핑되어 있는 url return
    current_app.logger.info('INFO 레벨로 출력') ## 직접 로그를 출력하기 위한 함수
    return redirect(url_for('question._list')) ## redirect : URL로 페이지 이동
    '''
    우리는 아까 question_view.py 에서 블루 프린트의 이름을 'question'이라고 했음
    question 불루 프린트 안의 _list 함수를 찾는 거!! 
    list 함수의 url은 @bp.route('/list/)
    그럼 url_for('question._list)가 반환하는 건 /question/list/를 반환하는 거임!!
    즉, 맨 처음 접속하면 그 주소는 localhost:5000/question/list/ 가 되는 거임
    '''


