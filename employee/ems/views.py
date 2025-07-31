from django.shortcuts import render,redirect
from .models import Employee
# Create your views here.
def home(request):
    return render(request, 'home.html')
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})
def employee_create(request):
    if request.method == 'POST':
        Employee.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            department=request.POST['department'],
            designation=request.POST['designation'],
            salary=request.POST['salary'],
            date_of_hire = request.POST['date_of_hire'],
            employment_type = request.POST['employment_type'],
            address=request.POST['address'],
            active_status=bool(request.POST['active_status']),
        )
        return redirect('employee_list')
    else:
        return render(request, 'employee_form.html')
def employee_edit(request, id):
    employee = Employee.objects.get(id=id)
    if request.method == 'POST':
        employee.name = request.POST['name']
        employee.email = request.POST['email']
        employee.phone = request.POST['phone']
        employee.department = request.POST['department']
        employee.designation = request.POST['designation']
        employee.salary = request.POST['salary']
        employee.date_of_hire = request.POST['date_of_hire']
        employee.employment_type = request.POST['employment_type']
        employee.address = request.POST['address']
        employee.active_status = request.POST['active_status']
        employee.save()
        return redirect('employee_list')
    else:
        return render(request, 'employee_edit.html', {'employee': employee})
def employee_delete(request, id):
    employee = Employee.objects.get(id=id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    else:
        return render(request, 'employee_delete.html', {'employee': employee})