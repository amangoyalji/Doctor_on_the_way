import pymysql as py

def table_patient():
    try:
        conn = py.connect(host='localhost', port=3306, user='root', password='123', db='new_project')
        cmd = conn.cursor()
        q = "create table patient(patientUsername varchar(45) primary key, patientfname varchar(45),patientlname varchar(45),patientemail varchar(60),patientgender varchar(10),patientdob date,patientbg varchar(45),patientmob numeric(15),patientadd varchar(100),patientstate varchar(45),patientcity varchar(45),patientpwd varchar(45))"
        cmd.execute(q)
        print("Table patient Created...")
        conn.commit()
        conn.close()
    except:
        print("Table patient Already Created....")



def table_doctor():
    try:
        conn = py.connect(host='localhost', port=3306, user='root', password='123', db='new_project')
        cmd = conn.cursor()
        q = "create table doctor(doctorUsername varchar(45) primary key,doctorfname varchar(45),doctorlname varchar(45),doctoremail varchar(60),doctorgender varchar(10),doctordob date,doctormob numeric(15),doctorexp numeric(3),doctorgedu varchar(100),doctorspec varchar(100),doctoradd varchar(100),doctorstate varchar(45),doctorcity varchar(45),doctorpwd varchar(45))"
        cmd.execute(q)
        print("Table doctor Created...")
        conn.commit()
        conn.close()
    except Exception as e:
        print("Table doctor Already Created...."+e)

def table_hospital():
    try:
        conn = py.connect(host='localhost', port=3306, user='root', password='123', db='new_project')
        cmd = conn.cursor()
        print("njbmnbmnbmn")
        q = "create table hospital(hospUsername varchar(45) primary key,hospname varchar(45),ohospname varchar(45),hospemail varchar(60),hospmob numeric(15),hospyoe integer,hospapec varchar(60),hospadd varchar(100),hospstate varchar(45),hospcity varchar(45),hoappwd varchar(45))"
        cmd.execute(q)
        print("Table hospital Created...")
        conn.commit()
        conn.close()
    except:
        print("Table hospital Already Created....")


def put_patient():
    try:
        conn = py.connect(host='localhost', port=3306, user='root', password='123', db='new_project')
        cmd = conn.cursor()
        pun=input("enter your username:")
        pfn= input("Enter Pateint first name Id:")
        pln = input("Enter Patient last Name:")
        pe = input("Enter Patient email")
        pg= input("Enter Patient gender")
        pdob = input("Enter date of birth:")
        pbg = input("Enter blood group")
        pmo = int(input("Enter mobile no:"))
        pa = input("Enter Patient address:")
        ps = input("Enter Patient state:")
        pc = input("Enter Patient city")
        pwd = input("Enter Patient password:")
        q = "insert into patient(patientUsername,patientfname,patientlname,patientemail,patientgender,patientdob,patientbg,patientmob,patientadd,patientstate,patientcity,patientpwd) values('{}','{}','{}','{}','{}','{}','{}',{},'{}','{}','{}','{}')".format(pun,pfn,pln,pe,pg,pdob,pbg,pmo,pa,ps,pc,pwd)
        print(q)
        cmd.execute(q)
        print("Record of patient Submitted")
        conn.commit()
        conn.close()
    except:
        print("Fail to Submit patient Record...")



def put_doctor():
    try:
        conn = py.connect(host='localhost', port=3306, user='root', password='123', db='new_project')
        cmd = conn.cursor()
        dorun=input("enter the username")
        dorfn = input("Enter Doctor first name Id:")
        dorln = input("Enter Doctor last Name:")
        dore = input("Enter Doctor email")
        dorg = input("Enter Doctor gender")
        dordob = input("Enter doctors date of birth:")
        dmo = int(input("Enter doctors mobile no:"))
        dexp = int(input("Enter doctor experience :"))
        dedu= input("Enter doctors education:")
        dspec = input("Enter doctors specialization")
        dadd = input("Enter doctors address:")
        dst = input("Enter doctors state:")
        dorc = input("Enter doctors city")
        dpwd = input("Enter doctors password:")
        q = "insert into doctor(doctorUsername,doctorfname,doctorlname,doctoremail,doctorgender,doctordob,doctormob,doctorexp,doctorgedu,doctorspec,doctoradd,doctorstate,doctorcity,doctorpwd) values('{}','{}','{}','{}','{}','{}',{},{},'{}','{}','{}','{}','{}','{}')".format(dorun,dorfn,dorln,dore,dorg,dordob,dmo,dexp,dedu,dspec,dadd,dst,dorc,dpwd)
        print(q)
        cmd.execute(q)
        print("doctor Record Submitted")
        conn.commit()
        conn.close()
    except:
        print("Fail to Submit doctor Record...")


