CREATE TABLE EMPWD (
EMPID VARCHAR(255) NOT NULL,
username VARCHAR(255) NOT NULL,
EName VARCHAR(255),
DOJRS DATE,
DOJSIPL DATE,
Profile VARCHAR(255),
Status VARCHAR(255),
SIPLLevel VARCHAR(255),
RSALevel VARCHAR(255),
EEMail VARCHAR(255),
IEMail VARCHAR(255),
Landline VARCHAR(255),
Mobile VARCHAR(255),
Ext VARCHAR(255),
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
Field7 VARCHAR(255),
PRIMARY KEY (EMPID, username)
);

-- Insert dummy data into EMPWD table
INSERT INTO EMPWD (
EMPID, username, EName, DOJRS, DOJSIPL, Profile, Status, SIPLLevel, RSALevel,
EEMail, IEMail, Landline, Mobile, Ext, Secretary, SecretaryID, SystemID, Password,
Team, LineManager, LineManagerID, AlternateContatName, AlternateContatID,
DateofLeavingRSAASIPL, ReasonforLeaving, LineManager2, ITAdmin, HRAdmin, TrnAdmin,
FinAdmin, Field6, Field7
) VALUES
-- Employee 1
('C001', 'johnsm', 'John Smith', '2022-01-15', '2022-02-01', 'Analyst', 'Active', 'Level 1', 'Intern',
'johnsm@rsadummy.com', 'johnsmith@internal.com', '123456789', '9876543210', '101', 'Anna Taylor',
'C005', 'SYS001', 'pass', 'Pricing', 'janedo', 'C002', 'Emily Watson', 'C003', NULL, NULL,
'susanjo', 'C004', NULL, NULL, NULL, NULL, NULL),

-- Employee 2
('C002', 'janedo', 'Jane Doe', '2021-03-10', '2021-04-01', 'Consultant', 'Active', 'Level 2', 'Consultant',
'janedo@rsadummy.com', 'janedoe@internal.com', '123456780', '9876543211', '102', 'Emily Watson',
'C003', 'SYS002', 'pass', 'Capital', 'susanjo', 'C004', 'Michael King', 'C006', NULL, NULL,
'mariath', 'C007', NULL, NULL, NULL, NULL, NULL),

-- Employee 3
('C003', 'emilywa', 'Emily Watson', '2020-05-20', '2020-06-01', 'Senior Analyst', 'Active', 'Level 3', 'Sr Consultant',
'emilywa@rsadummy.com', 'emilywatson@internal.com', '123456781', '9876543212', '103', 'Michael King',
'C006', 'SYS003', 'pass', 'Analytics', 'mariath', 'C007', 'Alice Moore', 'C008', NULL, NULL,
'susanjo', 'C004', NULL, NULL, NULL, NULL, NULL),

-- Employee 4
('C004', 'susanjo', 'Susan Johnson', '2019-07-15', '2019-08-01', 'Manager', 'Active', 'Level 4', 'Manager',
'susanjo@rsadummy.com', 'susanjohnson@internal.com', '123456782', '9876543213', '104', 'Alice Moore',
'C008', 'SYS004', 'pass', 'Reserving', 'alicewh', 'C009', 'David Brown', 'C010', NULL, NULL,
'mariath', 'C007', NULL, NULL, NULL, NULL, NULL),

-- Employee 5
('C005', 'annata', 'Anna Taylor', '2022-03-10', '2022-04-01', 'Junior Analyst', 'Active', 'Level 1', 'Intern',
'annata@rsadummy.com', 'annataylor@internal.com', '123456783', '9876543214', '105', 'David Brown',
'C010', 'SYS005', 'pass', 'IT', 'alicewh', 'C009', 'Jane Doe', 'C002', NULL, NULL,
'emilywa', 'C003', NULL, NULL, NULL, NULL, NULL),

-- Employee 6
('C006', 'michaki', 'Michael King', '2021-09-15', '2021-10-01', 'Consultant', 'Active', 'Level 2', 'Consultant',
'michaki@rsadummy.com', 'michaelking@internal.com', '123456784', '9876543215', '106', 'Susan Johnson',
'C004', 'SYS006', 'pass', 'HR', 'johnsm', 'C001', 'John Smith', 'C001', NULL, NULL,
'annata', 'C005', NULL, NULL, NULL, NULL, NULL),

-- Employee 7
('C007', 'mariath', 'Maria Thomas', '2020-12-01', '2021-01-01', 'Senior Manager', 'Active', 'Level 5', 'Sr Consultant',
'mariath@rsadummy.com', 'mariathomas@internal.com', '123456785', '9876543216', '107', 'Jane Doe',
'C002', 'SYS007', 'pass', 'CIO-UK', 'susanjo', 'C004', 'Susan Johnson', 'C004', NULL, NULL,
'michaki', 'C006', NULL, NULL, NULL, NULL, NULL),

-- Employee 8
('C008', 'alicemo', 'Alice Moore', '2021-02-10', '2021-03-01', 'IT Admin', 'Active', 'Level 2', 'Analyst',
'alicemo@rsadummy.com', 'alicemoore@internal.com', '123456786', '9876543217', '108', 'Michael King',
'C006', 'SYS008', 'pass', 'Capital', 'emilywa', 'C003', 'Emily Watson', 'C003', NULL, NULL,
'michaki', 'C006', NULL, NULL, NULL, NULL, NULL),

-- Employee 9
('C009', 'alicewh', 'Alice White', '2018-04-20', '2018-05-01', 'Finance Lead', 'Active', 'Level 6', 'Head',
'alicewh@rsadummy.com', 'alicewhite@internal.com', '123456787', '9876543218', '109', 'David Brown',
'C010', 'SYS009', 'pass', 'Finance', 'michaki', 'C006', 'Michael King', 'C006', NULL, NULL,
'susanjo', 'C004', NULL, NULL, NULL, NULL, NULL),

-- Employee 10
('C010', 'davidbr', 'David Brown', '2017-11-05', '2017-12-01', 'Director', 'Active', 'Level 6', 'Head',
'davidbr@rsadummy.com', 'davidbrown@internal.com', '123456788', '9876543219', '110', 'Anna Taylor',
'C005', 'SYS010', 'pass', 'Analytics', 'alicemo', 'C008', 'Alice Moore', 'C008', NULL, NULL,
'alicemo', 'C008', NULL, NULL, NULL, NULL, NULL);

-- Insert additional dummy data into EMPWD table
INSERT INTO EMPWD (
EMPID, username, EName, DOJRS, DOJSIPL, Profile, Status, SIPLLevel, RSALevel,
EEMail, IEMail, Landline, Mobile, Ext, Secretary, SecretaryID, SystemID, Password,
Team, LineManager, LineManagerID, AlternateContatName, AlternateContatID,
DateofLeavingRSAASIPL, ReasonforLeaving, LineManager2, ITAdmin, HRAdmin, TrnAdmin,
FinAdmin, Field6, Field7
) VALUES
-- Employee 11
('C011', 'markjo', 'Mark Johnson', '2023-01-10', '2023-02-01', 'Analyst', 'Active', 'Level 1', 'Intern',
'markjo@rsadummy.com', 'markjohnson@internal.com', '1234567891', '9876543220', '111', 'Anna Taylor',
'C005', 'SYS011', 'pass', 'Reserving', 'emilywa', 'C003', 'Susan Davis', 'C012', NULL, NULL,
'alicemo', 'C008', NULL, NULL, NULL, NULL, NULL),

