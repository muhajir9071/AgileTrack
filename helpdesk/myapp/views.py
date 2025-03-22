from django.shortcuts import render,redirect,get_object_or_404
from.forms import LoginForm,RegisterForm,UserProfileForm,TaskDetailsForm, AccountForm
from django.contrib.auth import authenticate, login,logout, update_session_auth_hash
from django.contrib import messages
from.models import UserProfile,TaskDetails,Mycart,User,Account,Transaction
from django.contrib.auth.forms import PasswordChangeForm
from django.utils import timezone
from django.db.models import Q



# Create your views here.
def Basepage(request):
    if request.user.is_authenticated:
       Taskdatas=TaskDetails.objects.all()
       return render(request,'Base.html',{'Taskdatas':Taskdatas})
    else:
        messages.error(request, 'You must be logged in to create a task.')
        return redirect('loginpage')
   

def Loginview(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid(): 
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,'successfully login')
                return redirect('basepage')
            else:
                messages.error(request,'username or password invalid')
                return render(request,'Login.html',{'form':form})
    else:
        form = LoginForm()

    return render(request, 'login.html',{'form':form})

def Logoutview(request):
    logout(request)
    messages.success(request,'logout successfully ')
    return redirect('loginpage')
#Registerview
def Registerview(request):
    if request.method =='POST':
        Register_form=RegisterForm(request.POST)
        UserProfile_form=UserProfileForm(request.POST)
        if Register_form.is_valid() and UserProfile_form.is_valid():
           Registerform= Register_form.save()
           User_Profile=UserProfile_form.save(commit=False)
           Address=UserProfile_form.cleaned_data['Address']
           City=UserProfile_form.cleaned_data['City']
           State=UserProfile_form.cleaned_data['State']
           profile=UserProfile(User=Registerform,Address=Address,City=City,State=State)
           profile.save()
           messages.success(request,"You have been Register succesfully!")
           return redirect('loginpage')
        else:
            messages.error(request,"You have not enter correct data! ") 
            return redirect('registerpage')
    else:
        Register_form=RegisterForm()
        UserProfile_form=UserProfileForm()
        return render(request,'Register.html',{'Register_form':Register_form,'UserProfile_form':UserProfile_form})    
 #Change_Password
def Change_Password(request):
    if request.method=='POST':
     fm=PasswordChangeForm(user=request.user,data=request.POST)  
     if fm.is_valid():
          fm.save()
          update_session_auth_hash(request,fm.user)
          messages.success(request,'Your password has be changed succesfully') 
          return redirect('basepage')  
    else:
       fm=PasswordChangeForm(user=request.user)
    return render (request,'Change_Password.html',{'fm':fm})     
#User_profile
def User_Profile(request):
    if request.user.is_authenticated:
        user=request.user
        AccountDatas=Account.objects.filter( ACCOUNT_HOLDER=user)
        ProfileDatas=UserProfile.objects.filter(User=user)
        return render(request,'Userprofile.html',{'ProfileDatas':ProfileDatas,'AccountDatas': AccountDatas})
    else:
        messages.success(request,'You must have to be login to see profile')
        return redirect('loginpage')
#update_Profile
def Update_Profile(request,pk):
    if request.user.is_authenticated:
        ProfileDatas=UserProfile.objects.get(id=pk)
        form=UserProfileForm(request.POST or None, instance= ProfileDatas)
        if form.is_valid():
            form.save()
            messages.success(request,'Your profile updated succesfully') 
            return redirect('userprofilepage')  
        return render(request,'Update_Profile.html',{'form':form})
    else:
        messages.success(request,'You must have to be login to see updateprofile')
        return redirect('loginpage')

#Task creation Function
def TaskDetail(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TaskDetailsForm(request.POST)
            if form.is_valid():
                Task = form.save(commit=False)
                Task.TASK_CREATED= request.user
                Task.save()
                messages.success(request, 'Your task was created successfully!')
                return redirect('basepage')  # Redirect only if the form is valid
            else:
                # Display form errors to the user
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"{field}: {error}")
        else:
            form = TaskDetailsForm()  # Empty form for GET requests

        # Render the form (with errors, if any)
        return render(request, 'TaskDetails.html', {'form': form})
    else:
        messages.error(request, 'You must be logged in to create a task.')
        return redirect('loginpage')
#Task information
def Taskinfo(request,pk):
    if request.user.is_authenticated:
        taskinfos=TaskDetails.objects.get(id=pk)
        return render(request,'Taskinfo.html',{'taskinfos':taskinfos})
    else:
        messages.error(request, 'You must be logged in to see  task.')
        return redirect('loginpage')

#update Task
def Updatetask(request,pk):
    if request.user.is_authenticated:
        UpdateDatas=TaskDetails.objects.get(id=pk)
        form=TaskDetailsForm(request.POST or None, instance=UpdateDatas )
        if form.is_valid():
            form.save()
            messages.success(request,'Your Task updated succesfully') 
            return redirect('basepage')  
        return render(request,'Updatetask.html',{'form':form})
    else:
        messages.success(request,'You must have to be login to  update task')
        return redirect('loginpage')
