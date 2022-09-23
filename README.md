# Index
[Book and Envrionment](#flask-study-and-envrionment-earthasia)  

[What I Learned - Pythona and Terminal](#what-i-learned-from-this-book-python-and-terminal-basic-facepunch)  

**[What I Leanred - FLASK](#what-i-learned-from-this-book-flask-bluebook)**

[What I Learned - misscelloaneous](#what-i-learned-from-this-boos-miscellaneous-exclamation)  

[Maybe Later...](#what-i-want-to-know-greyquestion)

# Flask Study and Envrionment :earth_asia:
I refer to [Jump to Flask](https://wikidocs.net/book/4542)   
Window  
VS Code  
Git Bash  
Python (So Obviously)

# What I learned from this book (Python and Terminal Basic) :facepunch:
**1. @decorator function of python**  
- It is used for add more actions of function without revising  
- It is little bit complicated but very useful!  

**2. Terminal Issues**  
- Windows Terminal somtimes raise error because Using '' Not "  "  :confused:    
- Somtimes.. we don't need "SPACE BAR"    
- We can easily run codes with cmd file! (You should not use space bar...!)
  
**3. Making Envrionments**  
- It is VERY USEFUL for developers when each project require different version of libraries  
- We can be less worried about version conflict or conflict between project !!  
- and I think it is more easier to connect with Git..!  

# What I learned from this book (Flask) :blue_book:  
- We have to run flask  _at project directory_
- Role of _create_app()_
- Role and Usage of _Blue Print_
- DB Connecting with model, ORM, SQLite
- DB Modification, Update and Inquire with Python Codes (But I think I will prefer SQL..)
- Setting DB's Type and Key Setting and Relationship Between Tables  

<br>

## **8.17**
- Template Tags that are ofren used in Flask (if, for, object) 
- 200 : Success   
  500 : Internal Server Error(it means my code's somewhere is wrong...)   
  404 : Not Found (it means I should make codes about other cases..!)  
- Role and Usage of _redirect_
- Role and Usage of _url_for()_ (Very Useful)
- Role of _request_ (I wonder if is almost same with request function of Crawling)  

<br>

## **8.19**
- Adjust Design with _CSS_ 
- Design Web Page more easier with _Bootstrap_ !! 

<br>

## **8.20**
- It is so AMAZNG to desing with _"card component" of Boostrap_
  - I think I should organize list of bootstrap's classes..! So useful!
- How to change of template file to standard HTML structure.

<br>

## **8.21**
- Data Validation with _Form Mudule_
- _SERET KEY_ for Detection from _CSRF Attack_
- Making _Answer Form_ and _Question Form_
- Review the function of _render template()_
- Review how to add datas to DB
- The importance of _"method" parameters_ (in form tag)
- How to _indicate Error Messages_
  - Role of _DataRequired_
  - How to change a Error Message to what I want to show

<br>

## **8.22**
- Navigation Bar
  - For going main page
  - The code should be in _'base.html'_
- Bootstrap NavBar provide _Menu Button_

<br>

## **8.27**
- Paging
  - _request.args.get()_ function can get value of page from URL
  - _paginate()_ function is the **MAIN KEY** of paging  

<br>
 
## **8.28**
- Template Filter
  - Change Format of datetime
- Add # of Posts !
- Add # of Comments!

<br>

## **8.29**
- Making _sign up_
- Add Codes about _db of users_
- Validator is VERY IMORTANT in this stage..!

<br>

## **8.30**
- The Role of _flash()_
- Encryption password by _generate\_password\_hash()_
- Navbar is returnd... with _js_
- Adding Navbar with _include_
  - _include_ can insert HTML in specific location of template
- The difference of _Session_ from request
  - It is a kind of MEMORY OF SERVER
  - So it maintain the received informations
- Making _Login_
- Making _Logout_
- _@bp.before\_app\_request_ Annotation is always implemented before all of routing Functions!!

<br>

## **9.1**
- _Revise models.py_ and _Revise \__init\__.py_ to add 'user' attribute
- When I want to add attribute that _nullable=False_, I shoud do sequential stages below...!
```
1. user_id의 nullable 설정을 False 대신 True로 바꾸기
2. user_id를 임의의 값으로 설정하기(여기서는 1로 설정)
3. flask db migrate 명령, flask db upgrade 명령 다시 실행하기
4. user_id의 nullable 설정을 다시 False로 변경하기
5. flask db migrate 명령, flask db upgrade 명령 다시 실행하기
```
- _g.user_ is user information data that saved in session.
  - It is generated by _@bp.before\_app\_request_ Annotation!!! of _auto\_views.py_

- **_@login\_required_** Decorator makes codes more efficiently!!
- How to _deactivate_ text area of HTML

- If I want to show nothing when I click a Button, use **_javascript:void(0)_** 
  - ex) Delete Button 

<br>

## **9.2**
- Add _Recommend Voting_(not RecSys.. ㅋㅋ)
  - It is N:N relatioonship! So We need to make _Table_ that has _many **PRIMARY KEY**_
  - _Can not have same backref name_ between relationship attribute by same model

- Add **_Anchor_** for moving scroll to what I post!!
- Can write the posts with **_MARK DOWN_** with flask-markdown 

<br>

## **9.5**
- Add **_Search_** !!
  - It has to be "GET" for indexing
  - and "POST" avoids duplicate requests 
    - It arise _expired page_

- How to use *_JOIN_* in FLASK
  - _.query.join(Table).filter(condition)_ to use inner join!
  - _.query.count()_ function for counting
  - _.query.outerjoin()_ to use outerjoin!
    - If you don't want to see duplicated values, use _distinct()_
  
- How to use *_Subquery_*
  - For joining complicated relationships
```python
sub_query = db.session.query(Answer.question_id, Answer.content, User.username)\
            .join(User, Answer.user_id == User.id).subquery()

Question.query.outerjoin(sub_query, sub_query.c.question_id == Question.id).distinct()
```

## **9.14**
- Using **config file** for more safe environment!!
- To generate **Complex Secret KEY**, use codes below in Terminal!!
```Terminal
python -c "import os; print(os.urandom(16))"
```
you will get a random key!

- If you use config folder to manage params..! you have to set config file directory in Terminal!!
`set APP_CONFIG_FILE=C:\venvs\myproject\config\development.py`
  
## **9.15**
- Add **Error Page**



<br>

# What I leaned from this book (Web and Server!) :computer:
## **9.14** (long time... no... see...)
- Web Browser request a **"Static Page"** to server!
  - It means `.js`, `.png`, `.css` , `.html`.. etc..
- Web Browser also request a **"Dynamic Page"**
  - It means changes continuously! like question list that is connected with DB!!
- When Browser request Dynamic Page, we need **Web Server and "WSGI(위스키)[=WSGI미들웨어, WSGI컨테이너]" Server!!**
  - _**Web Server calls WSGI Server and WSGI Server calls python programs!!**_
  - Web Server -> WSGI Server -> Python Programs!

- WSGI Server calls WSGI Application(like django.. FLASK!)
![image](https://user-images.githubusercontent.com/83996346/190076460-90ad227f-b5aa-4ae6-9aa1-09ec1e34d145.png)

## **9.15**  
- The Basic Port of HTTP Protocol is **80** !! 

## **9.23**
- How to log the logs to a log file
  - Using **_dictConfig_** to set the log formats

- Reason why we have to use **_SSL(HTTPS)_** !!


<br>

# What I learned from this book (Miscellaneous) :exclamation:
**1. HTML**
- If there are template code in Comment(주석) like {%%}, TemplateSyntaxError is raised.

<br>

## **8.20**
- There are _Standard of HTML_
  - HTML structure should have _html, head, body element_ and css file link should be in _head element_ 
  - Flask provide to us for changing of template to HTML Standard !!

<br>

## **9.1**
- If you want to Use **_JS_** in HTML, it is better to insert just over the \<Body> tag

<br>

## **9.2**
- Badge in Btn is so Cute...
- Anchor Element can go tag to url


**n. Hibbit**
- READ THE ERROR MESSAGES CAREFULLY... PLZ!!!!!!!! it already teachs to you the answer sometimes..! 
- If the function is different, it is better to seperate them by module. It will be easier to maintain projects!! 
- **_git_** is GOAT

# What I want to KNOW :grey_question:
- I don't know why I get messages like _""GET /static/bootstrap.min.css HTTP/1.1" 304 -"_ or _""GET /static/style.css HTTP/1.1" 304 -"_
- (8.22) I can not see "계정생성" and "로그인" in my page... I think made some typo.. 
  - (8.30) I finally find why I could not SEE that buttons... It was because the size of Window!!!!!!!! ... :(
