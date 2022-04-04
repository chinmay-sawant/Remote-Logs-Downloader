from http.client import HTTPResponse
import shutil
from django.shortcuts import render,redirect
import json
import os
from datetime import datetime

f = open('config.json')
data = json.load(f)
projectName=data["projectName"]
projectPass=data["projectPass"]
pathToShare=data["pathToShare"]
keyword=data["keyword"]

# Create your views here.
from django.http import FileResponse, HttpResponse,HttpResponseRedirect


def index(request):
    #request.session.flush()
    projectName=""
    projectName=data["projectName"]    
    return render(request, 'template.html', locals())


def checkIT(request):
    username=request.POST.get('email')
    password=request.POST.get('password')
    if username==f"{projectName}" and password==f"{projectPass}":
        request.session["username"]=username
        request.session["password"]=password
        return redirect("/dirTraverser/SharedPath/")
        #return HttpResponse(f"Inside Checkit \n Welcome User : {username} with {password}")
        
    else:
        return HttpResponse(f"Wrong User Credentials ...")


def SharedPath(request):
    try:
        if request.session["username"]:
            logsPaths=[]
          
            for root, dirs, files in os.walk("D:\\installers\\apache-tomcat-9.0.10_TNTRB"):
                for file in files:
                    if f"{keyword}" in file:
                        cDir=os.path.join(root, file)
                        print(cDir)
                        logsPaths.append(f"{cDir}")
            
        
            return render(request, 'SharedPath.html', locals())
    except KeyError:
        return redirect("/dirTraverser/")

def downloadLog(request):
    try:
        if request.session["username"]:
            logPath=request.POST.get('cLogPath')
            now=datetime.now()
            timestamp=now.strftime("%d_%m_%Y_%H_%M_%S")
            print("Selected Log Path",f"{logPath}")
            if os.path.exists("./ZipFiles/"):
                pass
            else:
                os.makedirs("./ZipFiles/")

            os.makedirs(f"./ZipFiles/{timestamp}")
            cTimeStamppath=os.path.join(os.path.abspath("."),"ZipFiles",timestamp)
            shutil.copy(logPath,cTimeStamppath)
            os.system(f"7z a -mx=9 .\ZipFiles\{timestamp}.zip {cTimeStamppath} -sdel")
            czipFile = open(f'{cTimeStamppath}.zip', 'rb')
            response = FileResponse(czipFile)
            return response
            #return HttpResponse(f"Check Console ...")

    except KeyError:
        return redirect("/dirTraverser/")

