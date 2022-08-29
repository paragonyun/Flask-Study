'''
우리가 만들 DB model columns

id | subject | content | create_date
'''

from pybo import db ## __init__.py의 db를 가져옴

## db.Model을 상속 받은 Question class로 SQL 작성
class Question(db.Model) : ## class 이름으로 Table 이름이 생성됨
    id = db.Column(db.Integer, primary_key = True) ## 칼럼 속성과 기본키인지 아닌지
    ## 기본키가 되면 당연히 중복값 허용 안 한

    subject = db.Column(db.String(200), nullable=False) ## Null값 허용 안 함
    content = db.Column(db.Text(), nullable=False)
    ## String과 Text의 차이 : String은 글자수 제한 O, Text는 X
    create_date = db.Column(db.DateTime(), nullable=False)


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


### 회원 정보 (User)
class User(db.Model) :
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)