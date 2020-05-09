
from django.urls import path
from . import views
from . import Doctor_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home),
    path('myReport/',views.myReport),
    path('Emergency/',views.map),
    path('Profile/',views.profile),
    path('login/',views.login),
    path('BookDoctor/',views.bookDoctor),
    path('searchDoctor/',views.seachDoctor),
    path('searchTreatment/',views.searchTreatment),
    path('search_remedies',views.search_remedies),
    path('signup_patient',views.signup_patient),
    path('signup_doctor',Doctor_views.signup_doctor),
    path('searchDoctorby',views.searchDoctorby),
    path('BookDoctor/doctor',views.doctor),
    path('appointment',views.appointment),
    path('logout/',views.logout),
    path('doctor_book',Doctor_views.doctor_book),
    path('doctorHome',Doctor_views.home),
    path('doctorAppointment',Doctor_views.appointment),
    path('BookDoctorByDoctor',Doctor_views.bookDoctor),
    path('patient',Doctor_views.getpatientbydoctor),
    path('doctorProfile',Doctor_views.profile_fun)

]
urlpatterns+=staticfiles_urlpatterns()
