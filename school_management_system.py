print("____school managemnet system____")

import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="1234")
mycursor = mydb.cursor()
mycursor.execute("create database if not exists pyschool")
mycursor.execute("use pyschool")
mycursor.execute("create table if not exists pystudent(name varchar(50) not null,classs varchar(25) not null,roll_no varchar(25),gender char(1))")
mycursor.execute("create table if not exists pystaff(name varchar(50) not null,gender char(1),subject varchar(25) not null,Salary varchar(25))")
mydb.commit()
while(True):
    print("1=enetr data for new student")
    print("2=enter data for new staff")
    print("3.search student data")
    print("4.search staff data")
    print("remove student data ")
    print("6.remove staff data")
    print("7.exit")
    ch=int(input("eneter your choice:"))
    if ch==1:
        name=input("enetr the name(limit 35 characrtwes):")
        student_class=input("enter the class:")
        roll_no=input("rollno:")
        gender=input("gender:")
        mycursor.execute("insert into pystudent values(%s,%s,%s,%s)",(name,student_class,roll_no,gender))
        mydb.commit()
        print("data inserted successfully")
    elif ch==2:
        sname=input("enter the staff name(limit 35 characters):")
        gender=input("enter gender:")
        dep=input("enter the subject:")
        sal=int(input("slalary:"))
        mycursor.execute("insert into pystaff values("sname","gender","dep","str(sal)")")
        mydb.commit()
        print("data inserted succeddfully")
    elif ch==3:
        roll_no=input("roll no:")
        mycursor.execute("select * from pystudent where roll_no="roll_no"")
        for i in mycursor:
            name,classs,roll_no,gender = i
            print(f"Name: {name}")
            print(f"class: {classs}")
            print(f"roll_no: {roll_no}")
            print(f"gender: {gender}")
    elif ch==4:
        name=input("name:")
        mycursor.execute("select * from pystaff where name="name"")
        for i in mycursor:
            name,gender,dep,sal = i
            print(f"name {name}")
            print(f"gender: {gender}")
            print(f"department: {dep}")
            print(f"sal: {sal}")
    elif ch==5:
        r_no=input("roll no;")
        mycursor.execute("delete from pystudent where roll_no=" + r_no + "")
        mydb.commit()
        print("data removed successfully")
    elif ch==6:
        name=input("enter the name:")
        mycursor.execute("delete from pystaff where name=" + name + "")            
        mybd.commit()
        print("data removed successfully")
    else:
        break              

        