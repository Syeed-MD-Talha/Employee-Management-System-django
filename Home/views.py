from django.shortcuts import render,redirect,get_object_or_404
from django.views import View  
from django.http import HttpResponse 
from .models import Employee
from .forms import EmployeeForm
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    total_employee=len(Employee.objects.all())
    return render(request, 'home.html',{'total_employee':total_employee})


class EmployeeList(View):
    def get(self, request):
        
        # for sorting functionality
        sort_by = request.GET.get('sort_by', 'full_name')
        order = request.GET.get('order', 'asc')
        if order == 'asc':
            employees = Employee.objects.all().order_by(sort_by)
        else:
            employees = Employee.objects.all().order_by(f'-{sort_by}')
        
        # for pagination
        paginator = Paginator(employees, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        

        return render(request, 'employee_list.html', {
            'page_obj': page_obj,
            'sort_by': sort_by,
            'order': order,
        })

    

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})


def employee_edit(request, id):
    employee = get_object_or_404(Employee, pk=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'edit_employee.html', {'form': form, 'employee': employee})



def employee_delete(request, id):
    employee = get_object_or_404(Employee, pk=id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})


def search_employee(request):
    queryset=Employee.objects.all()  
    
    # Get search parameters
    name=request.GET.get('name','')  
    date_of_birth=request.GET.get('date_of_birth','')
    email = request.GET.get('email','')
    mobile = request.GET.get('mobile','')
    
    if name:
        queryset=queryset.filter(full_name__icontains=name)
    if date_of_birth:
        queryset=queryset.filter(date_of_birth=date_of_birth)
    if email:
        queryset=queryset.filter(email__icontains=email)
    if mobile:
        queryset=queryset.filter(mobile=mobile)
    
    print(queryset)
    context={'employees':queryset}
    return render(request, 'search_employee.html', context)