-- Employee 12
('C012', 'susand', 'Susan Davis', '2022-09-15', '2022-10-01', 'Consultant', 'Active', 'Level 2', 'Consultant',
'susand@rsadummy.com', 'susandavis@internal.com', '1234567892', '9876543221', '112', 'Michael King',
'C006', 'SYS012', 'pass', 'HR', 'johnsm', 'C001', 'Mark Johnson', 'C011', NULL, NULL,
'alicemo', 'C008', NULL, NULL, NULL, NULL, NULL),

-- Employee 13
('C013', 'paulwi', 'Paul Wilson', '2021-06-05', '2021-07-01', 'Senior Analyst', 'Active', 'Level 3', 'Sr Consultant',
'paulwi@rsadummy.com', 'paulwilson@internal.com', '1234567893', '9876543222', '113', 'Emily Watson',
'C003', 'SYS013', 'pass', 'Pricing', 'janedo', 'C002', 'Susan Davis', 'C012', NULL, NULL,
'mariath', 'C007', NULL, NULL, NULL, NULL, NULL),

-- Employee 14
('C014', 'nancymo', 'Nancy Moore', '2020-03-15', '2020-04-01', 'Manager', 'Active', 'Level 4', 'Manager',
'nancymo@rsadummy.com', 'nancymoore@internal.com', '1234567894', '9876543223', '114', 'Mark Johnson',
'C011', 'SYS014', 'pass', 'Capital', 'susand', 'C012', 'Paul Wilson', 'C013', NULL, NULL,
'mariath', 'C007', NULL, NULL, NULL, NULL, NULL),

-- Employee 15
('C015', 'ericbr', 'Eric Brown', '2019-10-25', '2019-11-01', 'Consultant', 'Active', 'Level 2', 'Consultant',
'ericbr@rsadummy.com', 'ericbrown@internal.com', '1234567895', '9876543224', '115', 'Nancy Moore',
'C014', 'SYS015', 'pass', 'Analytics', 'janedo', 'C002', 'Nancy Moore', 'C014', NULL, NULL,
'paulwi', 'C013', NULL, NULL, NULL, NULL, NULL),

-- Employee 16
('C016', 'laurath', 'Laura Thomas', '2021-12-01', '2022-01-01', 'Analyst', 'Active', 'Level 1', 'Intern',
'laurath@rsadummy.com', 'laurathomas@internal.com', '1234567896', '9876543225', '116', 'Paul Wilson',
'C013', 'SYS016', 'pass', 'IT', 'ericbr', 'C015', 'Eric Brown', 'C015', NULL, NULL,
'nancymo', 'C014', NULL, NULL, NULL, NULL, NULL),

-- Employee 17
('C017', 'bradco', 'Brad Cooper', '2020-08-10', '2020-09-01', 'Senior Manager', 'Active', 'Level 5', 'Sr Consultant',
'bradco@rsadummy.com', 'bradcooper@internal.com', '1234567897', '9876543226', '117', 'Laura Thomas',
'C016', 'SYS017', 'pass', 'CIO-UK', 'nancymo', 'C014', 'Laura Thomas', 'C016', NULL, NULL,
'laurath', 'C016', NULL, NULL, NULL, NULL, NULL),

-- Employee 18
('C018', 'kevinan', 'Kevin Anderson', '2021-05-10', '2021-06-01', 'IT Admin', 'Active', 'Level 2', 'Analyst',
'kevinan@rsadummy.com', 'kevinanderson@internal.com', '1234567898', '9876543227', '118', 'Brad Cooper',
'C017', 'SYS018', 'pass', 'Pricing', 'susand', 'C012', 'Brad Cooper', 'C017', NULL, NULL,
'laurath', 'C016', NULL, NULL, NULL, NULL, NULL),

-- Employee 19
('C019', 'chrispa', 'Chris Parker', '2020-01-20', '2020-02-01', 'Finance Lead', 'Active', 'Level 6', 'Head',
'chrispa@rsadummy.com', 'chrisparker@internal.com', '1234567899', '9876543228', '119', 'Eric Brown',
'C015', 'SYS019', 'pass', 'Finance', 'kevinan', 'C018', 'Kevin Anderson', 'C018', NULL, NULL,
'bradco', 'C017', NULL, NULL, NULL, NULL, NULL),

-- Employee 20
('C020', 'sarajon', 'Sara Johnson', '2019-03-10', '2019-04-01', 'Director', 'Active', 'Level 6', 'Head',
'sarajon@rsadummy.com', 'sarajohnson@internal.com', '1234567800', '9876543229', '120', 'Chris Parker',
'C019', 'SYS020', 'pass', 'Reserving', 'chrispa', 'C019', 'Chris Parker', 'C019', NULL, NULL,
'kevinan', 'C018', NULL, NULL, NULL, NULL, NULL);

-- Insert additional dummy data into EMPWD table
INSERT INTO EMPWD (
EMPID, username, EName, DOJRS, DOJSIPL, Profile, Status, SIPLLevel, RSALevel,
EEMail, IEMail, Landline, Mobile, Ext, Secretary, SecretaryID, SystemID, Password,
Team, LineManager, LineManagerID, AlternateContatName, AlternateContatID,
DateofLeavingRSAASIPL, ReasonforLeaving, LineManager2, ITAdmin, HRAdmin, TrnAdmin,
FinAdmin, Field6, Field7
) VALUES
-- Employee 21
('C021', 'mikeru', 'Mike Russell', '2023-05-10', '2023-06-01', 'Analyst', 'Active', 'Level 1', 'Intern',
'mikeru@rsadummy.com', 'mikerussell@internal.com', '1234567801', '9876543230', '121', 'Sara Johnson',
'C020', 'SYS021', 'pass', 'Pricing', 'chrispa', 'C019', 'Laura Smith', 'C022', NULL, NULL,
'sarajon', 'C020', NULL, NULL, NULL, NULL, NULL),

-- Employee 22
('C022', 'laurasm', 'Laura Smith', '2022-10-15', '2022-11-01', 'Consultant', 'Active', 'Level 2', 'Consultant',
'laurasm@rsadummy.com', 'laurasmith@internal.com', '1234567802', '9876543231', '122', 'Mike Russell',
'C021', 'SYS022', 'pass', 'Analytics', 'sarajon', 'C020', 'Sara Johnson', 'C020', NULL, NULL,
'mikeru', 'C021', NULL, NULL, NULL, NULL, NULL),

-- Employee 23
('C023', 'davidle', 'David Lee', '2021-07-05', '2021-08-01', 'Senior Analyst', 'Active', 'Level 3', 'Sr Consultant',
'davidle@rsadummy.com', 'davidlee@internal.com', '1234567803', '9876543232', '123', 'Laura Smith',
'C022', 'SYS023', 'pass', 'Capital', 'laurasm', 'C022', 'Mike Russell', 'C021', NULL, NULL,
'sarajon', 'C020', NULL, NULL, NULL, NULL, NULL),

-- Employee 24
('C024', 'julieha', 'Julie Harris', '2020-12-15', '2021-01-01', 'Manager', 'Active', 'Level 4', 'Manager',
'julieha@rsadummy.com', 'julieharris@internal.com', '1234567804', '9876543233', '124', 'David Lee',
'C023', 'SYS024', 'pass', 'Reserving', 'davidle', 'C023', 'Laura Smith', 'C022', NULL, NULL,
'mikeru', 'C021', NULL, NULL, NULL, NULL, NULL),

