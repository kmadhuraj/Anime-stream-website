from django.shortcuts import render,redirect
from django.http import HttpResponse
from animieapp.models import Signups,Contact,Video
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages


# Create your views here.
def home(request):
    return HttpResponse("helloworld")



def signup(request):
    if  request.method =='POST':
        
        first_name=request.POST.get('f-name')
        second_name=request.POST.get('l-name')
        
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpass=request.POST.get('c-password')
        
        email_confirm=Signups.objects.filter(email=email)
        if email_confirm:
            messages.info(request,'Email is already exist')
            return render(request,'sign-up.html')
        else:
            Signups(first_name=first_name,second_name=second_name,email=email,password=password,cpass=cpass).save()
            messages.success(request,'Registration is Succesfull')
            # return render(request,'login.html')

    
    
    return render(request,'login.html')



#django authentication signup page

def Signup(request):
    if  request.method =='POST':
        username=request.POST['username']
        first_name=request.POST['f-name']
        last_name=request.POST['l-name']
        email=request.POST['email']
        password=request.POST['password']
        cpass=request.POST['c-password']
        
        #check errounous messages
        if len(username)>10:
            messages.warning(request,"Username must be under 10 characters ")
            return render(request,'sign-up.html')
            
        # check username only contain alphanumeric  
        if not username.isalnum():
            messages.warning(request,"Username only contain letters and numbers ")
            return render(request,'sign-up.html')
            
            
        # password sholud be match
        if password !=cpass:
            messages.warning(request,"Password does not match!")
            return render(request,'sign-up.html')
        
        
        username_check=User.objects.filter(username=username)
        if username_check:
            messages.warning(request,"Username already exist choose unique one")
            return render(request,'sign-up.html')
        
        #create the user
        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=first_name
        myuser.last_name=last_name
        myuser.save()
        messages.success(request,"Your account is created succesfully")
        return render(request,'index.html')
    
    return render(request,'sign-up.html')
    
    # return HttpResponse("404 not found")

def handlelogin(request):
    if request.method =="POST":
            # email = request.POST['email']
            username=request.POST['username']
            password = request.POST['password']
        
            # authenticate user name and password
            user = authenticate(username=username, password=password)
            

            if user is not None:
                messages.info(request, 'You are succesfully logged in')
                login(request,user)
                return redirect('/')
            else:
                messages.info(request, 'Invalid Credentials!')          
    # return HttpResponse("404 page not found")
                  
    return render(request,'login.html')
    

def handlelogout(request):
    logout(request)
    messages.success(request,"You are Succesfully logged out")
    return redirect('/')




def header(request):
    return render (request,'base.html')

def index(request):
    video=Video.objects.all()
    return render (request,'index.html',{'video':video})


def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        
        message=request.POST.get('message')
        
        contact= Contact(name=name,email=email,message=message)
        contact.save() 
        
    
    return render (request,'contact.html')

def mylist(request):
    return render(request ,'mylist.html')


def watchv(request,watch_id):
    video=Video.objects.all()
    watch_video=Video.objects.get(id=watch_id)
    dvar={
        'watch_video':watch_video,
        'video':video,
        
        
    }
    
    return render(request,'watch.html',dvar)