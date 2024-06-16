from taskmanager import app, db
from flask import flash, render_template, request, url_for, redirect
from sqlalchemy import text

@app.route('/')
def home_page():
    cookie = request.cookies.get('name')
    print("<>home_page()")

    # table = "users"
    # query_stmt = text("SELECT * FROM " + table) 
    # result = db.session.execute(query_stmt)
    # [print(row) for row in result]

    return render_template('home.html', cookie=cookie)



@app.route('/login', methods=['GET', 'POST'])
def login_pages():
    print("login was called")

    if request.method == 'POST':
        print("->login_pages()")
        username = request.form.get('Username')
        password = request.form.get('Password')
        print("Here the Data!!!")
        print(username)
        print(password)

        if (username is None or
                isinstance(username, str) is False or
                len(username) < 3):
            print("not valid")
            flash(f"Username is not valid", category='warning')
            return render_template('login.html', cookie=None)

        if (password is None or
                isinstance(password, str) is False or
                len(password) < 3):
            print("something with password")
            flash(f"Password is not valid", category='warning')
            return render_template('login.html', cookie=None)
        
        # [Skip password](username) ==> <name>' # 
        # [Skip password & Output passwords](username | password) ==>  ' OR '1'='1' UNION SELECT password FROM users #
        query_stmt = f"select name from users where name = '{username}' and password = '{password}'"
        print(query_stmt)
        result = db.session.execute(text(query_stmt))

        user = result.fetchall()
        if not user:
            flash(f"Try again", category='warning')
            return render_template('login.html', cookie=None)
        flash(f"'{user}', you are logged in ", category='success')

        resp = redirect(url_for('tasks_pages'))
        resp.set_cookie('name', username)
        print("<-login(), go to tasks_page")
        return resp

    return render_template('login.html', cookie=None)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    if request.method == 'POST':
        print("->register_page()")

        username = request.form.get('Username')
        password1 = request.form.get('Password1')
        password2 = request.form.get('Password2')

        print(username)
        print(password1)
        print(password2)

        if(username is None or
                isinstance(username, str) is False or
                len(username) < 3):
            #flash("Username not valid", category='danger')
            print("<-register_page(), username invalid")
            return render_template('register.html', cookie=None)

        # if(email is None or
        #         isinstance(email, str) is False or
        #         len(email) < 3):
        #     print("<-register_page(), email not valid")
        #     #flash("Email not valid", category='danger')
        #     return render_template('register.html', cookie=None)

        if(password1 is None or
                isinstance(password1, str) is False or
                len(password1) < 3 or
                password1 != password2):
            print("<-register_page(), password1 not valid")
            #flash("Password1 not valid", category='danger')
            return render_template('register.html', cookie=None)

        query_stmt = f"select name from users where name = '{username}'"
        print(query_stmt)
        result = db.session.execute(text(query_stmt))
        item = result.fetchone()
        print(item)

        if item is not None:
            flash("Username exists, try again", category="Warning")
            print("Username exists")
            return render_template('register.html', cookie=None)

        query_insert = f"insert into users (name, password) values ('{username}', '{password1}')"
        print(query_insert)
        db.session.execute(text(query_insert))
        db.session.commit()
        flash("You are registered", category='success')
        resp = redirect(url_for('tasks_pages'))
        resp.set_cookie('name', username)
        print("<-register_page(), go to tasks_pages")
        return resp

    return render_template('register.html')

@app.route('/tasks')
def tasks_pages():

    cookie = request.cookies.get('name')
    print("->tasks_page()", cookie)
    if not request.cookies.get('name'):
        print("<-tasks_page(), no cookie")
        return redirect(url_for('login_pages'))

    query_stmt = f"select * from tasks"
    result = db.session.execute(text(query_stmt))
    itemsquery = result.fetchall()

    print("<-tasks_pages()=", cookie)
    return render_template('tasks.html', items=itemsquery, cookie=cookie)


@app.route('/logout')
def logout():
    resp = redirect('/')
    resp.set_cookie('name', '', expires=0)
    return resp


@app.route('/task_entry', methods=['GET', 'POST'])
def task_entry():

    cookie = request.cookies.get('name')
    print("->task_entry()", cookie)
    if not cookie:
        print("no cookie")
        return redirect(url_for('login_pages'))

    if request.method == 'POST':
        title = request.form.get('title')
        user = request.form.get('userID')
        description = request.form.get('description')

        query_insert = f"insert into tasks ( user, title, description) values ('{user}', '{title}', '{description}')"
        print(query_insert)
        db.session.execute(text(query_insert))
        db.session.commit()
        resp = redirect('/tasks')
        resp.set_cookie('name', cookie)
        return resp

    return render_template('task_entry.html', cookie=cookie)