-- Employee 25
('C025', 'patribr', 'Patrick Brown', '2019-08-20', '2019-09-01', 'Consultant', 'Active', 'Level 2', 'Consultant',
'patribr@rsadummy.com', 'patrickbrown@internal.com', '1234567805', '9876543234', '125', 'Julie Harris',
'C024', 'SYS025', 'pass', 'HR', 'julieha', 'C024', 'David Lee', 'C023', NULL, NULL,
'laurasm', 'C022', NULL, NULL, NULL, NULL, NULL),

-- Employee 26
('C026', 'helenad', 'Helen Adams', '2021-03-01', '2021-04-01', 'Analyst', 'Active', 'Level 1', 'Intern',
'helenad@rsadummy.com', 'helenadams@internal.com', '1234567806', '9876543235', '126', 'Patrick Brown',
'C025', 'SYS026', 'pass', 'IT', 'patribr', 'C025', 'Patrick Brown', 'C025', NULL, NULL,
'julieha', 'C024', NULL, NULL, NULL, NULL, NULL),

-- Employee 27
('C027', 'tomhug', 'Tom Hughes', '2020-09-10', '2020-10-01', 'Senior Manager', 'Active', 'Level 5', 'Sr Consultant',
'tomhug@rsadummy.com', 'tomhughes@internal.com', '1234567807', '9876543236', '127', 'Helen Adams',
'C026', 'SYS027', 'pass', 'CIO-UK', 'julieha', 'C024', 'Helen Adams', 'C026', NULL, NULL,
'helenad', 'C026', NULL, NULL, NULL, NULL, NULL),

-- Employee 28
('C028', 'chrislo', 'Chris Logan', '2021-11-10', '2021-12-01', 'IT Admin', 'Active', 'Level 2', 'Analyst',
'chrislo@rsadummy.com', 'chrislogan@internal.com', '1234567808', '9876543237', '128', 'Tom Hughes',
'C027', 'SYS028', 'pass', 'Analytics', 'patribr', 'C025', 'Tom Hughes', 'C027', NULL, NULL,
'helenad', 'C026', NULL, NULL, NULL, NULL, NULL),

-- Employee 29
('C029', 'amyray', 'Amy Ray', '2020-02-25', '2020-03-01', 'Finance Lead', 'Active', 'Level 6', 'Head',
'amyray@rsadummy.com', 'amyray@internal.com', '1234567809', '9876543238', '129', 'Chris Logan',
'C028', 'SYS029', 'pass', 'Finance', 'chrislo', 'C028', 'Chris Logan', 'C028', NULL, NULL,
'tomhug', 'C027', NULL, NULL, NULL, NULL, NULL),

-- Employee 30
('C030', 'samanpe', 'Samantha Perry', '2019-05-15', '2019-06-01', 'Director', 'Active', 'Level 6', 'Head',
'samanpe@rsadummy.com', 'samanthaperry@internal.com', '1234567810', '9876543239', '130', 'Amy Ray',
'C029', 'SYS030', 'pass', 'Reserving', 'amyray', 'C029', 'Amy Ray', 'C029', NULL, NULL,
'chrislo', 'C028', NULL, NULL, NULL, NULL, NULL);

-- Insert additional dummy data into EMPWD table
INSERT INTO EMPWD (
EMPID, username, EName, DOJRS, DOJSIPL, Profile, Status, SIPLLevel, RSALevel,
EEMail, IEMail, Landline, Mobile, Ext, Secretary, SecretaryID, SystemID, Password,
Team, LineManager, LineManagerID, AlternateContatName, AlternateContatID,
DateofLeavingRSAASIPL, ReasonforLeaving, LineManager2, ITAdmin, HRAdmin, TrnAdmin,
FinAdmin, Field6, Field7
) VALUES
-- Employee 31
('C031', 'danieljo', 'Daniel Jones', '2023-07-01', '2023-08-01', 'Analyst', 'Active', 'Level 1', 'Intern',
'danieljo@rsadummy.com', 'danieljones@internal.com', '1234567811', '9876543240', '131', 'Samantha Perry',
'C030', 'SYS031', 'pass', 'Pricing', 'amyray', 'C029', 'Sophia Carter', 'C032', NULL, NULL,
'samanpe', 'C030', NULL, NULL, NULL, NULL, NULL),

-- Employee 32
('C032', 'sophiaca', 'Sophia Carter', '2022-05-10', '2022-06-01', 'Consultant', 'Active', 'Level 2', 'Consultant',
'sophiaca@rsadummy.com', 'sophiacarter@internal.com', '1234567812', '9876543241', '132', 'Daniel Jones',
'C031', 'SYS032', 'pass', 'Analytics', 'samanpe', 'C030', 'Samantha Perry', 'C030', NULL, NULL,
'danieljo', 'C031', NULL, NULL, NULL, NULL, NULL),

-- Employee 33
('C033', 'lucasba', 'Lucas Baker', '2021-08-20', '2021-09-01', 'Senior Analyst', 'Active', 'Level 3', 'Sr Consultant',
'lucasba@rsadummy.com', 'lucasbaker@internal.com', '1234567813', '9876543242', '133', 'Sophia Carter',
'C032', 'SYS033', 'pass', 'Capital', 'sophiaca', 'C032', 'Daniel Jones', 'C031', NULL, NULL,
'samanpe', 'C030', NULL, NULL, NULL, NULL, NULL),

-- Employee 34
('C034', 'clairebl', 'Claire Black', '2020-10-15', '2020-11-01', 'Manager', 'Active', 'Level 4', 'Manager',
'clairebl@rsadummy.com', 'claireblack@internal.com', '1234567814', '9876543243', '134', 'Lucas Baker',
'C033', 'SYS034', 'pass', 'Reserving', 'lucasba', 'C033', 'Sophia Carter', 'C032', NULL, NULL,
'danieljo', 'C031', NULL, NULL, NULL, NULL, NULL),

-- Employee 35
('C035', 'liambe', 'Liam Bennett', '2019-09-25', '2019-10-01', 'Consultant', 'Active', 'Level 2', 'Consultant',
'liambe@rsadummy.com', 'liambennett@internal.com', '1234567815', '9876543244', '135', 'Claire Black',
'C034', 'SYS035', 'pass', 'HR', 'clairebl', 'C034', 'Lucas Baker', 'C033', NULL, NULL,
'sophiaca', 'C032', NULL, NULL, NULL, NULL, NULL),

-- Employee 36
('C036', 'emmalo', 'Emma Lopez', '2021-01-15', '2021-02-01', 'Analyst', 'Active', 'Level 1', 'Intern',
'emmalo@rsadummy.com', 'emmalopez@internal.com', '1234567816', '9876543245', '136', 'Liam Bennett',
'C035', 'SYS036', 'pass', 'IT', 'liambe', 'C035', 'Liam Bennett', 'C035', NULL, NULL,
'clairebl', 'C034', NULL, NULL, NULL, NULL, NULL),

-- Employee 37
('C037', 'jacobhe', 'Jacob Hernandez', '2020-04-20', '2020-05-01', 'Senior Manager', 'Active', 'Level 5', 'Sr Consultant',
'jacobhe@rsadummy.com', 'jacobhernandez@internal.com', '1234567817', '9876543246', '137', 'Emma Lopez',
'C036', 'SYS037', 'pass', 'CIO-UK', 'clairebl', 'C034', 'Emma Lopez', 'C036', NULL, NULL,
'emmalo', 'C036', NULL, NULL, NULL, NULL, NULL),

