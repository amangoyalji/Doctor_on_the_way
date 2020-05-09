from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
import pymysql as py
from bs4 import BeautifulSoup
import requests

def home(request):
    if request.session.has_key('username'):
        return render(request,'doctor_home.html')
    else:
        return render(request, 'doctor_home.html')

def bookDoctor(request):
    if request.session.has_key('username'):
        return render(request,'bookAppointmentByDoctor.html')
    else:
        return redirect('/')

def appointment(request):
    if request.session.has_key('username'):
        username = request.session['username']
        try:
            conn = py.connect(host='localhost', port=3306, user='root', password='123', db='only2days')
            cmd = conn.cursor()
            q = "select * from  doctor_appointment where doctorUsername='{}'".format(username)
            cmd.execute(q)
            data = cmd.fetchall()
            conn.commit()
            conn.close()
            return render(request, 'doctor_appointment.html', {'result': data})
        except Exception as e:
            return e
    else:
        print('shiva')
        return redirect('/')

def profile(request):
    if request.session.has_key('username'):
        return render(request,'profile.html',{'login':1})
    else:
        return redirect('/')

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

def logout(request):
    try:
        del request.session['username']
    except KeyError:
        return JsonResponse({'result':'logout not successfully'})
    return JsonResponse({'result':'logout successfully'})

def getpatientbydoctor(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        conn = py.connect(host='localhost', port=3306, user='root', password='123', db='only2days')
        cmd = conn.cursor()
        q = "select * from patient where patientUsername='{}' and patientpwd='{}'".format(username, password)
        cmd.execute(q)
        data = cmd.fetchone()
        conn.commit()
        conn.close()
        if data is None:
            return render(request, 'bookAppointmentByDoctor.html', {'msg':'invalid username or password'})
        else:
            return patient(request,username)
    except Exception as e:
        return e

def patient(request,username):
    print(username)
    try:
        conn = py.connect(host='localhost', port=3306, user='root', password='123', db='only2days')
        cmd = conn.cursor()
        q = "select * from doctor where doctorUsername='{}'".format(request.session['username'])
        cmd.execute(q)
        data = cmd.fetchone()
        conn.commit()
        conn.close()
        print(data[0])
        return render(request, 'doctor_book.html', {'username':data[0],'fname':data[1],'lname':data[2],'specialist':data[9],'place':data[12]})
    except Exception as e:
        return e

def doctor_book(request):
    username=request.session['username']
    place=request.GET['place']
    specialist= request.GET['specialist']
    name=request.GET['name']
    token=request.GET['token']
    adate=request.GET['adate']
    bdate=request.GET['bdate']
    try:
        conn = py.connect(host='localhost', port=3306, user='root', password='123', db='only2days')
        cmd = conn.cursor()
        q = "insert into userappointment (username,bookdate,appointmentdate,doctorName,doctorPlace,token,treatment) values ('{}','{}','{}','{}','{}','{}','{}')".format(username,bdate,adate,name,place,token,specialist)
        print(q)
        cmd.execute(q)
        print("Record of patient Submitted")
        conn.commit()
        conn.close()
        return JsonResponse({'result': name})
    except Exception as e:
        return print(e)

def signup_doctor(request):
    username = request.GET['username']
    ufname = request.GET['ufname']
    ulname = request.GET['ulname']
    email = request.GET['email']
    gender = request.GET['gender']
    bdate = request.GET['bdate']
    experience = int(request.GET['experience'])
    mobileno = int(request.GET['mobileno'])
    specialist = request.GET['uspecialist']
    education = request.GET['education']
    address = request.POST['address']
    ustate = request.POST['ustate']
    ucity = request.POST['ucity']
    password = request.POST['password']
    res = get_doctor(username, ufname, ulname, email, gender, bdate, mobileno, experience, education, specialist,
                     address, ustate, ucity, password)
    if (res == '1'):
        return HttpResponse("record subitted succesfully")
    else:
        return HttpResponse("sorry submission error")


def get_doctor(dorun, dorfn, dorln, dore, dorg, dordob, dmo, dexp, dedu, dspec, dadd, dst, dorc, dpwd):
    try:
        conn = py.connect(host='localhost', port=3306, user='root', password='123', db='only2days')
        cmd = conn.cursor()

        q = "insert into doctor(doctorUsername,doctorfname,doctorlname,doctoremail,doctorgender,doctordob,doctormob,doctorexp,doctorgedu,doctorspec,doctoradd,doctorstate,doctorcity,doctorpwd) values('{}','{}','{}','{}','{}','{}',{},{},'{}','{}','{}','{}','{}','{}')".format(
            dorun, dorfn, dorln, dore, dorg, dordob, dmo, dexp, dedu, dspec, dadd, dst, dorc, dpwd)
        print(q)
        cmd.execute(q)
        print("doctor Record Submitted")
        conn.commit()
        conn.close()
        return ('1')
    except:
        return ('0')


def profile_fun(request):
    try:
        conn = py.connect(host='localhost', port=3306, user='root', password='123', db='only2days')
        cmd = conn.cursor()
        q = "select * from doctor where doctorUsername='{}'".format(request.session['username'])
        cmd.execute(q)
        result = cmd.fetchone()
        conn.close()
        return render(request, 'doctor_profile.html', {'result': result, 'login': 1})
    except:
        return ('0')