#Delete Task
def Deletetetask(request,pk):
    if request.user.is_authenticated:
        TaskDatas=TaskDetails.objects.get(id=pk)
        TaskDatas.delete()
        messages.success(request,'Your Task Delete succesfully') 
        return redirect('basepage')  
    else:
        messages.success(request,'You must have to be login to  Delete task')
        return redirect('loginpage')
#Accept task    
def Accepttask(request,pk):
    if request.user.is_authenticated:
        Currentuser=request.user
        TaskDatas=TaskDetails.objects.get(id=pk)
        TaskDatas.TASK_STATUS='Inprocess'
        TaskDatas.save()
        Mycart(user=Currentuser,task=TaskDatas).save()
        messages.success(request,'Your Acept Task succesfully') 
        return redirect('basepage')  
    else:
        messages.success(request,'You must have to be login to  Acept task')
        return redirect('loginpage')
#MY cart view
def Mycarts(request):
    if request.user.is_authenticated:
        Currentuser = request.user
        carts = Mycart.objects.filter(user=Currentuser)
        return render(request, 'Mycart.html', {'carts': carts})  # ✅ Fix: Use 'carts', not 'cart'
    else:
        messages.error(request, 'You must be logged in to view your cart.')
        return redirect('loginpage')
#Remove Task 
def Removetask(request,pk):
    if request.user.is_authenticated:
        TaskDatas=TaskDetails.objects.get(id=pk)
        TaskDatas.TASK_STATUS='Open'
        TaskDatas.save()
        mycart= Mycart.objects.filter(task=pk)
        mycart.delete()
        messages.success(request,'Your Remove  Task succesfully') 
        return redirect('basepage')  

    else:
        messages.success(request,'You must have to be login to  Remove  task')
        return redirect('loginpage')
#closed Task
def Closedtask(request,pk):
    if request.user.is_authenticated:
        Currentuser= request.user
        TaskDatas=TaskDetails.objects.get(id=pk)
        TaskDatas.TASK_STATUS='Closed'
        TaskDatas.TASK_CLOSED=Currentuser
        TaskDatas.TASK_CLOSED_ON=timezone.now()
        TaskDatas.save()
        mycart= Mycart.objects.filter(task=pk)
        mycart.delete()
        messages.success(request,'Your Close  Task succesfully') 
        return redirect('basepage')  

    else:
        messages.success(request,'You must have to be login to  Close  task')
        return redirect('loginpage')
#Reopen task
def Reopentask(request,pk):
    if request.user.is_authenticated:
        TaskDatas=TaskDetails.objects.get(id=pk)
        TaskDatas.TASK_STATUS='Reopen'
        holder=User.objects.get(username=TaskDatas.TASK_CLOSED)
        TaskDatas.save()
        Mycart(user=holder,task=TaskDatas).save()
        messages.success(request,'Your Acept Reopen succesfully') 
        return redirect('basepage')  
    else:
        messages.success(request,'You must have to be login to  Reopen task')
        return redirect('loginpage')
#Resolve Task
def Resolvetask(request,pk):
    if request.user.is_authenticated:
        TaskDatas=TaskDetails.objects.get(id=pk)
        TaskDatas.TASK_STATUS='Resolved'
        TaskDatas.save()
        creater=get_object_or_404(Account,ACCOUNT_HOLDER=TaskDatas.TASK_CREATED)
        resolver=get_object_or_404(Account,ACCOUNT_HOLDER=TaskDatas.TASK_CLOSED)
        if creater.ACCOUNT_BALANCE >= TaskDatas.TASK_REWARD:
            creater.ACCOUNT_BALANCE -= TaskDatas.TASK_REWARD
            creater.save()
            resolver.ACCOUNT_BALANCE += TaskDatas.TASK_REWARD
            resolver.save()
            Transaction.objects.create(sender=TaskDatas.TASK_CREATED,reciver=TaskDatas.TASK_CLOSED,amount=TaskDatas.TASK_REWARD)
            messages.success(request,'Your Acept Resolved succesfully') 
            return redirect('basepage')  
        
    else:
        messages.success(request,'You must have to be login to  Resolve task')
        return redirect('loginpage')

#Account Function
def AccountDetail(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form =AccountForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'coin added successfully!')
                return redirect('basepage')  # Redirect only if the form is valid
        else:
            form = AccountForm()  # Empty form for GET requests
            return render(request, 'Account.html', {'form': form})
    else:
        messages.error(request, 'You must be logged in to add coin.')
        return redirect('loginpage')
#Transaction
def Transactions(request):
    if request.user.is_authenticated:
        user=request.user
        Transactions=Transaction.objects.filter(Q(sender=user)|Q(reciver=user))
        return render(request,'Transaction.html',{'Transactions':Transactions})
    else:
       messages.success(request,"You must have to login to see Transaction!")
       return redirect('login')
    

