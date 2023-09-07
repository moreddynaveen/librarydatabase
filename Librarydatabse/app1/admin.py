from django.contrib import admin
from app1.models import Student
class Studentadmin(admin.ModelAdmin):
    list_display=('id','sno','sname','sbranch','smob','bookname','bookno')
admin.site.register(Student,Studentadmin)
# Register your models here.
