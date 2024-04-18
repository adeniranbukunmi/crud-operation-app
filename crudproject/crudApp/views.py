from django.shortcuts import render, redirect
from .models import StudentDetails

# Create your views here.
def index(request):
    info=StudentDetails.objects.all()
    return render(request, "index.html", {"data":info})

def insertdata(request):
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        age=request.POST.get("age")
        gender=request.POST.get("gender")
        # detail=[name,email,age, gender]
        query=StudentDetails(name=name,email=email,age=age, gender=gender)
        query.save()
        return redirect("/")
    return render(request, "index.html")

def updateData(request, id):
    if request.method == "POST":
        name=request.POST["name"]
        email=request.POST["email"]
        age=request.POST["age"]
        gender=request.POST["gender"]
        edit=StudentDetails.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.age=age
        edit.gender=gender
        edit.save()
        return redirect("/")

    data=StudentDetails.objects.get(id=id)
    return render(request, "edit.html", {'d':data})

def deleteData(request, id):
        deli=StudentDetails.objects.get(id=id)
        deli.delete()
        return redirect("/")
