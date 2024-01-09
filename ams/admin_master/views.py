from django.shortcuts import render
from admin_master.models import Department,Designation,Qualification,Class,Division,Employee_category
from django.http import JsonResponse
from django.conf import settings 

# Create your views here.
# -------------department----------------
def department_manage(request):
    deplist=Department.objects.all().values
    msg=""
    if request.POST:
        type=""
        dptname=request.POST["depname"].strip()
        dptcode=request.POST["depcode"].strip()
        if dptname=='' and dptcode=='':
            msg="please fill details"
            type="error"
            return render(request,'department_manage.html',{'message':msg,'type':type, 'deplist':deplist})
        elif Department.objects.filter(depname=dptname).exists() or Department.objects.filter(depcode=dptcode).exists():
            msg="Department name and code already exist"
            type="warning"
            return render(request,'department_manage.html',{'message':msg,'type':type, 'deplist':deplist})
        else:
            depadd=Department(depname=dptname,depcode=dptcode)
            depadd.save()
            msg="Department added successfully"
            type="success"
            return render(request,'department_manage.html',{'message':msg,'type':type ,'deplist':deplist})
    return render(request,'department_manage.html',{'deplist':deplist})

# -------department edit---------
def department_edit(request):
    depid=request.GET['eid']
    record=Department.objects.get(id=depid)
    res={'deptname':record.depname,'deptcode':record.depcode,'deptstatus':record.status}
    return JsonResponse(res)

# --------department update-------
def department_update(request):
    msg=""
    type=""
    depid=request.GET['eid']
    depname=request.GET['depname']
    depcode=request.GET['depcode']
    status=request.GET['depstatus']
    if depname=='' and depcode=='':
            msg="please fill details"
            type="error"
            
    elif Department.objects.filter(depname=depname,depcode=depcode).exclude(id=depid).exists() :
        msg="Department name and code already exist"
        type="warning"
        
    else:
        depupdate=Department.objects.get(id=depid)
        depupdate.depname=depname
        depupdate.depcode=depcode
        depupdate.status=status
        depupdate.save()
        msg="submitted"
        type="success"
    return JsonResponse({'message':msg,'type':type})

# ------------department delete------------
def department_delete(request):
    delid=request.GET['eid']
    deldep=Department.objects.get(id=delid)
    deldep.delete()
    msg="deleted"
    return JsonResponse({'message':msg})



# --------------------designation--------------------------
def designation_manage(request):
    deslist=Designation.objects.all().values
    msg=""
    if request.POST:
        type=""
        desiname=request.POST["desname"].strip()
        desicode=request.POST["descode"].strip()
        if desiname=='' and desicode=='':
            msg="please fill details"
            type="error"
            return render(request,'designation_manage.html',{'message':msg,'type':type, 'deslist':deslist})
        elif Designation.objects.filter(desname=desiname).exists() or Designation.objects.filter(descode=desicode).exists():
            msg="Designation name and code already exist"
            type="warning"
            return render(request,'designation_manage.html',{'message':msg,'type':type, 'deslist':deslist})
        else:
            desadd=Designation(desname=desiname,descode=desicode)
            desadd.save()
            msg="Designation added successfully"
            type="success"
            return render(request,'designation_manage.html',{'message':msg,'type':type ,'deslist':deslist})
    return render(request,'designation_manage.html',{'deslist':deslist})

# -----designation edit-----
def designation_edit(request):
    desid=request.GET['eid']
    record=Designation.objects.get(id=desid)
    res={'desiname':record.desname,'desicode':record.descode,'desistatus':record.status}
    return JsonResponse(res)

# -------designation update------
def designation_update(request):
    msg=""
    type=""
    desid=request.GET['eid']
    desname=request.GET['desname']
    descode=request.GET['descode']
    status=request.GET['desstatus']
    if desname=='' and descode=='':
            msg="please fill details"
            type="error"
            
    elif Designation.objects.filter(desname=desname,descode=descode).exclude(id=desid).exists() :
        msg="Designation name and code already exist"
        type="warning"
        
    else:
        desupdate=Designation.objects.get(id=desid)
        desupdate.desname=desname
        desupdate.descode=descode
        desupdate.status=status
        desupdate.save()
        msg="submitted"
        type="success"
    return JsonResponse({'message':msg,'type':type})