-- Employee 38
('C038', 'harrygr', 'Harry Green', '2021-03-10', '2021-04-01', 'IT Admin', 'Active', 'Level 2', 'Analyst',
'harrygr@rsadummy.com', 'harrygreen@internal.com', '1234567818', '9876543247', '138', 'Jacob Hernandez',
'C037', 'SYS038', 'pass', 'Analytics', 'liambe', 'C035', 'Jacob Hernandez', 'C037', NULL, NULL,
'emmalo', 'C036', NULL, NULL, NULL, NULL, NULL),

-- Employee 39
('C039', 'isabelmi', 'Isabel Miller', '2020-02-10', '2020-03-01', 'Finance Lead', 'Active', 'Level 6', 'Head',
'isabelmi@rsadummy.com', 'isabelmiller@internal.com', '1234567819', '9876543248', '139', 'Harry Green',
'C038', 'SYS039', 'pass', 'Finance', 'harrygr', 'C038', 'Harry Green', 'C038', NULL, NULL,
'jacobhe', 'C037', NULL, NULL, NULL, NULL, NULL),

-- Employee 40
('C040', 'oliviac', 'Olivia Clark', '2019-06-15', '2019-07-01', 'Director', 'Active', 'Level 6', 'Head',
'oliviac@rsadummy.com', 'oliviaclark@internal.com', '1234567820', '9876543249', '140', 'Isabel Miller',
'C039', 'SYS040', 'pass', 'Reserving', 'isabelmi', 'C039', 'Isabel Miller', 'C039', NULL, NULL,
'harrygr', 'C038', NULL, NULL, NULL, NULL, NULL);

-- Insert additional dummy data into EMPWD table
INSERT INTO EMPWD (
EMPID, username, EName, DOJRS, DOJSIPL, Profile, Status, SIPLLevel, RSALevel,
EEMail, IEMail, Landline, Mobile, Ext, Secretary, SecretaryID, SystemID, Password,
Team, LineManager, LineManagerID, AlternateContatName, AlternateContatID,
DateofLeavingRSAASIPL, ReasonforLeaving, LineManager2, ITAdmin, HRAdmin, TrnAdmin,
FinAdmin, Field6, Field7
) VALUES
-- Employee 41
('C041', 'ethanwa', 'Ethan Walker', '2023-03-10', '2023-04-01', 'Analyst', 'Active', 'Level 1', 'Intern',
'ethanwa@rsadummy.com', 'ethanwalker@internal.com', '1234567821', '9876543250', '141', 'Olivia Clark',
'C040', 'SYS041', 'pass', 'Pricing', 'isabelmi', 'C039', 'Charlotte Hall', 'C042', NULL, NULL,
'oliviac', 'C040', NULL, NULL, NULL, NULL, NULL),

-- Employee 42
('C042', 'charloha', 'Charlotte Hall', '2022-01-20', '2022-02-01', 'Consultant', 'Active', 'Level 2', 'Consultant',
'charloha@rsadummy.com', 'charlottehall@internal.com', '1234567822', '9876543251', '142', 'Ethan Walker',
'C041', 'SYS042', 'pass', 'Analytics', 'oliviac', 'C040', 'Ethan Walker', 'C041', NULL, NULL,
'isabelmi', 'C039', NULL, NULL, NULL, NULL, NULL),

-- Employee 43
('C043', 'masonlo', 'Mason Lopez', '2021-07-15', '2021-08-01', 'Senior Analyst', 'Active', 'Level 3', 'Sr Consultant',
'masonlo@rsadummy.com', 'masonlopez@internal.com', '1234567823', '9876543252', '143', 'Charlotte Hall',
'C042', 'SYS043', 'pass', 'Capital', 'charloha', 'C042', 'Ethan Walker', 'C041', NULL, NULL,
'oliviac', 'C040', NULL, NULL, NULL, NULL, NULL),

-- Employee 44
('C044', 'avawil', 'Ava Williams', '2020-11-01', '2020-12-01', 'Manager', 'Active', 'Level 4', 'Manager',
'avawil@rsadummy.com', 'avawilliams@internal.com', '1234567824', '9876543253', '144', 'Mason Lopez',
'C043', 'SYS044', 'pass', 'Reserving', 'masonlo', 'C043', 'Charlotte Hall', 'C042', NULL, NULL,
'charloha', 'C042', NULL, NULL, NULL, NULL, NULL),

-- Employee 45
('C045', 'emmajo', 'Emma Johnson', '2019-08-10', '2019-09-01', 'Consultant', 'Active', 'Level 2', 'Consultant',
'emmajo@rsadummy.com', 'emmajohnson@internal.com', '1234567825', '9876543254', '145', 'Ava Williams',
'C044', 'SYS045', 'pass', 'HR', 'avawil', 'C044', 'Mason Lopez', 'C043', NULL, NULL,
'masonlo', 'C043', NULL, NULL, NULL, NULL, NULL),

-- Employee 46
('C046', 'noahda', 'Noah Davis', '2021-05-20', '2021-06-01', 'Analyst', 'Active', 'Level 1', 'Intern',
'noahda@rsadummy.com', 'noahdavis@internal.com', '1234567826', '9876543255', '146', 'Emma Johnson',
'C045', 'SYS046', 'pass', 'IT', 'emmajo', 'C045', 'Emma Johnson', 'C045', NULL, NULL,
'avawil', 'C044', NULL, NULL, NULL, NULL, NULL),

-- Employee 47
('C047', 'miaev', 'Mia Evans', '2020-06-15', '2020-07-01', 'Senior Manager', 'Active', 'Level 5', 'Sr Consultant',
'miaev@rsadummy.com', 'miaevans@internal.com', '1234567827', '9876543256', '147', 'Noah Davis',
'C046', 'SYS047', 'pass', 'CIO-UK', 'avawil', 'C044', 'Noah Davis', 'C046', NULL, NULL,
'emmajo', 'C045', NULL, NULL, NULL, NULL, NULL),

-- Employee 48
('C048', 'sophiamo', 'Sophia Moore', '2021-09-25', '2021-10-01', 'IT Admin', 'Active', 'Level 2', 'Analyst',
'sophiamo@rsadummy.com', 'sophiamoore@internal.com', '1234567828', '9876543257', '148', 'Mia Evans',
'C047', 'SYS048', 'pass', 'Analytics', 'emmajo', 'C045', 'Mia Evans', 'C047', NULL, NULL,
'noahda', 'C046', NULL, NULL, NULL, NULL, NULL),

-- Employee 49
('C049', 'jamesbr', 'James Brown', '2020-03-10', '2020-04-01', 'Finance Lead', 'Active', 'Level 6', 'Head',
'jamesbr@rsadummy.com', 'jamesbrown@internal.com', '1234567829', '9876543258', '149', 'Sophia Moore',
'C048', 'SYS049', 'pass', 'Finance', 'sophiamo', 'C048', 'Sophia Moore', 'C048', NULL, NULL,
'miaev', 'C047', NULL, NULL, NULL, NULL, NULL),

-- Employee 50
('C050', 'ameliaan', 'Amelia Anderson', '2019-04-15', '2019-05-01', 'Director', 'Active', 'Level 6', 'Head',
'ameliaan@rsadummy.com', 'ameliaanderson@internal.com', '1234567830', '9876543259', '150', 'James Brown',
'C049', 'SYS050', 'pass', 'Reserving', 'jamesbr', 'C049', 'James Brown', 'C049', NULL, NULL,
'sophiamo', 'C048', NULL, NULL, NULL, NULL, NULL);

