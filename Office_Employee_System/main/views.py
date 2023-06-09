import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import employee
from django.db.models import Q


def index(response):
    return render(response, "main/index.html", {})


def view_all(response):
    emps = employee.objects.all()
    return render(response, "main/view_all.html", {"emps": emps})


def add_emp(response):
    if response.method == "POST":
        first_name = response.POST.get("first_name")
        last_name = response.POST.get("last_name")
        dept = response.POST.get("dept")
        role = response.POST.get("role")
        salary = response.POST.get("salary")
        bonus = response.POST.get("bonus")
        phone = response.POST.get("phone")
        hire_date = datetime.date.today()
        emp = employee(first_name=first_name, last_name=last_name, dept_id=dept, role_id=role, salary=salary,
                       bonus=bonus, phone=phone, hire_date=hire_date)
        emp.save()
        return HttpResponse("<h1>Employee Added Successfully</h1>")
    else:
        return render(response, "main/add_emp.html", {})


def remove_emp(response):
    emps = employee.objects.all()
    if response.method == "POST":
        if response.POST.get("delete"):
            for emp in emps:
                if response.POST.get("c" + str(emp.id)) == "clicked":
                    emp.delete()

        return redirect("/remove_emp")

    else:
        return render(response, "main/remove_emp.html", {"emps": emps})


def filter_emp(response):
    if response.method == "POST":
        name = response.POST.get("name")
        dept = response.POST.get("dept")
        role = response.POST.get("role")
        emps = employee.objects.all()

        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name__icontains=dept)
        if role:
            emps = emps.filter(role__name__icontains=role)

        return render(response, "main/view_all.html", {"emps": emps})

    else:
        return render(response, "main/filter_emp.html", {})


def update_emp(response):
    if response.method == "POST":
        if response.POST.get("search"):
            first_names = response.POST.get("first_names")
            last_names = response.POST.get("last_names")
            emps = employee.objects.all()
            emps = emps.filter(first_name__icontains=first_names, last_name__icontains=last_names)
            return render(response, "main/update.html", {"emps": emps})

        if response.POST.get("save"):
            first_name = response.POST.get("first_name")
            last_name = response.POST.get("last_name")
            dept = response.POST.get("dept")
            role = response.POST.get("role")
            salary = response.POST.get("salary")
            bonus = response.POST.get("bonus")
            phone = response.POST.get("phone")
            hire_date = response.POST.get("hire_date")
            emps = employee.objects.all()
            if hire_date == "":
                emps.filter(first_name=first_name, last_name=last_name).update(dept_id=dept, role_id=role,
                                                                               salary=salary, bonus=bonus, phone=phone)
            else:
                emps.filter(first_name=first_name, last_name=last_name).update(dept_id=dept, role_id=role,
                                                                               salary=salary, bonus=bonus, phone=phone,
                                                                               hire_date=hire_date)

            return redirect("/view_all")

    else:
        return render(response, "main/update.html", {})
