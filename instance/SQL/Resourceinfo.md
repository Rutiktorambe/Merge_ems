CREATE TABLE Resourceinfo (
ProjectCode VARCHAR(100),
ProjectName VARCHAR(255) NOT NULL,
Team VARCHAR(100),
EmpID VARCHAR(100),
EName VARCHAR(255),
Skill VARCHAR(255),
Occupancy VARCHAR(255),
FromDate DATE,
ToDate DATE,
Level VARCHAR(255),
Allocation FLOAT,
Status VARCHAR(50),
SSMA_Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (EmpID, SSMA_Timestamp)
);

INSERT INTO Resourceinfo (ProjectCode, ProjectName, Team, EmpID, EName, Skill, Occupancy, FromDate, ToDate, Level, Allocation, Status, SSMA_Timestamp)
VALUES
('P001', 'Project Alpha', 'Pricing', 'C001', 'Alice Johnson', 'Python', 'Full-Time', '2023-11-01', '2025-10-01', 'Senior', 100.0, 'Active', CURRENT_TIMESTAMP),
('P002', 'Project Beta', 'Capital', 'C001', 'Alice Johnson', 'SQL', 'Part-Time', '2024-01-15', '2025-11-30', 'Senior', 50.0, 'Active', CURRENT_TIMESTAMP),
('P003', 'Project Gamma', 'Analytics', 'C002', 'Bob Smith', 'Machine Learning', 'Full-Time', '2023-12-10', '2025-12-31', 'Intermediate', 100.0, 'Active', CURRENT_TIMESTAMP),
('P001', 'Project Alpha', 'Pricing', 'C002', 'Bob Smith', 'Python', 'Part-Time', '2024-03-01', '2025-09-30', 'Intermediate', 50.0, 'Active', CURRENT_TIMESTAMP),
('P004', 'Project Delta', 'Reserving', 'C003', 'Charlie Lee', 'R', 'Full-Time', '2023-10-01', '2025-10-15', 'Junior', 100.0, 'Active', CURRENT_TIMESTAMP),
('P005', 'Project Epsilon', 'CIO-UK', 'C004', 'Diana Evans', 'Java', 'Full-Time', '2023-11-01', '2025-10-30', 'Senior', 100.0, 'Active', CURRENT_TIMESTAMP),
('P002', 'Project Beta', 'Capital', 'C005', 'Eve Davis', 'SQL', 'Full-Time', '2024-02-01', '2025-11-15', 'Intermediate', 100.0, 'Active', CURRENT_TIMESTAMP),
('P003', 'Project Gamma', 'Analytics', 'C006', 'Frank Moore', 'Machine Learning', 'Part-Time', '2024-05-15', '2025-12-31', 'Junior', 50.0, 'Active', CURRENT_TIMESTAMP),
('P006', 'Project Zeta', 'HR', 'C007', 'Grace Adams', 'HR Analytics', 'Full-Time', '2023-09-15', '2025-10-01', 'Intermediate', 100.0, 'Active', CURRENT_TIMESTAMP),
('P001', 'Project Alpha', 'Pricing', 'C008', 'Henry Brown', 'Python', 'Part-Time', '2024-03-10', '2025-09-30', 'Junior', 50.0, 'Active', CURRENT_TIMESTAMP);