-- Insert additional dummy data into EMPWD table
INSERT INTO EMPWD (
EMPID, username, EName, DOJRS, DOJSIPL, Profile, Status, SIPLLevel, RSALevel,
EEMail, IEMail, Landline, Mobile, Ext, Secretary, SecretaryID, SystemID, Password,
Team, LineManager, LineManagerID, AlternateContatName, AlternateContatID,
DateofLeavingRSAASIPL, ReasonforLeaving, LineManager2, ITAdmin, HRAdmin, TrnAdmin,
FinAdmin, Field6, Field7
) VALUES
-- Employee 51
('C051', 'logansm', 'Logan Smith', '2023-02-15', '2023-03-01', 'Analyst', 'Active', 'Level 1', 'Intern',
'logansm@rsadummy.com', 'logansmith@internal.com', '1234567831', '9876543260', '151', 'Amelia Anderson',
'C050', 'SYS051', 'pass', 'Pricing', 'jamesbr', 'C049', 'Sophia Green', 'C052', NULL, NULL,
'ameliaan', 'C050', NULL, NULL, NULL, NULL, NULL),

-- Employee 52
('C052', 'sophiagr', 'Sophia Green', '2022-07-10', '2022-08-01', 'Consultant', 'Active', 'Level 2', 'Consultant',
'sophiagr@rsadummy.com', 'sophiagreen@internal.com', '1234567832', '9876543261', '152', 'Logan Smith',
'C051', 'SYS052', 'pass', 'Analytics', 'ameliaan', 'C050', 'Logan Smith', 'C051', NULL, NULL,
'jamesbr', 'C049', NULL, NULL, NULL, NULL, NULL),

-- Employee 53
('C053', 'lukemo', 'Luke Morgan', '2021-11-05', '2021-12-01', 'Senior Analyst', 'Active', 'Level 3', 'Sr Consultant',
'lukemo@rsadummy.com', 'lukemorgan@internal.com', '1234567833', '9876543262', '153', 'Sophia Green',
'C052', 'SYS053', 'pass', 'Capital', 'sophiagr', 'C052', 'Logan Smith', 'C051', NULL, NULL,
'ameliaan', 'C050', NULL, NULL, NULL, NULL, NULL),

-- Employee 54
('C054', 'gracewi', 'Grace Wilson', '2020-12-20', '2021-01-01', 'Manager', 'Active', 'Level 4', 'Manager',
'gracewi@rsadummy.com', 'gracewilson@internal.com', '1234567834', '9876543263', '154', 'Luke Morgan',
'C053', 'SYS054', 'pass', 'Reserving', 'lukemo', 'C053', 'Sophia Green', 'C052', NULL, NULL,
'sophiagr', 'C052', NULL, NULL, NULL, NULL, NULL),

-- Employee 55
('C055', 'liamev', 'Liam Evans', '2019-06-25', '2019-07-01', 'Consultant', 'Active', 'Level 2', 'Consultant',
'liamev@rsadummy.com', 'liamevans@internal.com', '1234567835', '9876543264', '155', 'Grace Wilson',
'C054', 'SYS055', 'pass', 'HR', 'gracewi', 'C054', 'Luke Morgan', 'C053', NULL, NULL,
'lukemo', 'C053', NULL, NULL, NULL, NULL, NULL),

-- Employee 56
('C056', 'olivercl', 'Oliver Clark', '2021-04-15', '2021-05-01', 'Analyst', 'Active', 'Level 1', 'Intern',
'olivercl@rsadummy.com', 'oliverclark@internal.com', '1234567836', '9876543265', '156', 'Liam Evans',
'C055', 'SYS056', 'pass', 'IT', 'liamev', 'C055', 'Liam Evans', 'C055', NULL, NULL,
'gracewi', 'C054', NULL, NULL, NULL, NULL, NULL),

-- Employee 57
('C057', 'ellaad', 'Ella Adams', '2020-09-01', '2020-10-01', 'Senior Manager', 'Active', 'Level 5', 'Sr Consultant',
'ellaad@rsadummy.com', 'ellaadams@internal.com', '1234567837', '9876543266', '157', 'Oliver Clark',
'C056', 'SYS057', 'pass', 'CIO-UK', 'gracewi', 'C054', 'Oliver Clark', 'C056', NULL, NULL,
'liamev', 'C055', NULL, NULL, NULL, NULL, NULL),

-- Employee 58
('C058', 'michaehu', 'Michael Hunt', '2021-08-10', '2021-09-01', 'IT Admin', 'Active', 'Level 2', 'Analyst',
'michaehu@rsadummy.com', 'michaelhunt@internal.com', '1234567838', '9876543267', '158', 'Ella Adams',
'C057', 'SYS058', 'pass', 'Analytics', 'liamev', 'C055', 'Ella Adams', 'C057', NULL, NULL,
'olivercl', 'C056', NULL, NULL, NULL, NULL, NULL),

-- Employee 59
('C059', 'isabello', 'Isabella Lopez', '2020-05-15', '2020-06-01', 'Finance Lead', 'Active', 'Level 6', 'Head',
'isabello@rsadummy.com', 'isabellalopez@internal.com', '1234567839', '9876543268', '159', 'Michael Hunt',
'C058', 'SYS059', 'pass', 'Finance', 'michaehu', 'C058', 'Michael Hunt', 'C058', NULL, NULL,
'ellaad', 'C057', NULL, NULL, NULL, NULL, NULL),

-- Employee 60
('C060', 'chloewa', 'Chloe Ward', '2019-03-20', '2019-04-01', 'Director', 'Active', 'Level 6', 'Head',
'chloewa@rsadummy.com', 'chloeward@internal.com', '1234567840', '9876543269', '160', 'Isabella Lopez',
'C059', 'SYS060', 'pass', 'Reserving', 'isabello', 'C059', 'Isabella Lopez', 'C059', NULL, NULL,
'michaehu', 'C058', NULL, NULL, NULL, NULL, NULL);

-- Insert additional dummy data into EMPWD table
INSERT INTO EMPWD (
EMPID, username, EName, DOJRS, DOJSIPL, Profile, Status, SIPLLevel, RSALevel,
EEMail, IEMail, Landline, Mobile, Ext, Secretary, SecretaryID, SystemID, Password,
Team, LineManager, LineManagerID, AlternateContatName, AlternateContatID,
DateofLeavingRSAASIPL, ReasonforLeaving, LineManager2, ITAdmin, HRAdmin, TrnAdmin,
FinAdmin, Field6, Field7
) VALUES
-- Employee 61
('C061', 'harryta', 'Harry Taylor', '2023-06-15', '2023-07-01', 'Analyst', 'Active', 'Level 1', 'Intern',
'harryta@rsadummy.com', 'harrytaylor@internal.com', '1234567841', '9876543270', '161', 'Chloe Ward',
'C060', 'SYS061', 'pass', 'Pricing', 'isabello', 'C059', 'Sophia Davis', 'C062', NULL, NULL,
'chloewa', 'C060', NULL, NULL, NULL, NULL, NULL),

-- Employee 62
('C062', 'sophiada', 'Sophia Davis', '2022-04-10', '2022-05-01', 'Consultant', 'Active', 'Level 2', 'Consultant',
'sophiada@rsadummy.com', 'sophiadavis@internal.com', '1234567842', '9876543271', '162', 'Harry Taylor',
'C061', 'SYS062', 'pass', 'Analytics', 'chloewa', 'C060', 'Harry Taylor', 'C061', NULL, NULL,
'isabello', 'C059', NULL, NULL, NULL, NULL, NULL),