def put_hospital():
    try:
        conn = py.connect(host='localhost', port=3306, user='root', password='123', db='new_project')
        cmd = conn.cursor()
        hosun=input("enter the username")
        hosn = input("Enter Hospital name:")
        ohons = input("Enter hospital owner Name:")
        hosemail = input("Enter hospital email")
        hosmo = int(input("Enter hospital mobile no:"))
        hosyoe= int(input("Enter hospital year of establishment address:"))
        hosspec= input("Enter hospital treatments:")
        hosadd = input("Enter hospital address:")
        hosstate = input("Enter hospital state:")
        hoscity = input("Enter Patient city:")
        hospwd=input("enter your hospital password:")
        q = "insert into hospital(hospUsername,hospname,ohospname,hospemail,hospmob,hospyoe,hospapec,hospadd,hospstate,hospcity,hoappwd) values('{}','{}','{}','{}',{},{},'{}','{}','{}','{}','{}')".format(hosun,hosn,ohons,hosemail,hosmo,hosyoe,hosspec,hosadd,hosstate,hoscity,hospwd)
        print(q)
        cmd.execute(q)
        print("hospital Record Submitted")
        conn.commit()
        conn.close()
    except:
        print("Fail to Submit hospital Record...")

def get_patient(pun,pfn,pln,pe,pg,pdob,pbg,pmo,pa,ps,pc,pwd):
    try:
        conn = py.connect(host='localhost', port=3306, user='root', password='123', db='only2days')
        cmd = conn.cursor()
        q = "insert into patient(patientUsername,patientfname,patientlname,patientemail,patientgender,patientdob,patientbg,patientmob,patientadd,patientstate,patientcity,patientpwd) values('{}','{}','{}','{}','{}','{}','{}',{},'{}','{}','{}','{}')".format(pun,pfn,pln,pe,pg,pdob,pbg,pmo,pa,ps,pc,pwd)
        print(q)
        cmd.execute(q)
        print("Record of patient Submitted")
        conn.commit()
        conn.close()
        return('1')
    except:
        return('0')




def get_doctor(dorun,dorfn,dorln,dore,dorg,dordob,dmo,dexp,dedu,dspec,dadd,dst,dorc,dpwd):
    try:
        conn = py.connect(host='localhost', port=3306, user='root', password='123', db='new_project')
        cmd = conn.cursor()

        q = "insert into doctor(doctorUsername,doctorfname,doctorlname,doctoremail,doctorgender,doctordob,doctormob,doctorexp,doctorgedu,doctorspec,doctoradd,doctorstate,doctorcity,doctorpwd) values('{}','{}','{}','{}','{}','{}',{},{},'{}','{}','{}','{}','{}','{}')".format(dorun,dorfn,dorln,dore,dorg,dordob,dmo,dexp,dedu,dspec,dadd,dst,dorc,dpwd)
        print(q)
        cmd.execute(q)
        print("doctor Record Submitted")
        conn.commit()
        conn.close()
        return('1')
    except:
        return('0')


def get_hospital(hosun,hosn,ohons,hosemail,hosmo,hosyoe,hosspec,hosadd,hosstate,hoscity,hospwd):
    try:
        conn = py.connect(host='localhost', port=3306, user='root', password='123', db='new_project')
        cmd = conn.cursor()
        q = "insert into hospital(hospUsername,hospname,ohospname,hospemail,hospmob,hospyoe,hospapec,hospadd,hospstate,hospcity,hoappwd) values('{}','{}','{}','{}',{},{},'{}','{}','{}','{}','{}')".format(hosun,hosn,ohons,hosemail,hosmo,hosyoe,hosspec,hosadd,hosstate,hoscity,hospwd)
        print(q)
        cmd.execute(q)
        print("hospital Record Submitted")
        conn.commit()
        conn.close()
        return('1')
    except:
        return('0')
