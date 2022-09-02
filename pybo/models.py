'''
우리가 만들 DB model columns

id | subject | content | create_date
'''

from pybo import db ## __init__.py의 db를 가져옴

## 추천수를 위한 객체 생성
question_voter = db.Table(
    'question_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('question_id', db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'), primary_key=True)    
)


answer_voter = db.Table(
    'answer_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('answer_id', db.Integer, db.ForeignKey('answer.id', ondelete='CASCADE'), primary_key=True)
)

## db.Model을 상속 받은 Question class로 SQL 작성
class Question(db.Model) : ## class 이름으로 Table 이름이 생성됨
    id = db.Column(db.Integer, primary_key = True) ## 칼럼 속성과 기본키인지 아닌지
    ## 기본키가 되면 당연히 중복값 허용 안 한

    subject = db.Column(db.String(200), nullable=False) ## Null값 허용 안 함
    content = db.Column(db.Text(), nullable=False)
    ## String과 Text의 차이 : String은 글자수 제한 O, Text는 X
    create_date = db.Column(db.DateTime(), nullable=False)

    ## User 모델을 Questin 모델과 연결하기 위한 속성
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    
    ## Question에서 User를 참조하기 위한 속성
    user = db.relationship('User', backref=db.backref('question_set'))

    ## 수정 일시 기록
    modify_date = db.Column(db.DateTime(), nullable=True)

    ## 추천수 기능
    # 추천인
    '''
    User 모델을 첫번째로 연결되어 있고 secondary=question_voter Table로 되어있으므로 
    Question 모델로 추천인을 저장하면 실제 ㄷ이터는 quesion_voter Table에 저장
    추천인 정보는 voter column에 저장됨
    '''
    voter = db.relationship('User', secondary=question_voter, backref=db.backref('qestion_voter_set'))

## 답변 class도 생성
class Answer (db.Model) :
    id = db.Column(db.Integer, primary_key = True)
    '''
    답변과 질문을 연결하기 위한 속성 
    연결 기준이 되는 key는 당연히 외래키가 됨 
    ForeignKey('qwestion.id')는 qestion Table의 id Column을 가져오겠다는 말, 객체 아님!!!!
    CASCADE : 질문이 삭제되면 답변도 함께 삭제된다는 말
    '''
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    
    '''
    relationship('참조할 모델명', backref)
    역참조(backref) : 질문에 달린 답변들을 볼 수 있게 하는 것 (한 질문엔 답변이 여러개 달릴 수 있다.)
    '''
    question = db.relationship('Question', backref=db.backref('answer_set'))

    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

    ## 글쓴이 추가
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('answer_set'))

    ## 수정 일시 기록
    modify_date = db.Column(db.DateTime(), nullable=True)

    ## 추천인 정보
    voter = db.relationship('User', secondary=answer_voter, backref=db.backref('answer_voter_set'))
    
### 회원 정보 (User)
class User(db.Model) :
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)