-- Employee 63
('C063', 'thomasev', 'Thomas Evans', '2021-09-25', '2021-10-01', 'Senior Analyst', 'Active', 'Level 3', 'Sr Consultant',
'thomasev@rsadummy.com', 'thomasevans@internal.com', '1234567843', '9876543272', '163', 'Sophia Davis',
'C062', 'SYS063', 'pass', 'Capital', 'sophiada', 'C062', 'Harry Taylor', 'C061', NULL, NULL,
'chloewa', 'C060', NULL, NULL, NULL, NULL, NULL),

-- Employee 64
('C064', 'emilymo', 'Emily Moore', '2020-12-01', '2021-01-01', 'Manager', 'Active', 'Level 4', 'Manager',
'emilymo@rsadummy.com', 'emilymoore@internal.com', '1234567844', '9876543273', '164', 'Thomas Evans',
'C063', 'SYS064', 'pass', 'Reserving', 'thomasev', 'C063', 'Sophia Davis', 'C062', NULL, NULL,
'sophiada', 'C062', NULL, NULL, NULL, NULL, NULL),

-- Employee 65
('C065', 'jameswi', 'James Wilson', '2019-07-15', '2019-08-01', 'Consultant', 'Active', 'Level 2', 'Consultant',
'jameswi@rsadummy.com', 'jameswilson@internal.com', '1234567845', '9876543274', '165', 'Emily Moore',
'C064', 'SYS065', 'pass', 'HR', 'emilymo', 'C064', 'Thomas Evans', 'C063', NULL, NULL,
'thomasev', 'C063', NULL, NULL, NULL, NULL, NULL),

-- Employee 66
('C066', 'lilyad', 'Lily Adams', '2021-03-20', '2021-04-01', 'Analyst', 'Active', 'Level 1', 'Intern',
'lilyad@rsadummy.com', 'lilyadams@internal.com', '1234567846', '9876543275', '166', 'James Wilson',
'C065', 'SYS066', 'pass', 'IT', 'jameswi', 'C065', 'James Wilson', 'C065', NULL, NULL,
'emilymo', 'C064', NULL, NULL, NULL, NULL, NULL),

-- Employee 67
('C067', 'oscarbr', 'Oscar Brown', '2020-10-15', '2020-11-01', 'Senior Manager', 'Active', 'Level 5', 'Sr Consultant',
'oscarbr@rsadummy.com', 'oscarbrown@internal.com', '1234567847', '9876543276', '167', 'Lily Adams',
'C066', 'SYS067', 'pass', 'CIO-UK', 'emilymo', 'C064', 'Lily Adams', 'C066', NULL, NULL,
'jameswi', 'C065', NULL, NULL, NULL, NULL, NULL),

-- Employee 68
('C068', 'lucasjo', 'Lucas Johnson', '2021-06-20', '2021-07-01', 'IT Admin', 'Active', 'Level 2', 'Analyst',
'lucasjo@rsadummy.com', 'lucasjohnson@internal.com', '1234567848', '9876543277', '168', 'Oscar Brown',
'C067', 'SYS068', 'pass', 'Analytics', 'jameswi', 'C065', 'Oscar Brown', 'C067', NULL, NULL,
'lilyad', 'C066', NULL, NULL, NULL, NULL, NULL),

-- Employee 69
('C069', 'oliviamo', 'Olivia Morgan', '2020-04-10', '2020-05-01', 'Finance Lead', 'Active', 'Level 6', 'Head',
'oliviamo@rsadummy.com', 'oliviamorgan@internal.com', '1234567849', '9876543278', '169', 'Lucas Johnson',
'C068', 'SYS069', 'pass', 'Finance', 'lucasjo', 'C068', 'Lucas Johnson', 'C068', NULL, NULL,
'oscarbr', 'C067', NULL, NULL, NULL, NULL, NULL),

-- Employee 70
('C070', 'chrisda', 'Chris Davis', '2019-02-15', '2019-03-01', 'Director', 'Active', 'Level 6', 'Head',
'chrisda@rsadummy.com', 'chrisdavis@internal.com', '1234567850', '9876543279', '170', 'Olivia Morgan',
'C069', 'SYS070', 'pass', 'Reserving', 'oliviamo', 'C069', 'Olivia Morgan', 'C069', NULL, NULL,
'lucasjo', 'C068', NULL, NULL, NULL, NULL, NULL);

-- Insert additional dummy data into EMPWD table
INSERT INTO EMPWD (
EMPID, username, EName, DOJRS, DOJSIPL, Profile, Status, SIPLLevel, RSALevel,
EEMail, IEMail, Landline, Mobile, Ext, Secretary, SecretaryID, SystemID, Password,
Team, LineManager, LineManagerID, AlternateContatName, AlternateContatID,
DateofLeavingRSAASIPL, ReasonforLeaving, LineManager2, ITAdmin, HRAdmin, TrnAdmin,
FinAdmin, Field6, Field7
) VALUES
-- Employee 71
('C071', 'ethansm', 'Ethan Smith', '2022-08-15', '2022-09-01', 'Analyst', 'Active', 'Level 1', 'Intern',
'ethansm@rsadummy.com', 'ethansmith@internal.com', '1234567851', '9876543280', '171', 'Chris Davis',
'C070', 'SYS071', 'pass', 'Pricing', 'oliviamo', 'C069', 'Sophia Green', 'C072', NULL, NULL,
'chrisda', 'C070', NULL, NULL, NULL, NULL, NULL),

-- Employee 72
('C072', 'sophiabu', 'Sophia Butler', '2021-11-10', '2021-12-01', 'Consultant', 'Active', 'Level 2', 'Consultant',
'sophiabu@rsadummy.com', 'sophiabutler@internal.com', '1234567852', '9876543281', '172', 'Ethan Smith',
'C071', 'SYS072', 'pass', 'Analytics', 'chrisda', 'C070', 'Ethan Smith', 'C071', NULL, NULL,
'oliviamo', 'C069', NULL, NULL, NULL, NULL, NULL),

-- Employee 73
('C073', 'liamjo', 'Liam Johnson', '2020-06-25', '2020-07-01', 'Senior Analyst', 'Active', 'Level 3', 'Sr Consultant',
'liamjo@rsadummy.com', 'liamjohnson@internal.com', '1234567853', '9876543282', '173', 'Sophia Butler',
'C072', 'SYS073', 'pass', 'Capital', 'sophiabu', 'C072', 'Ethan Smith', 'C071', NULL, NULL,
'chrisda', 'C070', NULL, NULL, NULL, NULL, NULL),

-- Employee 74
('C074', 'emmadav', 'Emma Davis', '2021-01-05', '2021-02-01', 'Manager', 'Active', 'Level 4', 'Manager',
'emmadav@rsadummy.com', 'emmadavis@internal.com', '1234567854', '9876543283', '174', 'Liam Johnson',
'C073', 'SYS074', 'pass', 'Reserving', 'liamjo', 'C073', 'Sophia Butler', 'C072', NULL, NULL,
'sophiabu', 'C072', NULL, NULL, NULL, NULL, NULL),

