from  django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from ebw_app.models import Ebw_data
from django.shortcuts import redirect, render

# Create your views here.

def home(request):

    if request.method=='POST':
        a=request.POST['mach_n1']
        b=request.POST['comp_n1']
        c=request.POST['mat_n1']
        d=request.POST['j_dia1']
        e=request.POST['j_dept1']
        f=request.POST['backup1']
        g=request.POST['gtwd1']
        h=request.POST['max_dop1']
        i=request.POST['min_dop1']
        j=request.POST['pfc1']
        k=request.POST['pbc1']

        p= Ebw_data()

        p.machine_name = a
        p.component_name = b
        p.material_name = c
        p.joint_dia = d
        p.joint_depth = e
        p.backup = f
        p.gtwd = g
        p.max_dop = h
        p.min_dop = i
        p.predicted_focus_current = j
        p.predicted_beam_current = k
        p.save()

        return render(request, "form.html")

    else:
        return render(request, "work_page.html")

def signup(request):

    if request.method == "POST":
        name = request.POST ["u_name"]
        password1 = request.POST ["passwd1"]
        password2 = request.POST ["passwd2"]
        emp_id = request.POST ["e_id"]
        print("collected")
        
        if password1 == password2:
            print("Password Match")
            
            if User.objects.filter(username=emp_id).exists():
                print("name")
                return render(request, 'Registor.html', {'msg':"* Id Already Exist"})
            else:
                user1 = User.objects.create_user(first_name = name, username = emp_id, password =  password2, last_name = password1)
                user1.save();
                print("save")
                return redirect("/signin")
        else:
            print("Not matched")
            return render(request, 'Registor.html', {'msg':"* Password not matching"})
    else:
        print("not Posted")
        return render (request, "Registor.html",{"msg":" "})

def signin(request):

    if request.method == "POST":
        emp_id = request.POST ["e_id"]
        passwd = request.POST ["passwd"]
        usr = auth.authenticate (username=emp_id, password = passwd)
        if usr is not None:
            auth.login(request, usr)
            request.session["keyid"]=True
            return redirect("/")
        else:
            messages.info(request,"* Incorrect Entry")
            return render(request,"login.html")
    return render(request,"login.html")

def signout(request):
    auth.logout(request)
    return redirect("/")



        

