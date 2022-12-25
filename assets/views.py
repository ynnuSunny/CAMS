from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Assets,AssetLogs


# add asstes by staff or manager
# empolyee can't add asset
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


#very user can view asset
@login_required
def view_assets(request):
    user = request.user
    assets = Assets.objects.filter(company_id = user.company_id)
    fs = FileSystemStorage()
    allAssets = []
    for i in assets:
        i.image = fs.url(i.image)
        allAssets.append(i)
    context = {
        'assets' : allAssets,
        'role' : user.role
    }
    return render(request,"view-assets.html",context)


# employee send resquest for an asset
@login_required
def request_assets(request):
    if(request.method=="POST"):
        user = request.user
        id = request.POST['id']
        request_reason = request.POST["request_reason"]
        assets = Assets.objects.get(id=id)
        assets.request_reason=request_reason
        assets.request_by = user.id
        assets.save()
        
        #saving product logs
        activity = user.first_name+" request for this Assets"
        logs = AssetLogs(assets_id=id,activity = activity,accept_reason=request_reason)
        logs.save()
        
        return redirect("view-assets")


# staff and manager can view request
@login_required
def view_request(request):
    admin = request.user
    if(admin.role=="EMPLOYEE"):
        return HttpResponse("<h1>You are not authorized user!!!<h1>")
    if request.method=="GET":
        user = request.user
        assets = Assets.objects.filter(company_id = user.company_id).filter(request_by__isnull=False)
        fs = FileSystemStorage()
        allAssets = []
        for i in assets:
            i.image = fs.url(i.image)
            
            allAssets.append(i)

        context = {
            'assets' : allAssets
        }
        return render(request,"view-request.html",context)

    if(request.method == "POST"):
        company_id = admin.company_id
        assets_name = request.POST['assets-name']
        uploaded_file = request.FILES['image']
        fs = FileSystemStorage()   
        image=fs.save(uploaded_file.name, uploaded_file)
        assets = Assets(company_id=company_id,assets_name=assets_name,image=image)
        assets.save()

    
        return redirect("view-assets")



# manager and staff can give permission
@login_required
def assets_persmission(request):
    admin = request.user
    if(admin.role=="EMPLOYEE"):
        return HttpResponse("<h1>You are not authorized user!!!<h1>")

    if(request.method=="POST"):
        manager = request.user

        #this is asset id
        id = request.POST['id']
        if(request.POST['value'] == "ACCEPT"):
            #update Assets Table
            assets = Assets.objects.get(id=id)
            assets.request_accepted_by = manager.id
            assets.save()
            
            #update in Asset Logs Table
            activity = "Request is Accpeted By "+manager.first_name
            logs = AssetLogs(assets_id=id,activity = activity)
            logs.save()


            return redirect("view-request")
        if(request.POST['value'] == "REJECT"):
            #update Assets Table
            assets = Assets.objects.get(id=id)
            assets.request_by = None
            assets.save()
            

            #update in Asset Log Table
            activity = "Request is Rejected By "+manager.first_name
            logs = AssetLogs(assets_id=id,activity = activity)
            logs.save()

            return redirect("view-request")

        if(request.POST['value'] == "RECEIVE"):
            #update Assets Table
            assets = Assets.objects.get(id=id)
            assets.request_accepted_by = None
            assets.request_by = None
            assets.save()
            
            #update in Asset Log Table
            activity = "Asset is Successfully Received by"+manager.first_name
            logs = AssetLogs(assets_id=id,activity = activity)
            logs.save()

            return redirect("view-request")
        


# return assets log to the Company Manager
@login_required
def logs_assets(request):
    manager = request.user
    if(manager.role!="MANAGER"):
        return HttpResponse("<h1>You are not authorized user!!!<h1>")
    if(request.POST):
        #asset id 
        id = request.POST['id']
        logs = AssetLogs.objects.filter(assets_id=id).order_by('-date_of_activity')
        context = {
            'logs':logs
        }
        return render(request,"logs-assets.html",context)