-- Employee 75
('C075', 'jackcla', 'Jack Clark', '2019-03-15', '2019-04-01', 'Consultant', 'Active', 'Level 2', 'Consultant',
'jackcla@rsadummy.com', 'jackclark@internal.com', '1234567855', '9876543284', '175', 'Emma Davis',
'C074', 'SYS075', 'pass', 'HR', 'emmadav', 'C074', 'Liam Johnson', 'C073', NULL, NULL,
'liamjo', 'C073', NULL, NULL, NULL, NULL, NULL),

-- Employee 76
('C076', 'lucyro', 'Lucy Robinson', '2020-09-20', '2020-10-01', 'Analyst', 'Active', 'Level 1', 'Intern',
'lucyro@rsadummy.com', 'lucyrobinson@internal.com', '1234567856', '9876543285', '176', 'Jack Clark',
'C075', 'SYS076', 'pass', 'IT', 'jackcla', 'C075', 'Jack Clark', 'C075', NULL, NULL,
'emmadav', 'C074', NULL, NULL, NULL, NULL, NULL),

-- Employee 77
('C077', 'henrywi', 'Henry Wilson', '2021-03-15', '2021-04-01', 'Senior Manager', 'Active', 'Level 5', 'Sr Consultant',
'henrywi@rsadummy.com', 'henrywilson@internal.com', '1234567857', '9876543286', '177', 'Lucy Robinson',
'C076', 'SYS077', 'pass', 'CIO-UK', 'emmadav', 'C074', 'Lucy Robinson', 'C076', NULL, NULL,
'jackcla', 'C075', NULL, NULL, NULL, NULL, NULL),

-- Employee 78
('C078', 'evama', 'Eva Martin', '2021-08-05', '2021-09-01', 'IT Admin', 'Active', 'Level 2', 'Analyst',
'evama@rsadummy.com', 'evamartin@internal.com', '1234567858', '9876543287', '178', 'Henry Wilson',
'C077', 'SYS078', 'pass', 'Analytics', 'jackcla', 'C075', 'Henry Wilson', 'C077', NULL, NULL,
'lucyro', 'C076', NULL, NULL, NULL, NULL, NULL),

-- Employee 79
('C079', 'miajo', 'Mia Johnson', '2020-05-10', '2020-06-01', 'Finance Lead', 'Active', 'Level 6', 'Head',
'miajo@rsadummy.com', 'miajohnson@internal.com', '1234567859', '9876543288', '179', 'Eva Martin',
'C078', 'SYS079', 'pass', 'Finance', 'evama', 'C078', 'Eva Martin', 'C078', NULL, NULL,
'henrywi', 'C077', NULL, NULL, NULL, NULL, NULL),

-- Employee 80
('C080', 'oliviaru', 'Olivia Russell', '2019-07-20', '2019-08-01', 'Director', 'Active', 'Level 6', 'Head',
'oliviaru@rsadummy.com', 'oliviarussell@internal.com', '1234567860', '9876543289', '180', 'Mia Johnson',
'C079', 'SYS080', 'pass', 'Reserving', 'miajo', 'C079', 'Mia Johnson', 'C079', NULL, NULL,
'evama', 'C078', NULL, NULL, NULL, NULL, NULL);

-- Insert additional dummy data into EMPWD table
INSERT INTO EMPWD (
EMPID, username, EName, DOJRS, DOJSIPL, Profile, Status, SIPLLevel, RSALevel,
EEMail, IEMail, Landline, Mobile, Ext, Secretary, SecretaryID, SystemID, Password,
Team, LineManager, LineManagerID, AlternateContatName, AlternateContatID,
DateofLeavingRSAASIPL, ReasonforLeaving, LineManager2, ITAdmin, HRAdmin, TrnAdmin,
FinAdmin, Field6, Field7
) VALUES
-- Employee 81
('C081', 'lukemo', 'Luke Morris', '2023-02-10', '2023-03-01', 'Analyst', 'Active', 'Level 1', 'Intern',
'lukemo@rsadummy.com', 'lukemorris@internal.com', '1234567861', '9876543290', '181', 'Olivia Russell',
'C080', 'SYS081', 'pass', 'Pricing', 'miajo', 'C079', 'Sophia White', 'C082', NULL, NULL,
'oliviaru', 'C080', NULL, NULL, NULL, NULL, NULL),

-- Employee 82
('C082', 'sophiawh', 'Sophia White', '2022-01-15', '2022-02-01', 'Consultant', 'Active', 'Level 2', 'Consultant',
'sophiawh@rsadummy.com', 'sophiawhite@internal.com', '1234567862', '9876543291', '182', 'Luke Morris',
'C081', 'SYS082', 'pass', 'Analytics', 'oliviaru', 'C080', 'Luke Morris', 'C081', NULL, NULL,
'miajo', 'C079', NULL, NULL, NULL, NULL, NULL),

-- Employee 83
('C083', 'noahcl', 'Noah Clark', '2021-07-25', '2021-08-01', 'Senior Analyst', 'Active', 'Level 3', 'Sr Consultant',
'noahcl@rsadummy.com', 'noahclark@internal.com', '1234567863', '9876543292', '183', 'Sophia White',
'C082', 'SYS083', 'pass', 'Capital', 'sophiawh', 'C082', 'Luke Morris', 'C081', NULL, NULL,
'oliviaru', 'C080', NULL, NULL, NULL, NULL, NULL),

-- Employee 84
('C084', 'ellajon', 'Ella Jones', '2020-03-10', '2020-04-01', 'Manager', 'Active', 'Level 4', 'Manager',
'ellajon@rsadummy.com', 'ellajones@internal.com', '1234567864', '9876543293', '184', 'Noah Clark',
'C083', 'SYS084', 'pass', 'Reserving', 'noahcl', 'C083', 'Sophia White', 'C082', NULL, NULL,
'sophiawh', 'C082', NULL, NULL, NULL, NULL, NULL),

-- Employee 85
('C085', 'oliverro', 'Oliver Robinson', '2019-11-05', '2019-12-01', 'Consultant', 'Active', 'Level 2', 'Consultant',
'oliverro@rsadummy.com', 'oliverrobinson@internal.com', '1234567865', '9876543294', '185', 'Ella Jones',
'C084', 'SYS085', 'pass', 'HR', 'ellajon', 'C084', 'Noah Clark', 'C083', NULL, NULL,
'noahcl', 'C083', NULL, NULL, NULL, NULL, NULL),

-- Employee 86
('C086', 'ameliacoo', 'Amelia Cooper', '2020-06-20', '2020-07-01', 'Analyst', 'Active', 'Level 1', 'Intern',
'ameliacoo@rsadummy.com', 'ameliacooper@internal.com', '1234567866', '9876543295', '186', 'Oliver Robinson',
'C085', 'SYS086', 'pass', 'IT', 'oliverro', 'C085', 'Oliver Robinson', 'C085', NULL, NULL,
'ellajon', 'C084', NULL, NULL, NULL, NULL, NULL),

-- Employee 87
('C087', 'isaacbr', 'Isaac Brown', '2021-04-15', '2021-05-01', 'Senior Manager', 'Active', 'Level 5', 'Sr Consultant',
'isaacbr@rsadummy.com', 'isaacbrown@internal.com', '1234567867', '9876543296', '187', 'Amelia Cooper',
'C086', 'SYS087', 'pass', 'CIO-UK', 'ellajon', 'C084', 'Amelia Cooper', 'C086', NULL, NULL,
'oliverro', 'C085', NULL, NULL, NULL, NULL, NULL),

