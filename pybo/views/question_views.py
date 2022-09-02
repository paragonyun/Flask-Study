from flask import Blueprint, render_template

from pybo.models import Question

from pybo.forms import QuestionForm, AnswerForm

from datetime import datetime
from flask import request, url_for
from werkzeug.utils import redirect
from .. import db

from flask import g
from pybo.views.auth_views import login_required

from flask import flash

bp = Blueprint('question', __name__, url_prefix='/question')


'''
main_views.py와 똑같아 보이지만 prefix 다르게 했고, 
route도 좀 더 상세하게 바꿈 !!

=> __init__ 도 수정해야됨
'''

@bp.route('/list/')
def _list() :
    page = request.args.get('page', type=int, default=1)  # 페이지
    question_list = Question.query.order_by(Question.create_date.desc())
    question_list = question_list.paginate(page, per_page=10)
    return render_template('question/question_list.html', question_list = question_list)

@bp.route('/detail/<int:question_id>/')
def detail(question_id) :
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question, form=form)

@bp.route('/create/', methods = ('GET', 'POST')) ## 질문 작성을 들어갈 때
@login_required ## 로그인이 필요한 서비스라는 제약을 걸어줌
def create() :
    form = QuestionForm()

    ## 여기부터 데이터를 db에 저장하는 코드
    ## POST로 지정했기 때문에 이제 POST인 경우[저장하기]엔 아래의 코드를 실행해서 return 하고
    if request.method == 'POST' and form.validate_on_submit() : ##validate_on_submit()은 전송된 폼 데이터의 정합성 점검
        question = Question(subject = form.subject.data, content = form.content.data, create_date = datetime.now(), user=g.user)
        db.session.add(question)
        db.session.commit()
        
        return redirect(url_for('main.index'))

    ## Post가 아닌 get인 경우[질문 등록하기]에는 아래를 return 함
    return render_template('question/question_form.html', form=form)

## 질문 수정을 위한 라우팅 함수
@bp.route('/modify/<int:question_id>', methods=('GET','POST'))
@login_required
def modify(question_id) :
    question = Question.query.get_or_404(question_id)
    if g.user != question.user :
        flash('너가 쓴 글 아니잖아여!!!!')
        return redirect(url_for('question.detail', question_id=question_id))
    
    if request.method == 'POST' : ## 수정하고 저장하기 버튼을 눌렀을 경우임!
        form = QuestionForm() 
        if form.validate_on_submit() :
            form.populate_obj(question)
            question.modify_date = datetime.now() ## 수정일시 저장
            db.session.commit()
            return redirect(url_for('question.detail', question_id = question_id))

    else : ## get 요청인 경우 = 질문 수정 버튼을 눌렀을 경우
        form = QuestionForm(obj=question) ## question의 내용이 담겨져서 나옴!!
    return render_template('question/question_form.html', form=form)


## 질문 삭제를 위한 라우팅 함수
@bp.route('/delete/<int:question_id>')
@login_required
def delete(question_id) :
    question = Question.query.get_or_404(question_id)
    if g.user != question.user :
        flash('다른 사람 글은 삭제 못해용~')
        return redirect(url_for('question.detail', question_id=question_id))
    db.session.delete(question) ## db에서 question에 해당되는 내용 삭제
    db.session.commit()
    return redirect(url_for('question._list'))


## 질문 추천을 위한 라우팅 함수
@bp.route('/vote/<int:question_id>/')
@login_required
def vote(question_id) :
    _question = Question.query.get_or_404(question_id)
    if g.user == _question.user :
        flash('본인 질문엔 추천할 수 없습니다.')
    
    else :
        _question.voter.append(g.user)
        db.session.commit()
    
    return redirect(url_for('question.detail', question_id = question_id))

