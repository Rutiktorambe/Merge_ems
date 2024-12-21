from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime, timezone

db = SQLAlchemy()

class EMPWD(db.Model, UserMixin):
    __tablename__ = 'EMPWD'
    
    EMPID = db.Column(db.String(255), primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    EName = db.Column(db.String(255))
    DOJRS = db.Column(db.Date) 
    DOJSIPL = db.Column(db.Date, nullable=True) 
    Profile = db.Column(db.String(255))
    Status = db.Column(db.String(50))
    SIPLLevel = db.Column(db.String(50))
    RSALevel = db.Column(db.String(50))
    EEMail = db.Column(db.String(255))
    IEMail = db.Column(db.String(255))
    Landline = db.Column(db.String(20))
    Mobile = db.Column(db.String(20))
    Ext = db.Column(db.String(10))
    Secretary = db.Column(db.String(255))
    SecretaryID = db.Column(db.String(255))
    SystemID = db.Column(db.String(255))
    Password = db.Column(db.String(255), nullable=False)
    Team = db.Column(db.String(255))
    LineManager = db.Column(db.String(255))
    LineManagerID = db.Column(db.String(255))
    AlternateContatName = db.Column(db.String(255))
    AlternateContatID = db.Column(db.String(255))
    DateofLeavingRSAASIPL = db.Column(db.Date)
    ReasonforLeaving = db.Column(db.String(255))
    LineManager2 = db.Column(db.String(255))
    ITAdmin = db.Column(db.String(255))
    HRAdmin = db.Column(db.String(255))
    TrnAdmin = db.Column(db.String(255))
    FinAdmin = db.Column(db.String(255))
    Field6 = db.Column(db.String(255))
    Field7 = db.Column(db.String(255))


    def get_id(self):
        return self.EMPID

class TimesheetEntry(db.Model):
    __tablename__ = 'Timesheet_database'
    
    Uniq_ID = db.Column(db.String(255), primary_key=True)
    EmpID = db.Column(db.String(10), nullable=False)
    DateofEntry = db.Column(db.Date, nullable=False)
    StartTime = db.Column(db.String(255))
    EndTime = db.Column(db.String(255))
    Hours = db.Column(db.Float)
    Minutes = db.Column(db.Float)
    AllocationType = db.Column(db.String(50))
    Category1 = db.Column(db.String(50))
    Category2 = db.Column(db.String(50))
    Category3 = db.Column(db.String(50))
    ProjectCode = db.Column(db.String(10))
    Category5 = db.Column(db.String(50))
    Category6 = db.Column(db.String(50))
    Comment = db.Column(db.String(255))
    Team = db.Column(db.String(255), nullable=False)
    Status = db.Column(db.String(20))
    SubmitDate = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))  
    RecordType = db.Column(db.String(50))
    WO_Percent = db.Column(db.Float)
    WO_Units = db.Column(db.Integer)
    NetUnits = db.Column(db.Integer)
    BaseRate = db.Column(db.Float)
    Billed_Label = db.Column(db.String(50))
    WOFF_Reason = db.Column(db.String(255))
    LastUploadDate = db.Column(db.DateTime, onupdate=lambda: datetime.now(timezone.utc))
    LastUpdatedBy = db.Column(db.String(50))
    InvNum =db.Column(db.Float)
    FinalRate = db.Column(db.Float)
    SSMA_TimeStamp = db.Column(db.DateTime )

    def __repr__(self):
        return f'<TimesheetEntry {self.Uniq_ID}>'

class Resourceinfo(db.Model, UserMixin):
    __tablename__ = 'ResourceInfo'
    
    ProjectCode = db.Column(db.String(100),primary_key=True)
    SSMA_Timestamp = db.Column(
        db.TIMESTAMP, 
        primary_key=True, 
        default=datetime.now(timezone.utc), 
        onupdate=datetime.now(timezone.utc)
    )
    EmpID = db.Column(db.String(100), primary_key=True)
    
    ProjectName = db.Column(db.String(255), nullable=False)
    Team = db.Column(db.String(100))
    EName = db.Column(db.String(255))
    Skill = db.Column(db.String(255))
    Occupancy = db.Column(db.String(255))
    FromDate = db.Column(db.Date)
    ToDate = db.Column(db.Date)
    Level = db.Column(db.String(255))
    Allocation = db.Column(db.Float)
    Status = db.Column(db.String(50))

    def __repr__(self):
        return f"<Resourceinfo(ProjectCode={self.ProjectCode}, ProjectName={self.ProjectName}, EmpID={self.EmpID})>"


class Trainings(db.Model, UserMixin):
    __tablename__ = 'Trainings'
    TID = db.Column(db.String(255), nullable=False, primary_key=True)
    EmpID = db.Column(db.String(255), nullable=False)
    TName = db.Column(db.String(255), nullable=False)
    TCat = db.Column(db.String(255), nullable=False)
    TDate = db.Column(db.Date, nullable=False)
    TDuration = db.Column(db.Float, nullable=False)
    TTime = db.Column(db.Float, nullable=False)
    Seats = db.Column(db.String(255), nullable=False)
    Relevance = db.Column(db.String(255), nullable=False)
    Comment = db.Column(db.String(255), nullable=False)
    TType = db.Column(db.String(255), nullable=False)
    Venue = db.Column(db.String(255), nullable=False)
    TPresenter = db.Column(db.String(255), nullable=False)
    TTravel = db.Column(db.String(255), nullable=False)
    TAcc = db.Column(db.String(255), nullable=False)
    TLevel1 = db.Column(db.String(255), nullable=False)
    TLevel2 = db.Column(db.String(255), nullable=False)
    TApproval = db.Column(db.String(255), nullable=False)
    SSMA_Timestamp = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<Training(TID={self.TID}, TName={self.TName})>"


class TrainingRegistration(db.Model, UserMixin):
    __tablename__ = 'TrainingRegistration'
    TID = db.Column(db.String(255), nullable=False, primary_key=True)
    EmpID = db.Column(db.String(255), nullable=False, primary_key=True)
    Status = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<TrainingRegistration(TID={self.TID}, EmpID={self.EmpID})>"
