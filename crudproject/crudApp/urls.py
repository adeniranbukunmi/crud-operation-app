from django.urls import path, include
from crudApp import views as vs

urlpatterns = [
path("", vs.index, name="index"),
path("insert", vs.insertdata, name="insertdata"),
path("update/<id>", vs.updateData, name="updateData"),
path("delete/<id>", vs.deleteData, name="deleteData"),
]
