from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from . forms import SignupForm,LoginForm,UpdateForm,ChangePasswordForm
from django.contrib.auth import logout as logouts
from . models import Signup

def hiii(request):
    return HttpResponse("Welcome project2")

def index(request):
    name="Thanazal"
    return render(request,'index.html', {'data':name})

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST,request.FILES)
        
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            password=form.cleaned_data['Password']
            email=form.cleaned_data['Email']
            user=Signup.objects.filter(Email=email).exists()
            photo=form.cleaned_data['Photo']           
            if user:
                messages.success(request,'Email alreadys exist')
                return redirect('/signup')
            else:
                tab=Signup(Name=name,Age=age,Password=password,Email=email,Photo=photo) 
                tab.save()
                messages.success(request,'Successful')       
                return redirect('/')
              
    else:
        form=SignupForm()
    return render(request,'signup.html',{'form':form})

def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            user=Signup.objects.get(Email=email)
            if not user:
                messages.success(request,'Email does not exist')
                return redirect('/login')
            else:
                request.session['email']=email
                messages.success(request,'Login successful')
                return redirect('/home/%s' % user.id)
        
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})

def home(request,id):
    user=Signup.objects.get(id=id)
    return render(request,'home.html',{'user':user})

def update(request,id):
    user=Signup.objects.get(id=id)
    form=UpdateForm(request.POST or None,request.FILES or None,instance=user)
    if form.is_valid():
        form.save()
        messages.success(request,'Updated successfully')
        return redirect('/home/%s' % user.id)
    return render(request,'update.html',{'user':user,'form':form})

def password_change(request,id):
    user=Signup.objects.get(id=id)
    if request.method == 'POST':
       form=ChangePasswordForm(request.POST)
       if form.is_valid():
           oldpassword = form.cleaned_data['OldPassword']
           newpassword = form.cleaned_data['NewPassword']
           confirmNewpassword = form.cleaned_data['ConfirmNewPassword']
           if oldpassword != user.Password:
                messages.success(request,'Enter correct password')
                return redirect('/changePassword/%s' % user.id)
            
           elif newpassword != confirmNewpassword:
                messages.success(request,'Password Mismatch')
                return redirect('/changePassword/%s' % user.id)
           else:
                user.Password=newpassword
                user.save()
                messages.success(request,'Password changed successfully')
                return redirect('/home/%s' % user.id)

    else:
        form =ChangePasswordForm() 
    return render(request,'changepassword.html',{'user':user, 'form':form} )  

def logout(request):
    logouts(request)
    messages.success(request,'Logout Successfull')
    return redirect('/')
    
    
     

   
   
   
    
    



# Create your views here.
