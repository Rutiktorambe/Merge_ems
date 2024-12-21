CREATE TABLE EmpWD (
    EMPID VARCHAR(255) PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    EName VARCHAR(255),
    DOJRS DATE,
    DOJSIPL DATE,
    Profile VARCHAR(255),
    Status VARCHAR(50),
    SIPLLevel VARCHAR(50),
    RSALevel VARCHAR(50),
    EEMail VARCHAR(255),
    IEMail VARCHAR(255),
    Landline VARCHAR(20),
    Mobile VARCHAR(20),
    Ext VARCHAR(10),
    Secretary VARCHAR(255),
    SecretaryID VARCHAR(255),
    SystemID VARCHAR(255),
    Password VARCHAR(255) NOT NULL,
    Team VARCHAR(255),
    LineManager VARCHAR(255),
    LineManagerID VARCHAR(255),
    AlternateContatName VARCHAR(255),
    AlternateContatID VARCHAR(255),
    DateofLeavingRSAASIPL DATE,
    ReasonforLeaving VARCHAR(255),
    LineManager2 VARCHAR(255),
    ITAdmin VARCHAR(255),
    HRAdmin VARCHAR(255),
    TrnAdmin VARCHAR(255),
    FinAdmin VARCHAR(255),
    Field6 VARCHAR(255),
    Field7 VARCHAR(255)
);


-- Insert data into the EmpWD table
INSERT INTO EmpWD (
    EMPID, username, EName, DOJRS, DOJSIPL, Profile, Status, SIPLLevel, RSALevel, 
    EEMail, IEMail, Landline, Mobile, Ext, Secretary, SecretaryID, SystemID, 
    Password, Team, LineManager, LineManagerID, AlternateContatName, AlternateContatID, 
    DateofLeavingRSAASIPL, ReasonforLeaving, LineManager2, ITAdmin, HRAdmin, 
    TrnAdmin, FinAdmin, Field6, Field7
) VALUES
-- A00001 entry
('A00001', 'DoeJo', 'John Doe', '2020-01-15', '2020-03-01', 'Analytics', 'Active', 'Level 1', 'Level 1',
 'johndoe@example.com', 'john.doe@internal.com', '123456789', '987654321', '101', NULL, NULL, 'SYS001',
 'pass', 'Pricing', 'Emma Watson', 'A00005', NULL, NULL, NULL, NULL, NULL, 'IT Admin', 'HR Admin',
 'Training Admin', 'Finance Admin', 'Extra Field 6', 'Extra Field 7'),

-- A00002 entry
('A00002', 'SmithJa', 'James Smith', '2020-02-01', '2020-04-01', 'Consultant', 'Active', 'Level 2', 'Level 2',
 'jamessmith@example.com', 'james.smith@internal.com', '123456789', '987654321', '102', NULL, NULL, 'SYS002',
 'pass', 'Capital', 'John Doe', 'A00001', NULL, NULL, NULL, NULL, NULL, 'IT Admin', 'HR Admin',
 'Training Admin', 'Finance Admin', 'Extra Field 6', 'Extra Field 7'),

-- A00003 entry
('A00003', 'BrownSa', 'Sarah Brown', '2020-03-01', '2020-05-01', 'Sr Consultant', 'Active', 'Level 3', 'Level 3',
 'sarahbrown@example.com', 'sarah.brown@internal.com', '123456789', '987654321', '103', NULL, NULL, 'SYS003',
 'pass', 'Analytics', 'James Smith', 'A00002', NULL, NULL, NULL, NULL, NULL, 'IT Admin', 'HR Admin',
 'Training Admin', 'Finance Admin', 'Extra Field 6', 'Extra Field 7'),

