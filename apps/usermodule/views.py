from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Address
from django.db.models import Q
from django.db.models import Count, Min, Max, Sum, Avg


# Create your views here.
def task6(request):
    objs = Student.objects.values('address__city').annotate(num_students=Count('id'))
    return render(request, 'usermodule/task6.html', {'objs': objs})