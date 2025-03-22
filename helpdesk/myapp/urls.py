
from django.urls import path
from.import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('base/',views.Basepage,name='basepage'),
    path('login/',views.Loginview,name='loginpage'), 
    path('logout/',views.Logoutview,name='logoutpage'),
    path('register/',views.Registerview,name='registerpage'),
    path('changepassword/',views.Change_Password,name='changepasswordpage'),
    path('UserProfile/',views.User_Profile,name='userprofilepage'),
    path('updateprofile/<int:pk>',views.Update_Profile,name='updateprofilepage'),
    path('taskdetails/',views.TaskDetail,name='taskdetailspage'),
    path('taskinfo/<int:pk>',views.Taskinfo,name='taskinfopage'),
    path('updatetask/<int:pk>',views.Updatetask,name='updatetaskpage'),
    path('deletetask/<int:pk>',views.Deletetetask,name='deletetaskpage'),
    path('accepttask/<int:pk>',views.Accepttask,name='accepttaskpage'),
    path('mycart/',views.Mycarts,name='mycartpage'),
    path('removetask/<int:pk>',views.Removetask,name='removetaskpage'),
    path('closetask/<int:pk>',views.Closedtask,name='closetaskpage'),
    path('reopentask/<int:pk>',views.Reopentask,name='reopentaskpage'),
    path('resolvetask/<int:pk>',views.Resolvetask,name='resolvetaskpage'),
    path('account/',views.AccountDetail,name='accountpage'),
    path('transaction', views.Transactions,name='transactionpage'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]