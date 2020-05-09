from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
import pymysql as py
from bs4 import BeautifulSoup
import requests

def home(request):
    print(request.session.get_expiry_age())
    if request.session.has_key('username'):
        return render(request,'home.html',{'login':1})
    else:
        return render(request, 'home.html', {'login': 0})

def bookDoctor(request):
    if request.session.has_key('username'):
        return render(request,'bookDoctor.html',{'login':1})
    else:
        return redirect('/')

def map(request):
    return render(request, 'map.html')

def appointment(request):
    if request.session.has_key('username'):
        print('shivam')
        username = 'shivam'
        try:
            conn = py.connect(host='localhost', port=3306, user='root', password='123', db='only2days')
            cmd = conn.cursor()
            q = "select * from  userappointment where username='{}'".format(username)
            cmd.execute(q)
            data = cmd.fetchall()
            conn.commit()
            conn.close()
            return render(request, 'appointment.html', {'result': data, 'login': 1})
        except Exception as e:
            return e
    else:
        print('shiva')
        return redirect('/')
        

def myReport(request):
    if request.session.has_key('username'):
        return render(request, 'myReport.html',{'login':1})
    else:
        return redirect('/')

def profile(request):
    if request.session.has_key('username'):
        try:
            conn = py.connect(host='localhost', port=3306, user='root', password='123', db='only2days')
            cmd = conn.cursor()
            q = "select * from patient where patientUsername='{}'".format(request.session['username'])
            print(q)
            cmd.execute(q)
            result = cmd.fetchone()
            conn.close()
            return render(request,'Profile.html',{'login':1,'result':result})
        except Exception as e:
            return e
    else:
        return redirect('/')

def check(request):
    return render(request,'check.html')

def login(request):
    username=request.GET['username']
    password=request.GET['password']
    users=int(request.GET['users'])
    try:
        conn = py.connect(host='localhost', port=3306, user='root', password='123', db='only2days')
        cmd = conn.cursor()
        if users==0:
            q = "select * from patient where patientUsername='{}' and patientpwd='{}'".format(username,password)
        elif users==1:
            q = "select * from doctor where doctorUsername='{}' and doctorpwd='{}'".format(username, password)
        cmd.execute(q)
        data=cmd.fetchone()
        conn.commit()
        conn.close()
        if data is None:
            return render(request, 'home.html', {'login': 0})
        else:
            request.session['username']=username
            request.session.set_expiry(0)
            if users==0:
                return redirect('/')
            elif users==1:
                return redirect('/doctorHome')
    except Exception as e:
        return e

def logout(request):
    try:
        del request.session['username']
    except KeyError:
        return JsonResponse({'result':'logout not successfully'})
    return JsonResponse({'result':'logout successfully'})

def signup_patient(request):
    if request.method=='POST':
        username = request. POST['username']
        ufname = request.POST['ufname']
        ulname = request.POST['ulname']
        email = request.POST['email']
        gender = request.POST['gender']
        bdate = request.POST['bdate']
        blood = request.POST['blood']
        mobileno = int(request.POST['mobileno'])
        address = request.POST['address']
        ustate = request.POST['ustate']
        ucity = request.POST['ucity']
        password = request.POST['password']
        res = get_patient(username, ufname, ulname, email, gender, bdate, blood, mobileno, address, ustate,
                             ucity, password)
        if (res == '1'):
            return HttpResponse("record subitted succesfully")
        else:
            return HttpResponse("sorry submission error")

def seachDoctor(request):
    a = request.GET['a']
    try:
        conn = py.connect(host='localhost', port=3306, user='root', password='123', db='only2days')
        cmd = conn.cursor()
        q = "select * from doctor where doctorcity='{}'".format(a)
        print(q)
        cmd.execute(q)
        data=cmd.fetchall()
        print(data)
        conn.commit()
        conn.close()
        return JsonResponse({'result': data})
    except Exception as e:
        return e

def searchDoctorby(request):
    a = request.GET['a']
    b=request.GET['b']
    try:
        conn = py.connect(host='localhost', port=3306, user='root', password='123', db='only2days')
        cmd = conn.cursor()
        if b=='city':

         q = "select * from doctor where doctorcity like '{}%'".format(a)
        elif b=='name':
            q = "select * from doctor where doctorfname like '{}%'".format(a)
        elif b=='specialist':
            q = "select * from doctor where doctorspec like '{}%'".format(a)
        print(q)
        cmd.execute(q)
        data = cmd.fetchall()
        print(data)
        conn.commit()
        conn.close()
        return JsonResponse({'result': data})
    except Exception as e:
        return e

def searchTreatment(request):
    a = request.GET['a']
    return JsonResponse({'result':1})

def search_remedies(request):
    text = 'https://www.google.co.in/search?q='
    a = request.GET['a']
    text = text + a
    response = requests.get(text)
    soup = BeautifulSoup(response.text, 'lxml')
    head = soup.findAll('div', {"class": "mraOPb"})
    head = str(head)
    if head :
        print("xcvb")
        return JsonResponse({'result':head})
    head = soup.findAll('div', {"class": "g"})
    head = str(head)
    return JsonResponse({'result':head})


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
    except Exception as e:
        return print(e)

def doctor(request):
    username=request.GET['username']
    try:
        conn = py.connect(host='localhost', port=3306, user='root', password='123', db='only2days')
        cmd = conn.cursor()
        q = "select * from doctor where doctorUsername='{}'".format(username)
        cmd.execute(q)
        data = cmd.fetchone()
        conn.commit()
        conn.close()
        l=[1,2,4,7,8,9]
        print(data[0])
        return render(request, 'doctorProfile.html', {'login':1,'username':data[0],'fname':data[1],'lname':data[2],'specialist':data[9]})
    except Exception as e:
        return e
def doctor_book(request):
    specialist= request.GET['specialist']
    name=request.GET['name']
    token=request.GET['token']
    adate=request.GET['adate']
    bdate=request.GET['bdate']
    return JsonResponse({'result':token})

def profile_fun(request):
    try:
        conn = py.connect(host='localhost', port=3306, user='root', password='123', db='only2days')
        cmd = conn.cursor()
        q = "select * from patient where patientUsername={''}".format(request.session['username'])
        cmd.execute(q)
        result = cmd.fetchone()
        conn.close()
        return HttpResponse(result)
    except Exception as e:
        return e