# -------------designation delete----------------
def designation_delete(request):
    desid=request.GET['eid']
    deldes=Designation.objects.get(id=desid)
    deldes.delete()
    msg="deleted"
    return JsonResponse({'message':msg})

# ---------------------------QUALIFICATION---------------------------------------
def qualification_manage(request):
    quallist=Qualification.objects.all().values
    msg=""
    if request.POST:
        type=""
        qualiname=request.POST["qualname"].strip()
        if qualiname=='':
            msg="please fill details"
            type="error"
            return render(request,'qualification_manage.html',{'message':msg,'type':type, 'quallist':quallist})
        elif Qualification.objects.filter(qualname=qualiname).exists() :
            msg="Qualification already exist"
            type="warning"
            return render(request,'qualification_manage.html',{'message':msg,'type':type, 'quallist':quallist})
        else:
            qualadd=Qualification(qualname=qualiname)
            qualadd.save()
            msg="Qualification added successfully"
            type="success"
            return render(request,'qualification_manage.html',{'message':msg,'type':type ,'quallist':quallist})
    return render(request,'qualification_manage.html',{'quallist':quallist})

# -----qualification edit------
def qualification_edit(request):
    qualid=request.GET['eid']
    record=Qualification.objects.get(id=qualid)
    res={'qname':record.qualname,'qstatus':record.status}
    return JsonResponse(res)

# ------qualification update-----
def qualification_update(request):
    msg=""
    type=""
    qualid=request.GET['eid']
    qualname=request.GET['qualname']
    status=request.GET['qualstatus']
    if qualname=='':
            msg="please fill details"
            type="error"
            
    elif Qualification.objects.filter(qualname=qualname).exclude(id=qualid).exists() :
        msg="Qualification already exist"
        type="warning"
        
    else:
        qualedit=Qualification.objects.get(id=qualid)
        qualedit.qualname=qualname
        qualedit.status=status
        qualedit.save()
        msg="submitted"
        type="success"
    return JsonResponse({'message':msg,'type':type})

# ---------Qualification delete-------------
def qualification_delete(request):
    qualid=request.GET['eid']
    delqual=Qualification.objects.get(id=qualid)
    delqual.delete()
    msg="deleted"
    return JsonResponse({'message':msg})



# -----------CLASS-----------
def class_manage(request):
    classlist=Class.objects.all().values
    msg=""
    if request.POST:
        type=""
        clsname=request.POST["classname"].strip()
        if clsname=='':
            msg="please fill details"
            type="error"
            return render(request,'class_manage.html',{'message':msg,'type':type, 'classlist':classlist})
        elif Class.objects.filter(classname=clsname).exists() :
            msg="Class already exist"
            type="warning"
            return render(request,'class_manage.html',{'message':msg,'type':type, 'classlist':classlist})
        else:
            classadd=Class(classname=clsname)
            classadd.save()
            msg="Class added successfully"
            type="success"
            return render(request,'Class_manage.html',{'message':msg,'type':type ,'classlist':classlist})
    return render(request,'class_manage.html',{'classlist':classlist})

# ---------class edit-------
def class_edit(request):
    classid=request.GET['eid']
    record=Class.objects.get(id=classid)
    res={'cname':record.classname,'cstatus':record.status}
    return JsonResponse(res)


# -----------class update---------
def class_update(request):
    msg=""
    type=""
    clsid=request.GET['eid']
    clsname=request.GET['classname']
    status=request.GET['classstatus']
    if clsname=='':
            msg="please fill details"
            type="error"
            
    elif Class.objects.filter(classname=clsname).exclude(id=clsid).exists() :
        msg="Class already exist"
        type="warning"
        
    else:
        clsedit=Class.objects.get(id=clsid)
        clsedit.classname=clsname
        clsedit.status=status
        clsedit.save()
        msg="submitted"
        type="success"
    return JsonResponse({'message':msg,'type':type})

# -------------class delete
def class_delete(request):
    clsid=request.GET['eid']
    delclass=Class.objects.get(id=clsid)
    delclass.delete()
    msg="deleted"
    return JsonResponse({'message':msg})