-- A00004 entry
('A00004', 'WhiteMa', 'Mary White', '2020-04-01', '2020-06-01', 'Consultant', 'Active', 'Level 4', 'Level 4',
 'marywhite@example.com', 'mary.white@internal.com', '123456789', '987654321', '104', NULL, NULL, 'SYS004',
 'pass', 'Reserving', 'Sarah Brown', 'A00003', NULL, NULL, NULL, NULL, NULL, 'IT Admin', 'HR Admin',
 'Training Admin', 'Finance Admin', 'Extra Field 6', 'Extra Field 7'),

-- A00005 entry
('A00005', 'WatsonEm', 'Emma Watson', '2020-05-01', '2020-07-01', 'Analytics', 'Active', 'Level 5', 'Level 5',
 'emmawatson@example.com', 'emma.watson@internal.com', '123456789', '987654321', '105', NULL, NULL, 'SYS005',
 'pass', 'IT', 'Mary White', 'A00004', NULL, NULL, NULL, NULL, NULL, 'IT Admin', 'HR Admin',
 'Training Admin', 'Finance Admin', 'Extra Field 6', 'Extra Field 7'),

-- A00006 entry
('A00006', 'BlackMi', 'Michael Black', '2020-06-01', '2020-08-01', 'Consultant', 'Active', 'Level 6', 'Level 6',
 'michaelblack@example.com', 'michael.black@internal.com', '123456789', '987654321', '106', NULL, NULL, 'SYS006',
 'pass', 'HR', 'Emma Watson', 'A00005', NULL, NULL, NULL, NULL, NULL, 'IT Admin', 'HR Admin',
 'Training Admin', 'Finance Admin', 'Extra Field 6', 'Extra Field 7'),

-- A00007 entry
('A00007', 'GreenWi', 'William Green', '2020-07-01', '2020-09-01', 'Sr Consultant', 'Active', 'Level 7', 'Level 7',
 'williamgreen@example.com', 'william.green@internal.com', '123456789', '987654321', '107', NULL, NULL, 'SYS007',
 'pass', 'CIO-UK', 'Michael Black', 'A00006', NULL, NULL, NULL, NULL, NULL, 'IT Admin', 'HR Admin',
 'Training Admin', 'Finance Admin', 'Extra Field 6', 'Extra Field 7'),

-- A00008 entry
('A00008', 'JohnsonJa', 'Jack Johnson', '2020-08-01', '2020-10-01', 'Analytics', 'Active', 'Level 8', 'Level 8',
 'jackjohnson@example.com', 'jack.johnson@internal.com', '123456789', '987654321', '108', NULL, NULL, 'SYS008',
 'pass', 'Finance', 'William Green', 'A00007', NULL, NULL, NULL, NULL, NULL, 'IT Admin', 'HR Admin',
 'Training Admin', 'Finance Admin', 'Extra Field 6', 'Extra Field 7'),

-- A00009 entry
('A00009', 'TaylorEl', 'Elizabeth Taylor', '2020-09-01', '2020-11-01', 'Consultant', 'Active', 'Level 9', 'Level 9',
 'elizabethtaylor@example.com', 'elizabeth.taylor@internal.com', '123456789', '987654321', '109', NULL, NULL, 'SYS009',
 'pass', 'Pricing', 'Jack Johnson', 'A00008', NULL, NULL, NULL, NULL, NULL, 'IT Admin', 'HR Admin',
 'Training Admin', 'Finance Admin', 'Extra Field 6', 'Extra Field 7'),

-- A00010 entry
('A00010', 'MooreHa', 'Hannah Moore', '2020-10-01', '2020-12-01', 'Analytics', 'Active', 'Level 10', 'Level 10',
 'hannahmoore@example.com', 'hannah.moore@internal.com', '123456789', '987654321', '110', NULL, NULL, 'SYS010',
 'pass', 'Analytics', 'Elizabeth Taylor', 'A00009', NULL, NULL, NULL, NULL, NULL, 'IT Admin', 'HR Admin',
 'Training Admin', 'Finance Admin', 'Extra Field 6', 'Extra Field 7');
