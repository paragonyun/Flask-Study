from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from pybo import db
from pybo.forms import UserCreateForm, UserLoginForm
from pybo.models import User


import functools

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/signup/', methods=('GET', 'POST'))
def signup() :
    form = UserCreateForm()

    ## post 방식이면 계정 저장
    if request.method== 'POST' and form.validate_on_submit() :
        user = User.query.filter_by(username=form.username.data).first()
        if not user :
            user = User(username=form.username.data,
                        password = generate_password_hash(form.password1.data),
                        email = form.email.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.index'))
        else :
            ## flash : 프로그램 논리 오류를 발생시키는 함수
            flash('이미 존재하는 사용자입니다.')
    
    ## get 방식이면 계정 등록 화면 출력
    return render_template('auth/signup.html', form=form)

## 로그인
@bp.route('/login/', methods=('GET', 'POST'))
def login() :
    form = UserLoginForm()
    if request.method== 'POST' and form.validate_on_submit() :
        error = None
        user = User.query.filter_by(username=form.username.data).first()
        if not user :
            error = '존재하지 않는 사용자입니다.'
        elif not check_password_hash(user.password, form.password.data) :
            error = '잘못 입력하신 거 같은데유~ 다시 확인해봐유!'
        
        ## 정상 로그인 되면 메인으로
        if error is None :
            session.clear()
            ## flask session에 사용자 정보 저장
            ## session은 한번 생성되면 그 값을 계속 유지함 <-> request : 객체를 요청할 때마다 새로운 객체 생성
            session['user_id'] = user.id

            _next = request.args.get('next', '')
            if _next :
                return redirect(_next)
            else :
                return redirect(url_for('main.index'))

            return redirect(url_for('main.index'))
        flash(error) ## 이거 아니면 전송 받았는데 에러가 났다는 의미이므로..!

    return render_template('auth/login.html', form=form)

## 로그인 여부 확인
@bp.before_app_request
def load_logged_in_user() :
    user_id = session.get('user_id')
    if user_id is None :
        g.user = None
    else :
        g.user = User.query.get(user_id)

## 로그아웃
@bp.route('/logout/')
def logout() :
    session.clear()
    return redirect(url_for('main.index'))

def login_required(view) :
    @functools.wraps(view)
    def wrapped_view(*args, **kwargs) :
        if g.user is None : ##로그인이 안 되어 있는 상태
            _next = request.url if request.method == 'GET' else ''
            return redirect(url_for('auth.login', next=_next))
        return view(*args, **kwargs)
    return wrapped_view