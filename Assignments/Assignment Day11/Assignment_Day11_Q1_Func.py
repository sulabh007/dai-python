import sqlite3

try:
    conn=sqlite3.connect("emp.db")
    print("connection done")
except Exception as e:
    print("Error Occurred",e)
    
cursor=conn.cursor()

def create_table():
    try:
        cursor.execute('''CREATE TABLE  IF NOT EXISTS employee (empid,empname,mob,sal)''')
        conn.commit()
        print("Table Created")
    except Exception as e:
        print("Error Occurred ",e)


def addemp(empid,empname,mob,sal):
    try:
        cursor.execute("insert into employee values(?,?,?,?)",(empid,empname,mob,sal))
        conn.commit()
    except Exception as e:
        print("Error Occurred ",e)
        conn.rollback()
        
def displayempall():
    cursor.execute("select * from employee")
    for row in cursor.fetchall():
        print(f"""
        Employee ID: {row[0]} 
        Employee Name: {row[1]} 
        Mob No.: {row[2]}
        Employee Salary : {row[3]}""")
        
def delemp(empid):
    empid=int(empid)
    try:
        cursor.execute("delete from employee where empid=?",(empid))
        conn.commit()
        return 1
    except Exception as e:
        print("Error Occurred ",e)
        conn.rollback()
        return 0
    
def modemp(empid,empname,mob,sal):
    empid=int(empid)
    try:
        cursor.execute("update employee set empname=?,mob=?,sal=? where empid=?",(empname,mob,sal,empid))
        conn.commit()
        return True
    except Exception as e:
        print("Error Occurred ",e)
        conn.rollback()
        return False
    
def displybyid(empid):
    try:
        cursor.execute(f"select * from employee where empid={empid}")
        row=cursor.fetchone()
        print(f"""
        Employee ID: {row[0]} 
        Employee Name: {row[1]} 
        Mob No.: {row[2]}
        Employee Salary : {row[3]}""")
        return 1
    except Exception as e:
        print("Error Occurred",e)
        
def displaybysal(sal):
    try:
        cursor.execute(f"select * from employee where sal>{sal}")
        for row in cursor.fetchall():
            print(f"""
            Employee ID: {row[0]} 
            Employee Name: {row[1]} 
            Mob No.: {row[2]}
            Employee Salary : {row[3]}""")
        return 1
    except Exception as e:
        print("Error Occurred ",e)
        conn.rollback()
        return False