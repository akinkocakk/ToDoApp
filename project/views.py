from django.shortcuts import render, redirect

# Create your views here.

from .models import ToDo
from .forms import ToDoForm

def Index(request):
    qs = ToDo.objects.all()
    context = {
        "object": qs 
    }
    return render(request, "project/index.html", context)




def Task_Create(request):
    to_do = ToDo.objects.all()
    form = ToDoForm
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    context = {
        "to_do": to_do,
        "form" : form
    }
    return render(request, "project/create.html", context)


def Task_edit(request, pk):
    qs = ToDo.objects.get(id=pk)
    form = ToDoForm(instance=qs)
    if request.method == "POST":
        form = ToDoForm(request.POST, instance=qs)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        "form":form
    }
    return render(request, "project/update.html", context)


def Task_delete(request, pk):
    qs = ToDo.objects.get(id=pk)
    if request.method == "POST":
        qs.delete()
        return redirect("/")
    context = {
        "qs": qs
    }
    return render(request, "project/delete.html", context)