from flask import Blueprint, render_template

from pybo.models import Question

from pybo.forms import QuestionForm, AnswerForm

from datetime import datetime
from flask import request, url_for
from werkzeug.utils import redirect
from .. import db

bp = Blueprint('question', __name__, url_prefix='/question')


'''
main_views.py와 똑같아 보이지만 prefix 다르게 했고, 
route도 좀 더 상세하게 바꿈 !!

=> __init__ 도 수정해야됨
'''

@bp.route('/list/')
def _list() :
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', question_list = question_list)

@bp.route('/detail/<int:question_id>/')
def detail(question_id) :
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question, form=form)

@bp.route('/create/', methods = ('GET', 'POST')) ## 질문 작성을 들어갈 때
def create() :
    form = QuestionForm()

    ## 여기부터 데이터를 db에 저장하는 코드
    ## POST로 지정했기 때문에 이제 POST인 경우[저장하기]엔 아래의 코드를 실행해서 return 하고
    if request.method == 'POST' and form.validate_on_submit() : ##validate_on_submit()은 전송된 폼 데이터의 정합성 점검
        question = Question(subject = form.subject.data, content = form.content.data, create_date = datetime.now())
        db.session.add(question)
        db.session.commit()
        
        return redirect(url_for('main.index'))

    ## Post가 아닌 get인 경우[질문 등록하기]에는 아래를 return 함
    return render_template('question/question_form.html', form=form)
