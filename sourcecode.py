import mysql.connector as mcon
import sys
con = mcon.connect (host="localhost" ,port="3306" ,user="root"  ,passwd="root")
mycursor = con.cursor()
if con.is_connected():
print("MySql DataBase is connected Successfully.")
         mycursor.execute("create database if not exists LOC")
         mycursor.execute("use LOC")
         mycursor.execute("create table if not exists user \                (uname varchar(20) primary key,upwd varchar(20)\
,utype char(5),ustatus char(5))")
        Q = "insert into user(uname,upwd,utype) values (\'LOC\',\'LOC\',\'S\')"
        #print(Q)
        #mycursor.execute(Q)
        con.commit()
        at = 1	
        while at <= 3:
                at += 1
                uid = input("Enter User Name : ")
                pwd = input("Enter User Password : ")
                status = 'A'
                mycursor.execute("select * from user where uname = '{}' and upwd = '{}' and ustatus = '{}'".format(uid,pwd,status))
                data = mycursor.fetchone()
                count = mycursor.rowcount
                #print(count)    
                if count == 1:
                print("Login Successfully.")
                print("Perform CRUD Operations.")
#--------------------------*CHOICES*-----------------------------        
                while True:
                        print("Input 'I' for Insertion a New Record.")
                	       print("Input 'U' for Update an Existing Record.")
                	       print("Input 'R' for Removal an Existing Record.")
                        print("Input 'S' for Searching a Record.")
                        print("Input 'D' for Display All Records.")
                        print("Input 'E' for Exit the Program.")
                        ch = input("Enter Your Option: ")
    #--------------------------*TABLE CREATION*----------------------------
                       if ch == 'I' or ch == 'i':
                               ins = "create table if not exists students(\
    reg_num int(20) primary key, loc_sr_num integer NOT NULL, yr_pass_xi int(5) NOT NULL, exam_cat char(5) NOT NULL, cand_name char(50) NOT NULL, mother_name char(50) NOT NULL, father_name char(50) NOT NULL, gender varchar(5), category1 varchar(5), minority varchar(5), PwD_status varchar(20), mob_num bigint NOT NULL, email_id varchar(50), aadhar_num bigint, sub_1 char(15), sub_2 char(15) NOT NULL, sub_3 char(15) NOT NULL, sub_4 char(15) NOT NULL, sub_5 char(15) NOT NULL, add_sub_6 char(15) NOT NULL, int_grade_sub1 char(30), int_grade_sub2 char(30), int_grade_sub3 char(30), annual_income varchar(25), roll_num_of_equi_exam_passed integer, exam_of_equi_exam_passed char(20), board_of_equi_exam_passed char(20), single_child char(5), migration_certificate char(5), adm_no integer, adm_date date)"
                        #print(ins)
                        mycursor.execute(ins)
#--------------------------*INSERTION OF RECORDS*-------------------         
                        print("Insertion Operation.")
                        reg = int(input("Enter student's registration_num: "))
                        locsr = int(input("Enter student's loc_sr_num: "))
                        yrpassc11 = int(input("Enter student's year_passing_class11: "))
                        ecat = input("Enter student's exam_cat: ")
                       cname = input("Enter student's Name: ")
                       mname = input("Enter student's mother's name: ")
                       fname = input("Enter student's father's name: ")
                       gender = input("Enter student's gender: ")
                       cat = input("Enter student's category: ")
                       minor = input("Enter if student belongs to minority section(y/n): ")
                       pwdis = input("Enter if student have disability (type of disability): ")
                      mnum = int(input("Enter student's mobile_num: "))
                      email = input("Enter student's email_id: ")
                      ad_num = int(input("Enter student's addhar number: "))
                      s1 = input("Enter subject1(compulsory language): ")
                      s2 = input("Enter subject2: ")
                      s3 = input("Enter subject3: ")
                      s4 = input("Enter subject4: ")
                      s5 = input("Enter subject5: ")
                      s6 = input("Enter subject6(additional): ")
                      intsub1 = input("Enter name of internal grade subject1: ")
                      intsub2 = input("Enter name of internal grade subject2: ")
                      intsub3 = input("Enter name of internal grade subject3: ")
                      aninc = int(input("Enter annual income of student's parents: "))
                      eexrnum = int(input("Enter student's rollnum of equivalent exam passed:"))
                      eexam = input("Enter student's exam of equivalent exam passed:")
                      eexboard = input("Enter student's board of equivalent exam passed:")
                      sch = input("Enter if student is single girl child or not:")
                      mgcr = input("Enter if migration certificate is required or not:")
                      adm_num = int(input("Enter student's admission num:"))
                      adm_date = input("Enter student's admission date as (yyyy-mm-dd):")

                      q = "insert into students (reg_num, loc_sr_num,\ yr_pass_xi,exam_cat, cand_name, mother_name, father_name, gender,\ category1, minority, PwD_status, mob_num, email_id, aadhar_num,\ sub_1, sub_2, sub_3, sub_4, sub_5, add_sub_6, int_grade_sub1,\ int_grade_sub2, int_grade_sub3, annual_income,\ roll_num_of_equi_exam_passed, exam_of_equi_exam_passed,\ board_of_equi_exam_passed, single_child, migration_certificate,\ adm_no, adm_date) values ({}, {}, {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, {}, '{}', '{}', '{}', '{}', {}, '{}') ".format (reg, locsr, yrpassc11, ecat, cname, mname, fname, gender, cat, minor, pwdis, mnum, email, ad_num ,s1, s2, s3, s4, s5, s6, intsub1, intsub2, intsub3, aninc, eexrnum, eexam, eexboard, sch, mgcr, adm_num, adm_date)
                       mycursor.execute(q)
                       con.commit()
                       print("Record is inserted Successfully.")
