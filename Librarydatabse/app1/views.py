from django.shortcuts import render
from app1.models import Student
def index(request):
    return render(request,'app1/index.html')
def StdView(request):
    std_list=Student.objects.all()
    my_dict={'std_list':std_list}
    return render(request,'app1/std.html',context=my_dict)
# Create your views here.
