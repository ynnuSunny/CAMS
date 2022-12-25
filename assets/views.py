from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Assets


@login_required
def add_assets(request):
    admin = request.user
    if(admin.role=="EMPLOYEE"):
        return HttpResponse("<h1>You are not authorized user!!!<h1>")
    if request.method=="GET":
        return render(request,"add-assets.html")
    if(request.method == "POST"):
        company_id = admin.company_id
        assets_name = request.POST['assets-name']
        uploaded_file = request.FILES['image']
        fs = FileSystemStorage()   
        image=fs.save(uploaded_file.name, uploaded_file)
        assets = Assets(company_id=company_id,assets_name=assets_name,image=image)
        assets.save()

        return redirect("view-assets")

def view_assets(request):
    return render(request,"view-assets.html")
    