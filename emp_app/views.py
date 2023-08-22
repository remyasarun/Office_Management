from django.shortcuts import render, HttpResponse
from .models import Employee

# Create your views here.
def index(request):

    return render(request, 'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context={
        'emps': emps
    }
    print(context)
    return render(request, 'view_all_emp.html',context)



def add_emp(request):
    if request.method == 'POST':
        first = request.POST.get('first')
        last = request.POST.get('last')
        dept = request.POST.get('dept')
        salary = request.POST.get('salary')
        role = request.POST.get('role')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        Employee(First_name=first, Last_name=last, Dept=dept, Salary=salary, Role=role, phone=phone, hire_date=date).save()
        return HttpResponse(" EMPLOYEE DETAILS ADDED SUCCESSFULLY")
    elif request.method =='GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("error occured")


def remove_emp(request, emp_id=0, ):
    if emp_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Details Deleted Successfully")
            pass
        except:
            return HttpResponse("error occured! Details not deleted")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }

    return render(request, 'remove_emp.html', context)

def filter_emp(request):
    if request.method=='POST':
        dept = request.POST.get('dept')
        role = request.POST.get('role')
        emps=Employee.objects.all()

        if dept:
            emps = emps.filter(Dept=dept)
        if role:
           emps = emps.filter(Role=role)

        context = {
            'emps': emps
           }
        return render(request, 'view_all_emp.html', context)

    elif request.method =='GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse("error occured")
