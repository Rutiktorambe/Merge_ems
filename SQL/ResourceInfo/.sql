CREATE TABLE ResourceInfo (
    ProjectCode VARCHAR(100) NOT NULL,
    SSMA_Timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    EmpID VARCHAR(100) NOT NULL,
    ProjectName VARCHAR(255) NOT NULL,
    Team VARCHAR(100),
    EName VARCHAR(255),
    Skill VARCHAR(255),
    Occupancy VARCHAR(255),
    FromDate DATE,
    ToDate DATE,
    Level VARCHAR(255),
    Allocation FLOAT,
    Status VARCHAR(50),
    PRIMARY KEY (ProjectCode, SSMA_Timestamp, EmpID)
);



INSERT INTO ResourceInfo (
    ProjectCode, 
    SSMA_Timestamp, 
    EmpID, 
    ProjectName, 
    Team, 
    EName, 
    Skill, 
    Occupancy, 
    FromDate, 
    ToDate, 
    Level, 
    Allocation, 
    Status
)
VALUES
('P001', '2024-12-01 13:07:22', 'A00001', 'Project Alpha', 'Pricing', 'Alice Johnson', 'Python', 'Full-Time', '2023-11-01', '2025-10-01', 'Senior', 100.0, 'Active'),
('P002', '2024-12-01 13:07:22', 'A00001', 'Project Beta', 'Capital', 'Alice Johnson', 'SQL', 'Part-Time', '2024-01-15', '2025-11-30', 'Senior', 50.0, 'Active'),
('P003', '2024-12-01 13:07:22', 'A00002', 'Project Gamma', 'Analytics', 'Bob Smith', 'Machine Learning', 'Full-Time', '2023-12-10', '2025-12-31', 'Intermediate', 100.0, 'Active'),
('P001', '2024-12-01 13:07:22', 'A00002', 'Project Alpha', 'Pricing', 'Bob Smith', 'Python', 'Part-Time', '2024-03-01', '2025-09-30', 'Intermediate', 50.0, 'Active'),
('P004', '2024-12-01 13:07:22', 'A00003', 'Project Delta', 'Reserving', 'Charlie Lee', 'R', 'Full-Time', '2023-10-01', '2025-10-15', 'Junior', 100.0, 'Active'),
('P005', '2024-12-01 13:07:22', 'A00004', 'Project Epsilon', 'CIO-UK', 'Diana Evans', 'Java', 'Full-Time', '2023-11-01', '2025-10-30', 'Senior', 100.0, 'Active'),
('P002', '2024-12-01 13:07:22', 'A00005', 'Project Beta', 'Capital', 'Eve Davis', 'SQL', 'Full-Time', '2024-02-01', '2025-11-15', 'Intermediate', 100.0, 'Active'),
('P003', '2024-12-01 13:07:22', 'A00006', 'Project Gamma', 'Analytics', 'Frank Moore', 'Machine Learning', 'Part-Time', '2024-05-15', '2025-12-31', 'Junior', 50.0, 'Active'),
('P006', '2024-12-01 13:07:22', 'A00007', 'Project Zeta', 'HR', 'Grace Adams', 'HR Analytics', 'Full-Time', '2023-09-15', '2025-10-01', 'Intermediate', 100.0, 'Active'),
('P001', '2024-12-01 13:07:22', 'A00008', 'Project Alpha', 'Pricing', 'Henry Brown', 'Python', 'Part-Time', '2024-03-10', '2025-09-30', 'Junior', 50.0, 'Active'),
('P002', '2024-12-01 13:07:33', 'A00003', 'Project Beta', 'Capital', 'Charlie Lee', 'R', 'Part-Time', '2024-01-10', '2025-11-20', 'Intermediate', 50.0, 'Active'),
('P007', '2024-12-01 13:07:33', 'A00004', 'Project Eta', 'Analytics', 'Diana Evans', 'Data Analysis', 'Full-Time', '2023-12-01', '2025-12-15', 'Senior', 100.0, 'Active'),
('P003', '2024-12-01 13:07:33', 'A00005', 'Project Gamma', 'Analytics', 'Eve Davis', 'Python', 'Part-Time', '2024-02-20', '2025-12-31', 'Intermediate', 50.0, 'Active'),
('P008', '2024-12-01 13:07:33', 'A00006', 'Project Theta', 'Reserving', 'Frank Moore', 'Statistics', 'Full-Time', '2023-09-01', '2025-10-05', 'Junior', 100.0, 'Active'),
('P004', '2024-12-01 13:07:33', 'A00007', 'Project Delta', 'Reserving', 'Grace Adams', 'R', 'Part-Time', '2024-03-15', '2025-11-01', 'Intermediate', 50.0, 'Active'),
('P009', '2024-12-01 13:07:33', 'A00008', 'Project Iota', 'HR', 'Henry Brown', 'HR Systems', 'Full-Time', '2023-11-15', '2025-10-30', 'Junior', 100.0, 'Active'),
('P005', '2024-12-01 13:07:33', 'A00009', 'Project Epsilon', 'CIO-UK', 'Irene White', 'JavaScript', 'Part-Time', '2024-01-25', '2025-09-15', 'Intermediate', 50.0, 'Active'),
('P006', '2024-12-01 13:07:33', 'A00010', 'Project Zeta', 'HR', 'Jack Black', 'HR Analytics', 'Full-Time', '2024-02-10', '2025-11-10', 'Senior', 100.0, 'Active'),
('P007', '2024-12-01 13:07:33', 'A00001', 'Project Eta', 'Analytics', 'Alice Johnson', 'Data Analysis', 'Full-Time', '2023-10-01', '2025-10-20', 'Senior', 100.0, 'Active'),
('P001', '2024-12-01 13:07:33', 'A00009', 'Project Alpha', 'Pricing', 'Irene White', 'Python', 'Part-Time', '2024-04-15', '2025-09-30', 'Junior', 50.0, 'Active');
