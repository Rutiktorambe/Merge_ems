# Table Schema

### **1. Table: `EMPWD`**

| **Sr. No** | **Column Name**       | **Type**    | **Constraints**  |
| ---------- | --------------------- | ----------- | ---------------- |
| 1          | EMPID                 | String(255) | Primary Key      |
| 2          | username              | String(255) | Unique, Not Null |
| 3          | EName                 | String(255) |                  |
| 4          | DOJRS                 | Date        |                  |
| 5          | DOJSIPL               | Date        | Nullable         |
| 6          | Profile               | String(255) |                  |
| 7          | Status                | String(50)  |                  |
| 8          | SIPLLevel             | String(50)  |                  |
| 9          | RSALevel              | String(50)  |                  |
| 10         | EEMail                | String(255) |                  |
| 11         | IEMail                | String(255) |                  |
| 12         | Landline              | String(20)  |                  |
| 13         | Mobile                | String(20)  |                  |
| 14         | Ext                   | String(10)  |                  |
| 15         | Secretary             | String(255) |                  |
| 16         | SecretaryID           | String(255) |                  |
| 17         | SystemID              | String(255) |                  |
| 18         | Password              | String(255) | Not Null         |
| 19         | Team                  | String(255) |                  |
| 20         | LineManager           | String(255) |                  |
| 21         | LineManagerID         | String(255) |                  |
| 22         | AlternateContatName   | String(255) |                  |
| 23         | AlternateContatID     | String(255) |                  |
| 24         | DateofLeavingRSAASIPL | Date        | Nullable         |
| 25         | ReasonforLeaving      | String(255) |                  |
| 26         | LineManager2          | String(255) |                  |
| 27         | ITAdmin               | String(255) |                  |
| 28         | HRAdmin               | String(255) |                  |
| 29         | TrnAdmin              | String(255) |                  |
| 30         | FinAdmin              | String(255) |                  |
| 31         | Field6                | String(255) |                  |
| 32         | Field7                | String(255) |                  |

---

### **2. Table: `timesheet_entries`**

| **Sr. No** | **Column Name** | **Type**    | **Constraints**              |
| ---------- | --------------- | ----------- | ---------------------------- |
| 1          | Uniq_ID         | String(255) | Primary Key                  |
| 2          | EmpID           | String(10)  | Not Null                     |
| 3          | DateofEntry     | Date        | Not Null                     |
| 4          | StartTime       | String(255) | Nullable                     |
| 5          | EndTime         | String(255) | Nullable                     |
| 6          | Hours           | Float       | Nullable                     |
| 7          | Minutes         | Float       | Nullable                     |
| 8          | AllocationType  | String(50)  | Nullable                     |
| 9          | Category1       | String(50)  | Nullable                     |
| 10         | Category2       | String(50)  | Nullable                     |
| 11         | Category3       | String(50)  | Nullable                     |
| 12         | ProjectCode     | String(10)  | Nullable                     |
| 13         | Category5       | String(50)  | Nullable                     |
| 14         | Category6       | String(50)  | Nullable                     |
| 15         | Comment         | String(255) | Nullable                     |
| 16         | Team            | String(255) | Not Null                     |
| 17         | Status          | String(20)  | Nullable                     |
| 18         | SubmitDate      | DateTime    | Default(Current Timestamp)   |
| 19         | RecordType      | String(50)  | Nullable                     |
| 20         | WO_Percent      | Float       | Nullable                     |
| 21         | WO_Units        | Integer     | Nullable                     |
| 22         | NetUnits        | Integer     | Nullable                     |
| 23         | BaseRate        | Float       | Nullable                     |
| 24         | Billed_Label    | String(50)  | Nullable                     |
| 25         | WOFF_Reason     | String(255) | Nullable                     |
| 26         | LastUploadDate  | DateTime    | On Update(Current Timestamp) |
| 27         | LastUpdatedBy   | String(50)  | Nullable                     |
| 28         | InvNum          | Float       | Nullable                     |
| 29         | FinalRate       | Float       | Nullable                     |
| 30         | SSMA_TimeStamp  | DateTime    | Nullable                     |

---

### **3. Table: `Resourceinfo`**

| **Sr. No** | **Column Name** | **Type**    | **Constraints**                  |
| ---------- | --------------- | ----------- | -------------------------------- |
| 1          | ProjectCode     | String(100) | Primary Key                      |
| 2          | SSMA_Timestamp  | TIMESTAMP   | Primary Key, Default + On Update |
| 3          | EmpID           | String(100) | Primary Key                      |
| 4          | ProjectName     | String(255) | Not Null                         |
| 5          | Team            | String(100) | Nullable                         |
| 6          | EName           | String(255) | Nullable                         |
| 7          | Skill           | String(255) | Nullable                         |
| 8          | Occupancy       | String(255) | Nullable                         |
| 9          | FromDate        | Date        | Nullable                         |
| 10         | ToDate          | Date        | Nullable                         |
| 11         | Level           | String(255) | Nullable                         |
| 12         | Allocation      | Float       | Nullable                         |
| 13         | Status          | String(50)  | Nullable                         |

---

### **4. Table: `trainings`**

| **Sr. No** | **Column Name** | **Type**    | **Constraints** |
| ---------- | --------------- | ----------- | --------------- |
| 1          | TID             | String(255) | Primary Key     |
| 2          | EmpID           | String(255) | Not Null        |
| 3          | TName           | String(255) | Not Null        |
| 4          | TCat            | String(255) | Not Null        |
| 5          | TDate           | Date        | Not Null        |
| 6          | TDuration       | Float       | Not Null        |
| 7          | TTime           | Float       | Not Null        |
| 8          | Seats           | String(255) | Not Null        |
| 9          | Relevance       | String(255) | Not Null        |
| 10         | Comment         | String(255) | Not Null        |
| 11         | TType           | String(255) | Not Null        |
| 12         | Venue           | String(255) | Not Null        |
| 13         | TPresenter      | String(255) | Not Null        |
| 14         | TTravel         | String(255) | Not Null        |
| 15         | TAcc            | String(255) | Not Null        |
| 16         | TLevel1         | String(255) | Not Null        |
| 17         | TLevel2         | String(255) | Not Null        |
| 18         | TApproval       | String(255) | Not Null        |
| 19         | SSMA_Timestamp  | DateTime    | Not Null        |

---

### **5. Table: `TrainingRegistration`**

| **Sr. No** | **Column Name** | **Type**    | **Constraints** |
| ---------- | --------------- | ----------- | --------------- |
| 1          | TID             | String(255) | Primary Key     |
| 2          | EmpID           | String(255) | Primary Key     |
| 3          | Status          | String(255) | Not Null        |

---
