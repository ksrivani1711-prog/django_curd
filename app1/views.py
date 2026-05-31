from django.shortcuts import render
from app1.models import employee

def emp_details(request):
    data = employee.objects.all()

    context = {
        'data': data
    }

    return render(request, "app1_template/home.html", context)