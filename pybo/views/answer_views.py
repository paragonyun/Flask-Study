from datetime import datetime

from flask import Blueprint, url_for, request
from werkzeug.utils import redirect

from pybo import db

from pybo.models import Question, Answer

from flask import render_template
from ..forms import AnswerForm

from flask import g
from .auth_views import login_required

from flask import flash

bp = Blueprint('answer', __name__, url_prefix='/answer')

@bp.route('/create/<int:question_id>', methods=('POST',))
@login_required
def create(question_id) :
    '''

    question = Question.query.get_or_404(question_id)

    ## request로 question_detail.html의 form 태그에 있는 content를 가져옴
    content = request.form['content']

    ## answer 생성 (models.py 참고)
    answer = Answer(content = content, create_date = datetime.now())

    ## 이 함수가 db.session.add()를 대신함!!
    question.answer_set.append(answer)

    ## db에 commit
    db.session.commit()
    return redirect(url_for('question.detail', question_id = question_id))
    '''
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    if form.validate_on_submit():
        content = request.form['content']
        answer = Answer(content=content, create_date=datetime.now(), user=g.user) 
        question.answer_set.append(answer)
        db.session.commit()
        return redirect(url_for('question.detail', question_id=question_id))
    return render_template('question/question_detail.html', question=question, form=form)


## 답변 수정 라우팅 함수
@bp.route('/modify/<int:answer_id>', methods=('GET', 'POST'))
@login_required
def modify(answer_id) :
    answer = Answer.query.get_or_404(answer_id)
    if g.user != answer.user :
        flash('본인 답변만 수정할 수 있습니다.')
        return redirect(url_for('question.detail', question_id=answer.question.id))
    
    if request.method == 'POST' :
        form = AnswerForm()
        if form.validate_on_submit() :
            form.populate_obj(answer)
            answer.modify_date = datetime.now() ## 수정 시각 저장
            db.session.commit()
            return redirect(url_for('question.detail', question_id = answer.question.id))
    
    else : ## 수정 버튼을 누르는 경우!!!!!!!
        form = AnswerForm(obj=answer)
    
    return render_template('answer/answer_form.html', form=form)

## 삭제를 위한 라우팅 함수
@bp.route('/delete/<int:answer_id>')
@login_required
def delete(answer_id) :
    answer = Answer.query.get_or_404(answer_id)
    question_id = answer.question.id
    if g.user != answer.user :
        flash('타인의 답변은 삭제할 수 없습니다.')
    
    else :
        db.session.delete(answer)
        db.session.commit()
    
    return redirect(url_for('question.detail', question_id=question_id))