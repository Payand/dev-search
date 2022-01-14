from django.shortcuts import redirect, render
from .models import Project
from .forms import ProjectForm




def projects(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'project/projects.html',context)

def singleProject(request, pk):
    projectObj = Project.objects.get(id=pk)
    context = {'projectObj': projectObj}
    return render(request, 'project/single-project.html', context)


def addProject(request):
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
        
    context = {'form':form}
    return render(request, 'project/project-form.html', context)    



def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    
    if request.method == "POST":
        form = ProjectForm(request.POST , instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context={"form":form}
    return render (request,'project/project-form.html', context)    
        
def deleteProject(request,pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect('projects')
    context={'object': project}
    return render (request, 'project/project-delete.html', context)              