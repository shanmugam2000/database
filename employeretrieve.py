import  sqlite3
connection = sqlite3.connect("company.db")

result = connection.execute("select * from EMPLOYEE")

for i in result:
    print("EMPLOYEECODE",i[1])
    print("EMPLOYEENAME",i[2])
    print("COMPANYNAME ",i[3])
    print("SALARY ",i[4])
