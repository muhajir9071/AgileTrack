from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from.models import UserProfile, TaskDetails,Account


#LoginForm
class LoginForm(forms.Form):
    username=forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

# RegisterForm
class RegisterForm(UserCreationForm):
    first_name=forms.CharField(label='First Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(label='Last Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    username=forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(label='Email Address',widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
#UserProfileForm
class UserProfileForm(forms.ModelForm):
    Address=forms.CharField(label='Address',widget=forms.TextInput(attrs={'class':'form-control'}))
    City =forms.CharField(label=' City',widget=forms.TextInput(attrs={'class':'form-control'}))
    State=forms.CharField(label=' State',widget=forms.TextInput(attrs={'class':'form-control'}))
   

    class Meta:
        model=UserProfile
        fields = ['Address','City', 'State']
   
class TaskDetailsForm(forms.ModelForm):
      TASK_TITLE=forms.CharField(label='Task Title',widget=forms.TextInput(attrs={'class':'form-control'}))
      TASK_DUE_DATE=forms.DateField(label='Task Due Date')
      TASK_REWARD=forms.IntegerField(label='Task Reward')
      TASK_DESCRIPTION=forms.CharField(label='Task Description',widget=forms.TextInput(attrs={'class':'form-control'}))
      
      class Meta:
        model= TaskDetails
        fields = ['TASK_TITLE','TASK_DUE_DATE','TASK_REWARD','TASK_DESCRIPTION']

#AccountForm
class AccountForm(forms.ModelForm):
    ACCOUNT_HOLDER=forms.ModelChoiceField(label='ACCOUNT HOLDER',queryset=User.objects.all())
    ACCOUNT_BALANCE =forms.IntegerField(label='ACCOUNT BALANCE',widget=forms.TextInput(attrs={'class':'form-control'}))
   

    class Meta:
        model=Account
        fields = ['ACCOUNT_HOLDER','ACCOUNT_BALANCE']