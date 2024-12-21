CREATE TABLE Trainings (
    TID VARCHAR(255) NOT NULL PRIMARY KEY,
    EmpID VARCHAR(255) NOT NULL,
    TName VARCHAR(255) NOT NULL,
    TCat VARCHAR(255) NOT NULL,
    TDate DATE NOT NULL,
    TDuration FLOAT NOT NULL,
    TTime FLOAT NOT NULL,
    Seats VARCHAR(255) NOT NULL,
    Relevance VARCHAR(255) NOT NULL,
    Comment VARCHAR(255) NOT NULL,
    TType VARCHAR(255) NOT NULL,
    Venue VARCHAR(255) NOT NULL,
    TPresenter VARCHAR(255) NOT NULL,
    TTravel VARCHAR(255) NOT NULL,
    TAcc VARCHAR(255) NOT NULL,
    TLevel1 VARCHAR(255) NOT NULL,
    TLevel2 VARCHAR(255) NOT NULL,
    TApproval VARCHAR(255) NOT NULL,
    SSMA_Timestamp DATETIME NOT NULL
);



INSERT INTO Trainings (TID, EmpID, TName, TCat, TDate, TDuration, TTime, Seats, Relevance, Comment, TType, Venue, TPresenter, TTravel, TAcc, TLevel1, TLevel2, TApproval, SSMA_Timestamp) VALUES
('T101', 'A00001', 'Python', 'Technical', '2023-01-15', 2.5, 3.0, '30', 'High', 'N/A', 'Internal', 'Room A', 'John Doe', 'No', 'N/A', 'Basic', 'Advanced', 'Yes', '2023-01-01 08:00:00'),
('T102', 'A00002', 'Power BI', 'Analytical', '2023-02-10', 3.0, 2.5, '25', 'Medium', 'N/A', 'External', 'Room B', 'Jane Smith', 'Yes', 'Hotel A', 'Intermediate', 'Advanced', 'Yes', '2023-02-01 09:00:00'),
('T103', 'A00003', 'SAS', 'Data Science', '2023-03-20', 4.0, 3.0, '20', 'High', 'Important', 'Internal', 'Room C', 'Mike Brown', 'No', 'N/A', 'Intermediate', 'Expert', 'No', '2023-03-05 10:00:00'),
('T104', 'A00004', 'R', 'Data Science', '2023-04-15', 3.5, 2.0, '35', 'High', 'Recommended', 'External', 'Room D', 'Sarah White', 'Yes', 'Hotel B', 'Basic', 'Intermediate', 'Yes', '2023-04-01 11:00:00'),
('T105', 'A00005', 'Excel', 'Analytical', '2023-05-12', 2.0, 1.5, '40', 'Low', 'Optional', 'Internal', 'Room E', 'Anna Green', 'No', 'N/A', 'Basic', 'Advanced', 'No', '2023-05-01 12:00:00'),
('T106', 'A00006', 'SQL', 'Technical', '2023-06-18', 3.0, 3.5, '28', 'Medium', 'Required', 'Internal', 'Room F', 'David Blue', 'No', 'N/A', 'Intermediate', 'Expert', 'Yes', '2023-06-01 13:00:00'),
('T107', 'A00007', 'Tableau', 'Visualization', '2023-07-22', 2.5, 2.0, '30', 'High', 'N/A', 'External', 'Room G', 'Karen Black', 'Yes', 'Hotel C', 'Basic', 'Intermediate', 'Yes', '2023-07-01 14:00:00'),
('T108', 'A00008', 'Python Advanced', 'Technical', '2023-08-30', 5.0, 4.0, '20', 'High', 'Critical', 'Internal', 'Room H', 'Chris Yellow', 'No', 'N/A', 'Advanced', 'Expert', 'Yes', '2023-08-01 15:00:00'),
('T109', 'A00009', 'Power BI Advanced', 'Analytical', '2023-09-25', 3.5, 3.0, '18', 'High', 'Key Skill', 'External', 'Room I', 'Emily Pink', 'Yes', 'Hotel D', 'Intermediate', 'Expert', 'Yes', '2023-09-01 16:00:00'),
('T110', 'A00010', 'R Advanced', 'Data Science', '2023-10-15', 4.5, 3.5, '22', 'High', 'Specialized', 'Internal', 'Room J', 'Liam Violet', 'No', 'N/A', 'Advanced', 'Expert', 'No', '2023-10-01 17:00:00');
