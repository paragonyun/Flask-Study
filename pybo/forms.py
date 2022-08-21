## 질문을 등록할 때의 폼 작성
from typing import Text
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

## 폼 클래스는 FlaskForm 을 상속 받아야함
## 여기엔 제목과 내용에 형식 제한을 걸 거임
class QuestionForm(FlaskForm) :
    '''
    StringField('Label', validators=[])
    validators 의 종류
    - DataRequired : 필수 항복인지 체크
    - Email : 이메일인지 체크
    - Length : 길이 체크
    '''
    subject = StringField('제목', validators=[DataRequired('제목 입력 하셔야쥬!!')]) ## 이렇게 하면 오류 내용을 한글로 띄울 수 있음
    content = TextAreaField('내용', validators=[DataRequired('내용은 왜 안 적으셨댜~~??')])


class AnswerForm(FlaskForm) :
    content = TextAreaField('내용', validators=[DataRequired('답변 하기 싫어유?')])
    