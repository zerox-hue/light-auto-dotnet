import subprocess
from colorama import Fore

cd = "./"
type_project = ["webapi", "webapiaot", "console", "webapp", "razor", "mvc", "blazor", "blazorwasm", "web", "classlib", "razorclasslib", "class", "razorcomponent", "apicontroller", "mvccontroller", "record", "enum", "interface", "mstest-playwright", "mstest", "viewimports", "viewstart", "nunit-test", "nunit", "nunit-playwright", "page", "grpc", "worker", "struct", "structure", "view", "xunit"]

def define_cd(new_cd:str):
    global cd
    cd = new_cd

def create_dotnet_project(type:str):
    if type not in type_project:
        print(Fore.YELLOW + "The type isn't a type for create a dotnet project type")
        return
    try:
        project = subprocess.run(["dotnet","new",type],cwd=cd,capture_output=True,text=True)
        print(Fore.MAGENTA + project.stdout)
    except Exception as exception:
        print(Fore.YELLOW + str(exception))

def build_project():
    try:
        response = subprocess.run(["dotnet","build"],capture_output=True,text=True,cwd=cd)
        print(Fore.MAGENTA + response.stdout)
    except Exception as exception:
        print(Fore.YELLOW + str(exception))

def run_project():
    try:
        response = subprocess.run(["dotnet","run"],capture_output=True,text=True,cwd=cd)
        print(Fore.MAGENTA + response.stdout)
    except Exception as exception:
        print(Fore.YELLOW + str(exception))