# -------   DIVISION----------
def division_manage(request):
    divlist=Division.objects.all().values
    msg=""
    if request.POST:
        type=""
        divisionname=request.POST["divname"].strip()
        if divisionname=='':
            msg="please fill details"
            type="error"
            return render(request,'division_manage.html',{'message':msg,'type':type, 'divlist':divlist})
        elif Division.objects.filter(divname=divisionname).exists() :
            msg="Division already exist"
            type="warning"
            return render(request,'division_manage.html',{'message':msg,'type':type, 'divlist':divlist})
        else:
            divadd=Division(divname=divisionname)
            divadd.save()
            msg="Division added successfully"
            type="success"
            return render(request,'division_manage.html',{'message':msg,'type':type ,'divlist':divlist})
    return render(request,'division_manage.html',{'divlist':divlist})

def division_get(request):
    divid=request.GET['eid']
    record=Division.objects.get(id=divid)
    res={'name':record.divname,'status':record.status}
    return JsonResponse(res)

def division_update(request):
    msg=""
    type=""
    divid=request.GET['eid']
    divname=request.GET['divname']
    status=request.GET['divstatus']
    if divname=='':
            msg="please fill details"
            type="error"
            
    elif Division.objects.filter(divname=divname).exclude(id=divid).exists() :
        msg="Division already exist"
        type="warning"
        
    else:
        divedit=Division.objects.get(id=divid)
        divedit.divname=divname
        divedit.status=status
        divedit.save()
        msg="submitted"
        type="success"
    return JsonResponse({'message':msg,'type':type})

# ----------Division delete---------
def division_delete(request):
    divid=request.GET['eid']
    deldiv=Division.objects.get(id=divid)
    deldiv.delete()
    msg="deleted"
    return JsonResponse({'message':msg})



        
def employee_manage(request):
    emplist=Employee_category.objects.all()
    msg=""
    if request.POST:
        type=""
        empname=request.POST["ename"].strip()
        emparea=request.POST["earea"]
        if empname=='' and emparea=='':
            msg="please fill details"
            type="error"
            return render(request,'employee_manage.html',{'message':msg,'type':type, 'emplist':emplist,"settings":settings})
        elif Employee_category.objects.filter(ename=empname).exists() or Employee_category.objects.filter(area=emparea).exists():
            msg="Employee category name and area already exist"
            type="warning"
            return render(request,'employee_manage.html',{'message':msg,'type':type, 'emplist':emplist,"settings":settings})
        else:
            empadd=Employee_category(ename=empname,area=emparea)
            empadd.save()
            msg="Employee added successfully"
            type="success"
            return render(request,'employee_manage.html',{'message':msg,'type':type ,'emplist':emplist,"settings":settings})

    return render(request,'employee_manage.html',{'emplist':emplist,"settings":settings})

# -----------------employeee edit------------
def employee_edit(request):
    empid=request.GET['eid']
    record=Employee_category.objects.get(id=empid)
    res={'ename':record.ename,'earea':record.area,'estatus':record.status}
    return JsonResponse(res)

# ---------------employee update-------------
def employee_update(request):
    msg=""
    type=""
    empid=request.GET['eid']
    empname=request.GET['empname']
    emparea=request.GET['emparea']
    status=request.GET['empstatus']
    if empname=='' and emparea=='':
            msg="please fill details"
            type="error"
            
    elif Employee_category.objects.filter(ename=empname,area=emparea).exclude(id=empid).exists() :
        msg="employee name and area already exist"
        type="warning"
        
    else:
        empupdate=Employee_category.objects.get(id=empid)
        empupdate.ename=empname
        empupdate.area=emparea
        empupdate.status=status
        empupdate.save()
        msg="submitted"
        type="success"
    return JsonResponse({'message':msg,'type':type})


# ----------Employee delete---------
def employee_delete(request):
    empid=request.GET['eid']
    delemp=Employee_category.objects.get(id=empid)
    delemp.delete()
    msg="deleted"
    return JsonResponse({'message':msg})


# -------------------SUBJECT-----------------
def subject_manage(request):
    return render(request,'subject_manage.html')
















