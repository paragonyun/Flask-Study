from flask import Blueprint, render_template

from pybo.models import Question

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
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question)

