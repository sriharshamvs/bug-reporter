from flask import Flask, render_template, request, redirect, session, url_for, abort, session
from models import db, EmployeeModel, BugModel, ProgramModel
from constants import ReportSelectData_Program, ReportSelectData_Report_Type, ReportSelectData_Report_Severity, ReportSelectData_ReportedBy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yellow-pages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "SnrWYeG9faB&HeE2hnx9&Cva"
db.init_app(app)

@app.before_first_request
def before_request():
    db.create_all()

@app.route('/')
def index():
    status = None
    level = None
    try:
        status = session['login_id']
        level = session['level']
        user = session['user']
    except:
        status = None
        level = None  
        user = None  
    if not status:
        return redirect('/login')
    else:
        bug_model = BugModel.query.all()
        return render_template('index.html', bug_model=bug_model, status=status, level=level, user=user)

@app.route('/users')
def users():
    status = None
    level = None
    try:
        status = session['login_id']
        level = session['level']
        user = session['user']
    except:
        status = None
        level = None  
        user = None  
    if not status:
        return redirect('/login')
    else:
        users = EmployeeModel.query.all()
        return render_template('users.html', users=users, status=status, level=level, user=user)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')

    if request.method == 'POST':
        user = request.form['user']
        login_id = request.form['login_id']
        user_password = request.form['user_password']
        level = request.form['level']

        if  not user or not login_id or not user_password or not level:
            return render_template('error.html')
        else:    
            employee = EmployeeModel(user=user, login_id=login_id, user_password=user_password, level=level)
            db.session.add(employee)
            db.session.commit()

            return redirect('/')

@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    if request.method == 'GET':
        return render_template('create_user.html')

    if request.method == 'POST':
        user = request.form['user']
        login_id = request.form['login_id']
        user_password = request.form['user_password']
        level = request.form['level']

        if  not user or not login_id or not user_password or not level:
            return render_template('error.html')
        else:    
            employee = EmployeeModel(user=user, login_id=login_id, user_password=user_password, level=level)
            db.session.add(employee)
            db.session.commit()

            return redirect('/')


@app.route('/user/<int:id>/update', methods=['GET', 'POST'])
def update_user(id):
    employee = EmployeeModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if employee:
            db.session.delete(employee)
            db.session.commit()
            
            user = request.form['user']
            login_id = request.form['login_id']
            user_password = request.form['user_password']
            level = request.form['level']
            
            employee = EmployeeModel(user=user, login_id=login_id, user_password=user_password, level=level)
            
            db.session.add(employee)
            db.session.commit()
            return redirect('/')
        return f"Employee with id = {id} Does not exist"
 
    return render_template('update_user.html', employee=employee)


@app.route('/user/<int:id>/delete', methods=['GET'])
def delete_user(id):
    employee = EmployeeModel.query.filter_by(id=id).first()
    if request.method == 'GET':
        if employee:
            db.session.delete(employee)
            db.session.commit()
            return redirect('/')
        abort(404)
 
    return redirect('/')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop("login_id", None)
        login_id = request.form['login_id']
        user_password = request.form['user_password']

        user = EmployeeModel.query.filter_by(login_id=login_id).first()
        if user and user.user_password == user_password:
            session['login_id'] = user.login_id
            session['level'] = user.level
            session['user'] = user.user
            return redirect('/')
    
    return render_template('login.html')


@app.route('/logout')
def logout():
    if request.method == "GET":
        session.pop("login_id", None)
        return redirect('/login')

@app.route('/create/', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html', ReportSelectData_Program=ReportSelectData_Program, \
                ReportSelectData_Report_Type=ReportSelectData_Report_Type, \
                ReportSelectData_Report_Severity=ReportSelectData_Report_Severity, \
                ReportSelectData_ReportedBy=ReportSelectData_ReportedBy)
    
    if request.method == 'POST':
        program = request.form['program']
        report_type = request.form['report_type']
        severity = request.form['severity']
        summary = request.form['summary']
        problem = request.form['problem']
        reported_by = request.form['reported_by']
        date = request.form['date']
        if request.form['reproducible']:
            reproducible = True 
        else:
            reproducible = False
        
        bug_model = BugModel(program=program, report_type=report_type, severity=severity, reproducible=reproducible, summary=summary, problem=problem, reported_by=reported_by, date=date)
        db.session.add(bug_model)
        db.session.commit()
        
        return redirect('/')


@app.route('/<int:id>/update',methods = ['GET','POST'])
def update(id):
    bug_model = BugModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if bug_model:
            db.session.delete(bug_model)
            db.session.commit()
            
            program = request.form['program']
            report_type = request.form['report_type']
            severity = request.form['severity']
            summary = request.form['summary']
            problem = request.form['problem']
            reported_by = request.form['reported_by']
            date = request.form['date']
            
            bug_model = BugModel(program=program, report_type=report_type, severity=severity, \
                                reproducible= reproducible, summary=summary, \
                                problem=problem, reported_by=reported_by, date=date)
            
            db.session.add(bug_model)
            db.session.commit()
            return redirect('/')
        return f"Bug with id = {id} Does not exist"
 
    return render_template('update.html', bug_model=bug_model)

@app.route('/<int:id>/delete', methods=['GET'])
def delete(id):
    bug_model = BugModel.query.filter_by(id=id).first()
    if request.method == 'GET':
        if bug_model:
            db.session.delete(bug_model)
            db.session.commit()
            return redirect('/')
        abort(404)
 
    return redirect('/')

@app.route('/programs')
def list_programs():
    status = None
    level = None
    try:
        status = session['login_id']
        level = session['level']
        user = session['user']
    except:
        status = None
        level = None  
        user = None  
    if not status:
        return redirect('/login')
    else:
        programs = ProgramModel.query.all()
        return render_template('list_programs.html', programs=programs, status=status, level=level, user=user)

@app.route('/create_program', methods=['GET', 'POST'])
def create_program():
    if request.method == 'GET':
        return render_template('create_program.html')

    if request.method == 'POST':
        program = request.form['program']
        release = request.form['release']
        version = request.form['version']
        area = " "

        if  not program or not release or not version:
            return render_template('error.html')
        else:    
            program = ProgramModel(program=program, release=release, version=version, area=area)
            db.session.add(program)
            db.session.commit()

            return redirect('/')

@app.route('/program/<int:id>/update', methods=['GET', 'POST'])
def update_program(id):
    program = ProgramModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        program = request.form['program']
        release = request.form['release']
        version = request.form['version']
        area = request.form['area']

            
        program = ProgramModel(program=program, release=release, version=version, area=area)
        
        db.session.add(program)
        db.session.commit()
        return redirect('/')
 
    return render_template('update_program.html', program=program)


@app.route('/program/<int:id>/delete', methods=['GET'])
def delete_program(id):
    program = ProgramModel.query.filter_by(id=id).first()
    if request.method == 'GET':
        if program:
            db.session.delete(program)
            db.session.commit()
            return redirect('/')
        abort(404)
 
    return redirect('/')


if __name__ == "__main__":
    app.run(port=5000, debug=True)