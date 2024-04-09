from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth.models import User
from .models import donateTbl,registeredUser,fundraiseTbl,campaignTbl,volunteertbl,messagetbl,User

def index(request):
    return render(request,'index.html')

# Create your views here.
def donateView(request):
    if request.method == 'POST':
        uname=request.POST.get('uname')
        username=registeredUser.objects.filter(username=uname).get()
        freq=request.POST.get('freq')
        dtype=request.POST.get('dtype')
        category=request.POST.get('category')
        amount=request.POST.get('amount')
        print(username,freq,dtype,category,amount)
        
        donate = donateTbl(username=username,freq=freq,dtype=dtype,category=category,amount=amount)
        donate.save()
        
        print("data saved")
        return redirect('/')
    return render(request,'donate.html')

def aboutView(request):
    return render(request,'about.html')

def campaignView(request):
    if request.method == 'POST':
         uname=request.POST.get('uname')
         username=registeredUser.objects.filter(username=uname).get()
         email=request.POST.get('email')
         category=request.POST.get('category')
         print(username,email,category)
        
         campaign =campaignTbl(username=username,email=email,category=category)
         campaign.save()
        
         print("data saved")
         return redirect('/') 
     
    return render(request,'campaign.html')

def fundraiseView(request):
    if request.method == 'POST':
        uname=request.POST.get('uname')
        username=registeredUser.objects.filter(username=uname).get()
        freq=request.POST.get('freq')
        category=request.POST.get('category')
        amount=request.POST.get('amount')
        print(username,freq,category,amount)
        
        fund =fundraiseTbl(username=username,freq=freq,category=category,amount=amount)
        fund.save()
        
        print("data saved")
        return redirect('/')
    return render(request,'fundraise.html')

def volunteerView(request):
    if request.method == 'POST':
        uname=request.POST.get('uname')
        username=registeredUser.objects.filter(username=uname).get()
        freq=request.POST.get('freq')
        #dtype=request.POST.get('dtype')
        category=request.POST.get('category')
        #amount=request.POST.get('amount')
        print(username,freq,category)
        
        volunteer = volunteertbl(username=username,freq=freq,category=category)
        volunteer.save()
        
        print("data saved")
        return redirect('/')
    
    return render(request,'volunteer.html')

def contactView(request):
    return render(request,'contact.html')

def galleryView(request):
    return render(request,'gallery.html')


def registerPage(request):
    if request.method == 'POST':
        fullname=request.POST.get('fullname')
        username=request.POST.get('username')
        email=request.POST.get('email')
        phonenumber=request.POST.get('phonenumber')
        password=request.POST.get('password')
        print(fullname,username,email,phonenumber,password)
        register=registeredUser(name=fullname,username=username,email=email,phone_number=phonenumber,password=password)
        register.save()
        return redirect('/')
    return render(request,'registration.html')


def login(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        reguser = registeredUser.objects.get(username=username)
        print(reguser,username,password)
        if reguser.password == password:            
            return redirect('/')
        if reguser is None:
            return redirect('/login')
    return render(request,'loginuser.html')
    
def messageView(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        message=request.post.get('message')
        print(username,email,message)
        msg=messagetbl(username=username,email=email,message=message)
        msg.save()
        return redirect('/')
    return render(request,'contact.html')

def adminView(request):      
    return render(request,'adminLogin.html')

def adminRegView(request):
    reg=registeredUser.objects.all()
    return render(request,'adminRegister.html',{'reg':reg})

def adminDonateView(request):
    donate=donateTbl.objects.all()
    return render(request,'adminDonate.html',{'donate':donate})

def adminFundView(request):
    fund=fundraiseTbl.objects.all()
    return render(request,'adminFundraise.html',{'fund':fund})

def adminCampView(request):
    camp=campaignTbl.objects.all()
    return render(request,'adminCampaign.html',{'camp':camp})

def adminVolView(request):
    vol=volunteertbl.objects.all()
    return render(request,'adminVolunteer.html',{'vol':vol})

def adminLoginPageView(request):
    try:
        if request.method =='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = User.objects.get(username=username)
            print(user,username,password)
            if user.password == password:            
                return redirect('/adminLogin')
            elif user.username!=username or user.password!=password:
                return redirect('/adminLg')
            elif user is None:
                return redirect('/adminLg')
    except:
        pass
    return render(request,'adminLogin.html')
