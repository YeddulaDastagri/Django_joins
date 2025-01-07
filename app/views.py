from django.shortcuts import render
from django.http import HttpResponse 
from app.models import *

# Create your views here.  

def empdepno(request):
    LEDO=Emp.objects.select_related('dpt_no').all() 
    LEDO=Emp.objects.select_related('dpt_no','mgr').all()    
    LEDO=Emp.objects.select_related('dpt_no','mgr').filter(mgr__isnull=True)   
    LEDO=Emp.objects.select_related('dpt_no','mgr').filter(job='clerk') 
    LEDO=Emp.objects.select_related('dpt_no','mgr').filter(dpt_no__dname='accounting')   
    LEDO=Emp.objects.select_related('dpt_no','mgr').filter(sal__gt=5000,ename='rajesh')   
    LEDO=Emp.objects.select_related('dpt_no','mgr').filter(Q(ename='ravi')|Q(sal__gt=1000))   
    LEDO=Emp.objects.select_related('dpt_no','mgr').filter(Q(ename='raju')&Q(sal__lt=10000))   
    d={'LEDO':LEDO}
    return render(request,'empdepno.html',d)
def depempdatapr(request):
    LDEO=Dpt.objects.prefetch_related('emp_set').all() 
    print(LDEO) 
    d={'LDEO':LDEO} 
    return render(request,'depempdatapr.html',d)
