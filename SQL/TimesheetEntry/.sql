CREATE TABLE Timesheet_database (
    Uniq_ID VARCHAR(255) PRIMARY KEY,
    EmpID VARCHAR(10) NOT NULL,
    DateofEntry DATE NOT NULL,
    StartTime VARCHAR(255),
    EndTime VARCHAR(255),
    Hours FLOAT,
    Minutes FLOAT,
    AllocationType VARCHAR(50),
    Category1 VARCHAR(50),
    Category2 VARCHAR(50),
    Category3 VARCHAR(50),
    ProjectCode VARCHAR(10),
    Category5 VARCHAR(50),
    Category6 VARCHAR(50),
    Comment VARCHAR(255),
    Team VARCHAR(255) NOT NULL,
    Status VARCHAR(20),
    SubmitDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    RecordType VARCHAR(50),
    WO_Percent FLOAT,
    WO_Units INT,
    NetUnits INT,
    BaseRate FLOAT,
    Billed_Label VARCHAR(50),
    WOFF_Reason VARCHAR(255),
    LastUploadDate DATETIME DEFAULT NULL,
    LastUpdatedBy VARCHAR(50),
    InvNum FLOAT,
    FinalRate FLOAT,
    SSMA_TimeStamp DATETIME
);
