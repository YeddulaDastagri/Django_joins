from django.shortcuts import render
from django.http import HttpResponse 
from app.models import *

# Create your views here.  

def empdepno(request):
    LEDO=Emp.objects.select_related('dpt_no').all()
    d={'LEDO':LEDO}
    return render(request,'empdepno.html',d)

