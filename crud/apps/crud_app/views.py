from django.shortcuts import render, redirect
from .models import Code

def index(request):
    newcodes = Code.objects.all() #all of the codes put into an object
    context = {'newcodes': newcodes}
    return render(request, 'crud_app/index.html', context)

def create(request): 
    print (request.POST) 
    newcode = Code(name=request.POST['name'],language=request.POST['language'], codesnippet=request.POST['codesnippet'])
    newcode.save()
    return redirect('/')  

def edit(request, id): 
    newcode = Code.objects.get(id=id) #the second id = the id from (request, id)
    context= {"newcode":  newcode}
    return render(request, 'crud_app/edit.html', context)

def update(request, id): 
    newcode =  Code.objects.get(id=id)
    newcode.name = request.POST['name']
    newcode.language = request.POST['language']
    newcode.codesnippet = request.POST['codesnippet']
    return redirect('/')

def destroy(request, id): 
    newcode = Code.objects.get(id=id) 
    newcode.delete()
    return redirect('/')
