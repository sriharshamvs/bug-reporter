from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()


class ProgramModel(db.Model):
    __tablename__ = "program"

    id = db.Column(db.Integer, primary_key=True)
    program = db.Column(db.String())
    release = db.Column(db.String())
    version = db.Column(db.String())
    area = db.Column(db.String())

    def __init__(self, program, release, version, area):
        self.program = program
        self.release = release
        self.version = version
        self.area = area

    def __repr__(self):
        return f"{self.program}: {self.release}: {self.version} : {self.area}"

class EmployeeModel(db.Model):
    __tablename__ = "employee"

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String())
    login_id = db.Column(db.String())
    level = db.Column(db.Integer)
    user_password = db.Column(db.String())

    def __init__(self, user, login_id, level, user_password):
        self.user = user
        self.login_id = login_id
        self.level = level
        self.user_password = user_password

    def __repr__(self):
        return f"{self.user}: {self.login_id}: {self.level} : {self.user_password}"

class BugModel(db.Model):
    __tablename__ = "bug"
 
    id = db.Column(db.Integer, primary_key=True)
    program = db.Column(db.String())
    report_type = db.Column(db.String())
    severity = db.Column(db.String())
    reproducible = db.Column(db.Boolean())
    summary = db.Column(db.String())
    problem = db.Column(db.String())
    reported_by = db.Column(db.String())
    date = db.Column(db.String())
    area = db.Column(db.String())
    assigned_to = db.Column(db.String())
    priority = db.Column(db.String())
    resolution = db.Column(db.String())
    resolved_by = db.Column(db.String())
    status = db.Column(db.String())

    def __init__(self, program, report_type, severity, reproducible, summary, problem, reported_by, date, area, assigned_to, priority, resolution, resolved_by, status):
        self.program = program
        self.report_type = report_type
        self.severity = severity
        self.reproducible = reproducible
        self.summary = summary
        self.problem = problem
        self.reported_by = reported_by
        self.date = date
        self.area = area
        self.assigned_to = assigned_to
        self.priority = priority
        self.resolution = resolution
        self.resolved_by = resolved_by
        self.status = status
 
    def __repr__(self):
        return f"{self.program} : {self.report_type} : {self.severity} : {self.reproducible} : {self.summary} : {self.problem} : {self.reported_by} : {self.date}"


 