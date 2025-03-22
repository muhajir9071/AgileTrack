

# Register your models here.
from django.contrib import admin

from .models import UserProfile,TaskDetails,Mycart, Account,Transaction



# Extend the existing UserAdmin to include UserProfile
class UserProfileAdmin(admin.ModelAdmin):
    list_display=['Address','City','State']
admin.site.register(UserProfile,UserProfileAdmin)
#register Taskdetails
class TaskDetailsAdmin(admin.ModelAdmin):
       list_display=['id','TASK_TITLE','TASK_CREATED','TASK_CLOSED','TASK_CREATED_ON','TASK_CLOSED_ON','TASK_DUE_DATE','TASK_REWARD','TASK_DESCRIPTION','TASK_HOLDER','TASK_STATUS']
admin.site.register(TaskDetails,TaskDetailsAdmin)
#register mycart
class MycartAdmin(admin.ModelAdmin):
       list_display=['id','user','task','task_count']
admin.site.register(Mycart,MycartAdmin)

#Account register
class AccountAdmin(admin.ModelAdmin):
       list_display=['id','ACCOUNT_HOLDER','ACCOUNT_BALANCE']
admin.site.register(Account,AccountAdmin)

#Transaction register
class TransactionAdmin(admin.ModelAdmin):
       list_display=['id','sender','reciver','amount','timestamp']
admin.site.register(Transaction,TransactionAdmin)