-- Employee 88
('C088', 'avalam', 'Ava Lambert', '2021-10-10', '2021-11-01', 'IT Admin', 'Active', 'Level 2', 'Analyst',
'avalam@rsadummy.com', 'avalambert@internal.com', '1234567868', '9876543297', '188', 'Isaac Brown',
'C087', 'SYS088', 'pass', 'Analytics', 'oliverro', 'C085', 'Isaac Brown', 'C087', NULL, NULL,
'ameliacoo', 'C086', NULL, NULL, NULL, NULL, NULL),

-- Employee 89
('C089', 'gracejo', 'Grace Johnson', '2020-09-01', '2020-10-01', 'Finance Lead', 'Active', 'Level 6', 'Head',
'gracejo@rsadummy.com', 'gracejohnson@internal.com', '1234567869', '9876543298', '189', 'Ava Lambert',
'C088', 'SYS089', 'pass', 'Finance', 'avalam', 'C088', 'Ava Lambert', 'C088', NULL, NULL,
'isaacbr', 'C087', NULL, NULL, NULL, NULL, NULL),

-- Employee 90
('C090', 'emilywa', 'Emily Walker', '2019-12-20', '2020-01-01', 'Director', 'Active', 'Level 6', 'Head',
'emilywa@rsadummy.com', 'emilywalker@internal.com', '1234567870', '9876543299', '190', 'Grace Johnson',
'C089', 'SYS090', 'pass', 'Reserving', 'gracejo', 'C089', 'Grace Johnson', 'C089', NULL, NULL,
'avalam', 'C088', NULL, NULL, NULL, NULL, NULL);

-- Insert additional dummy data into EMPWD table
INSERT INTO EMPWD (
EMPID, username, EName, DOJRS, DOJSIPL, Profile, Status, SIPLLevel, RSALevel,
EEMail, IEMail, Landline, Mobile, Ext, Secretary, SecretaryID, SystemID, Password,
Team, LineManager, LineManagerID, AlternateContatName, AlternateContatID,
DateofLeavingRSAASIPL, ReasonforLeaving, LineManager2, ITAdmin, HRAdmin, TrnAdmin,
FinAdmin, Field6, Field7
) VALUES
-- Employee 91
('C091', 'jamesgr', 'James Green', '2022-03-12', '2022-04-01', 'Senior Analyst', 'Active', 'Level 3', 'Sr Consultant',
'jamesgr@rsadummy.com', 'jamesgreen@internal.com', '1234567871', '9876543300', '191', 'Emily Walker',
'C090', 'SYS091', 'pass', 'Pricing', 'gracejo', 'C089', 'Emily Walker', 'C090', NULL, NULL,
'avalam', 'C088', NULL, NULL, NULL, NULL, NULL),

-- Employee 92
('C092', 'emilyjo', 'Emily Johnson', '2020-10-18', '2020-11-01', 'Consultant', 'Active', 'Level 2', 'Consultant',
'emilyjo@rsadummy.com', 'emilyjohnson@internal.com', '1234567872', '9876543301', '192', 'James Green',
'C091', 'SYS092', 'pass', 'Analytics', 'gracejo', 'C089', 'James Green', 'C091', NULL, NULL,
'jamesgr', 'C090', NULL, NULL, NULL, NULL, NULL),

-- Employee 93
('C093', 'liamfr', 'Liam Fraser', '2021-05-20', '2021-06-01', 'Manager', 'Active', 'Level 4', 'Manager',
'liamfr@rsadummy.com', 'liamfraser@internal.com', '1234567873', '9876543302', '193', 'Emily Johnson',
'C092', 'SYS093', 'pass', 'Reserving', 'emilyjo', 'C092', 'Emily Johnson', 'C092', NULL, NULL,
'jamesgr', 'C090', NULL, NULL, NULL, NULL, NULL),

-- Employee 94
('C094', 'victorba', 'Victor Barnes', '2021-09-15', '2021-10-01', 'Consultant', 'Active', 'Level 2', 'Consultant',
'victorba@rsadummy.com', 'victorbarnes@internal.com', '1234567874', '9876543303', '194', 'Liam Fraser',
'C093', 'SYS094', 'pass', 'HR', 'liamfr', 'C093', 'Liam Fraser', 'C093', NULL, NULL,
'emilyjo', 'C092', NULL, NULL, NULL, NULL, NULL),

-- Employee 95
('C095', 'hannahwi', 'Hannah Wilson', '2022-02-01', '2022-03-01', 'Senior Analyst', 'Active', 'Level 3', 'Sr Consultant',
'hannahwi@rsadummy.com', 'hannahwilson@internal.com', '1234567875', '9876543304', '195', 'Victor Barnes',
'C094', 'SYS095', 'pass', 'Capital', 'victorba', 'C094', 'Victor Barnes', 'C094', NULL, NULL,
'liamfr', 'C093', NULL, NULL, NULL, NULL, NULL),

-- Employee 96
('C096', 'danielca', 'Daniel Carter', '2020-01-30', '2020-02-01', 'Analyst', 'Active', 'Level 1', 'Intern',
'danielca@rsadummy.com', 'danielcarter@internal.com', '1234567876', '9876543305', '196', 'Hannah Wilson',
'C095', 'SYS096', 'pass', 'IT', 'victorba', 'C094', 'Hannah Wilson', 'C095', NULL, NULL,
'liamfr', 'C093', NULL, NULL, NULL, NULL, NULL),

-- Employee 97
('C097', 'jacobhv', 'Jacob Howard', '2021-06-01', '2021-07-01', 'Senior Manager', 'Active', 'Level 5', 'Sr Consultant',
'jacobhv@rsadummy.com', 'jacobhoward@internal.com', '1234567877', '9876543306', '197', 'Daniel Carter',
'C096', 'SYS097', 'pass', 'CIO-UK', 'hannahwi', 'C095', 'Daniel Carter', 'C096', NULL, NULL,
'victorba', 'C094', NULL, NULL, NULL, NULL, NULL),

-- Employee 98
('C098', 'lilysc', 'Lily Scott', '2021-12-10', '2021-12-15', 'IT Admin', 'Active', 'Level 2', 'Analyst',
'lilysc@rsadummy.com', 'lilyscott@internal.com', '1234567878', '9876543307', '198', 'Jacob Howard',
'C097', 'SYS098', 'pass', 'Analytics', 'danielca', 'C096', 'Jacob Howard', 'C097', NULL, NULL,
'hannahwi', 'C095', NULL, NULL, NULL, NULL, NULL),

-- Employee 99
('C099', 'noahbr', 'Noah Brown', '2020-07-18', '2020-08-01', 'Finance Lead', 'Active', 'Level 6', 'Head',
'noahbr@rsadummy.com', 'noahbrown@internal.com', '1234567879', '9876543308', '199', 'Lily Scott',
'C098', 'SYS099', 'pass', 'Finance', 'lilysc', 'C098', 'Lily Scott', 'C098', NULL, NULL,
'jacobhv', 'C097', NULL, NULL, NULL, NULL, NULL),

-- Employee 100
('C100', 'rebeccac', 'Rebecca Carter', '2021-02-10', '2021-03-01', 'Director', 'Active', 'Level 6', 'Head',
'rebeccac@rsadummy.com', 'rebeccacarter@internal.com', '1234567880', '9876543309', '200', 'Noah Brown',
'C099', 'SYS100', 'pass', 'Reserving', 'noahbr', 'C099', 'Noah Brown', 'C099', NULL, NULL,
'lilysc', 'C098', NULL, NULL, NULL, NULL, NULL);
