from django.shortcuts import get_object_or_404, redirect, render
from .models import Employee
from .forms import EmployeeForm

# Create your views here.


def list(request):
    employees = Employee.objects.all()
    return render(request, "crud/list.html", {"employees": employees})


def detail(request, id):
    employee = get_object_or_404(Employee, id=id)
    return render(request, "crud/detail.html", {"employee": employee})


def create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("fbv:list")
    else:
        form = EmployeeForm()

    return render(request, "crud/create.html", {"form": form})

def edit(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('fbv:detail', id=employee.id)
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'crud/edit.html', {"form": form, "employee": employee})

def delete(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == "POST":
        employee.delete()
        return redirect('fbv:list')
    return render(request, 'crud/delete.html', {"employee":employee})