#--------------------------*UPDATION*-----------------------------               
                elif ch == 'U' or ch == 'u':
                        print("Updation of Record.")
                        reg = input("Enter Student's registration Number: ")              
                        sn = input("Enter New student's Name: ")
                        mn = input("Enter New student Mother's Name: ")
                        fn = input("Enter New student Father's Name: ")      
                        qry = "update students set cand_name = '{}', mother_name = '{}' , father_name = '{}' where reg_num = {}".format(sn,mn,fn,reg)
                        mycursor.execute(qry)
                        con.commit()
                        print("Record is updated Successfully.")
#--------------------------*DELETION*-----------------------------                   
                elif ch == 'R' or ch == 'r':
                        print("Removal of Record.")
                        reg = input("Enter Student's registration Number: ")
                        qry = "delete from students where reg_num = {}".format(reg)
                        mycursor.execute(qry)
                        con.commit()
                        print("Record is deleted Successfully.")
#--------------------------*SEARCHING*-----------------------------               
                elif ch == 'S' or ch == 's':
                        print("Searching Operation.")
                        reg = input("Enter Student's registration Number: ")              
                        qry = "select * from students where reg_num = {} ".format(reg)
                        #print(qry)
                        mycursor.execute(qry)
                        print("Record is found Successfully.")
                        data = mycursor.fetchone()
                        count = mycursor.rowcount
                        print("Total No. of Record:",count)
                        for row in data:
                                print(row)
#--------------------------*DISPLAY*-----------------------------                       
                elif ch == 'D' or ch == 'd':
                        print("Display ALl Records.")
                        qry = "select * from students"
                        mycursor.execute(qry)
                        data = mycursor.fetchall()
                        count = mycursor.rowcount
                        print("Total No. of Record: ",count)
                        print("{0:<9s} {1:<9s} {2:<9s} {3:<9s} {4:<9s} {5:<9s} {6:<9s} {7:<9s} {8:<9s} {9:<9s}" .format ('Sl.No', 'Name', 'MName', 'FName', 'Subject1', 'Subject2', 'Subject3','Subject4','Subject5','Subject6'))
                        print("________________________________ ____ _____________________________________________________"
                        for row in data:
                                  print ("{0:<9s} {1:<9s} {2:<9s} {3:<9s} {4:<9s} {5:<9s} {6:<9s} {7:<9s} {8:<9s} {9:<9s}" .format (str(row[1]), row[4], row[5], row[6], row[14], row[15], row[16], row[17],row[18],row[19]))
                elif ch == 'E' or ch == 'e':
                    print("Exiting Program.")
                    sys.exit(0)
                else:
                    print("Wrong Input. Try Again!!!!!")
           
        else:
            print("Login Failed")
            if at !=4:
                print("Try Again")
else:
    print("MySql DataBase Connection Failed.Terminating....")
