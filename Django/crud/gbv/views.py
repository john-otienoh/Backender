from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from .models import Employee
from .forms import EmployeeForm


# Create your views here.
class EmployeeListView(ListView):
    model = Employee
    template_name = "crud/list.html"
    context_object_name = "employees"


class EmployeeCreateView(CreateView):
    model = Employee
    template_name = "crud/create.html"
    form_class = EmployeeForm
    success_url = reverse_lazy("gbv:list")


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = "crud/detail.html"
    context_object_name = "employee"


class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = "crud/edit.html"
    success_url = reverse_lazy("gbv:detail")
    context_object_name = "employee"

    def get_success_url(self):
        return reverse_lazy("gbv:detail", kwargs={"pk": self.object.pk})


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = "crud/delete.html"
    success_url = reverse_lazy("gbv:list")
