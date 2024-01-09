from django.urls import path
from .import views

urlpatterns = [
     path('dpt/',views.department_manage, name="master_department"),
     path('depedit/',views.department_edit,name="depedit"),
     path('depupdate/',views.department_update,name="depupdate"),
     path('depdel/',views.department_delete,name="depdel"),

     path('des/',views.designation_manage,name="master_designation"),
     path('desedit/',views.designation_edit,name="desedit"),
     path('desupdate/',views.designation_update,name="desupdate"),
     path('desdel/',views.designation_delete,name="desdel"),

     path('qual/',views.qualification_manage,name="master_qualification"),
     path('qualedit/',views.qualification_edit,name="qualedit"),
     path('qualupdate/',views.qualification_update,name="qualupdate"),
     path('qualdel/',views.qualification_delete,name="qualdel"),

     path('class/',views.class_manage,name="master_class"),
     path('classedit/',views.class_edit,name="classedit"),
     path('classupdate/',views.class_update,name="classupdate"),
     path('classdel/',views.class_delete,name="classdel"),

     path('div/',views.division_manage,name="master_division"),
     path('divget/',views.division_get,name="div_get"),
     path('divupdate/',views.division_update,name="divupdate"),
     path('divdel/',views.division_delete,name="divdel"),

     path('emp/',views.employee_manage,name="master_employee"),
     path('empedit/',views.employee_edit,name="empedit"),
     path('empupdate/',views.employee_update,name="empupdate"),
     path('empdel/',views.employee_delete,name="empdel"),

     path('sub/',views.subject_manage,name="master_subject"),
     


]




     

     
     
     
     
     

     