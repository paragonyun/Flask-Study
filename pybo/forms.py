## 질문을 등록할 때의 폼 작성
from ast import Pass
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
    

## 회원 가입 폼
from wtforms import PasswordField, EmailField
from wtforms.validators import Length, EqualTo, Email

class UserCreateForm(FlaskForm) :
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[
        DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다.')
    ])
    password2 = PasswordField('비밀번호 확인', validators=[
        DataRequired()
    ])
    email = EmailField('이메일', validators=[DataRequired(), Email()])