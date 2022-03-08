import sqlite3

connection = sqlite3.connect("company.db")

#connection.execute('''  CREATE TABLE EMPLOYEE(
#                 EMPLOYEECODE INTEGER PRIMARY KEY AUTOINCREMENT,
#                 EMPLOYEENAME TEXT,
#                 DESIGNATION TEXT,
#                 SALARY INTEGER,
#                 COMPANYNAME TEXT,
#                 MOBILENO INTEGER
# );    ''')


print("TABLE CREATED SUCCESFULLY")

getEmployeeCode = input("Enter EmployeeCode : ")
getEmployeeName = input("Enter EmployeeName : ")
getDesignation = input("Enter Designation : ")
getSalary = input("Enter Salary : ")
getCompanyName = input("Enter CompanyName : ")
getMobileNo = input("Enter MobileNo : ")
connection.execute("INSERT INTO EMPLOYEE(EMPLOYEECODE,EMPLOYEENAME,DESIGNATION,SALARY,COMPANYNAME,MOBILENO) \
 VALUES("+getEmployeeCode+",'"+getEmployeeName+"','"+getDesignation+"',"+getSalary+",'"+getCompanyName+"',"+getMobileNo+")")
connection.commit()
connection.close()
print("DATA BASE INSERTED SUCCESFULLY")

