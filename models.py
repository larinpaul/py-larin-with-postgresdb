from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}')"

# Run the following command to create the database tables:
# flask db init
# flask db migrate
# flask db upgrade
# This will create the database tables based on my models

class ProgramProject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    devicetypeid = db.Column(db.Integer, db.ForeignKey('devicetype.id'))
    programtypeid = db.Column(db.Integer, db.ForeignKey('programtype.id'))
    clienttypeid = db.Column(db.Integer, db.ForeignKey('clienttype.id'))
    localityid = db.Column(db.Integer, db.ForeignKey('locality.id'))
    teamtypeid = db.Column(db.Integer, db.ForeignKey('teamtype.id'))
    taskid = db.Column(db.Integer, db.ForeignKey('task.id'))
    startdate = db.Column(db.Date)

class DeviceType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class ProgramType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class ClientType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    optionsid = db.Column(db.Integer, db.ForeignKey('options.id'))
    expertassessmentid = db.Column(db.Integer, db.ForeignKey('expertassessment.id'))
    criteriatypeid = db.Column(db.Integer, db.ForeignKey('criteriatype.id'))

class Options(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class CriterionType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    criterionid = db.Column(db.Integer, db.ForeignKey('criterion.id'))
    name = db.Column(db.String)

class Criterion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class TeamType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teamid = db.Column(db.Integer, db.ForeignKey('team.id'))
    name = db.Column(db.String)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    managerstatusid = db.Column(db.Integer, db.ForeignKey('managerstatus.id'))
    developerid = db.Column(db.Integer, db.ForeignKey('developer.id'))

class ManagerStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class Developer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String)
    personalname = db.Column(db.String)
    patronym = db.Column(db.String)
    jobtitleid = db.Column(db.Integer, db.ForeignKey('jobtitle.id'))
    statusid = db.Column(db.Integer, db.ForeignKey('status.id'))

class ExpertAssessment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meaning = db.Column(db.String)

class JobTitle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class Locality(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

db.create_all()




