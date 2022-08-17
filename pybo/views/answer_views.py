from datetime import datetime

from flask import Blueprint, url_for, request
from werkzeug.utils import redirect

from pybo import db

from pybo.models import Question, Answer

bp = Blueprint('answer', __name__, url_prefix='/answer')

@bp.route('/create/<int:question_id>', methods=('POST',))
def create(question_id) :
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


