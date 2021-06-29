from django.shortcuts import redirect, render,HttpResponse
from tasks.models import *


# Create your views here.
def home(request):
    if request.method=="POST":
        title = request.POST['title']
        ins = Task(title=title)
        ins.save()
        return redirect('/')
    tasks = Task.objects.all()
    context = {'tasks':tasks}
    
        
    return render(request, "list.html",context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    
   
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    

    context={'item':item}
    return render(request,'delete.html',context)
