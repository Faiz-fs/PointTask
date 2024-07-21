from django.shortcuts import render, redirect
import requests
from django.conf import settings


# Create your views here.


# View to render the login page
def index(request):
    return render(request, "login.html")


# View to render the home page with user and app data
def home(request, usr):
    response = requests.get(f"{settings.API_URL}/app/")
    # print(response.json())
    userrep = requests.get(f"{settings.API_URL}/user/{usr}")
    # print(userrep.json())
    return render(
        request, "home.html", {"data": response.json(), "userdata": userrep.json()}
    )


# View to render the user profile page
def profile(request, usr):
    userrep = requests.get(f"{settings.API_URL}/user/{usr}")
    return render(request, "profile.html", {"userdata": userrep.json()})


# View to render the user points page
def point(request, usr):
    userrep = requests.get(f"{settings.API_URL}/user/{usr}")
    return render(request, "point.html", {"userdata": userrep.json()})


# View to render the task page with user tasks
def task(request, usr):
    userrep = requests.get(f"{settings.API_URL}/user/{usr}")
    taskdata = requests.get(f"{settings.API_URL}/quest/")
    appdata = requests.get(f"{settings.API_URL}/app/")
    app = []
    data = []
    for val in taskdata.json():
        if val["userid"] == usr:
            app.append(val["appid"])
    for val in appdata.json():
        if val["appid"] in app:
            data.append(val)
    return render(request, "task.html", {"userdata": userrep.json(), "taskdata": data})


# View to render the admin login page
def administrator(request):
    return render(request, "admin.html")


# View to render the add app page
def addapp(request):
    return render(request, "addapp.html")


# View to render the app details page
def details(request, id, usr):
    response = requests.get(f"{settings.API_URL}/app/{id}")
    userrep = requests.get(f"{settings.API_URL}/user/{usr}")
    return render(
        request, "details.html", {"data": response.json(), "userdata": userrep.json()}
    )


# View to pass data to another page
def passdata(request, id, usr):
    if request.method == "POST":
        img = request.FILES.get("img")
        response = requests.get(f"{settings.API_URL}/app/{id}")
        userrep = requests.get(f"{settings.API_URL}/user/{usr}")
        usrdata = userrep.json()
        appdata = response.json()
        usrdata["points"] += appdata["points"]
        print(usrdata)
        taskdata = {"appid": id, "userid": usr, "taskname": appdata["appName"]}
        taskfile = {"appIcon": img}
        userpost = requests.put(f"{settings.API_URL}/user/{usr}", data=usrdata)
        taskpost = requests.post(
            f"{settings.API_URL}/quest/", data=taskdata, files=taskfile
        )
        if userpost.status_code == 200 and taskpost.status_code == 201:
            return redirect("Home", usr)
        else:
            return render(
                request,
                "details.html",
                {
                    "data": appdata,
                    "userdata": usrdata,
                    "taskerror": taskpost.json(),
                    "updaterror": userpost.json(),
                },
            )


# View to handle user sign-up
def signin(request):
    return render(request, "sign.html")


# View to handle adding a new user
def adduser(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        data = {"name": name, "email": email, "password": password, "points": 50}
        userrep = requests.post(f"{settings.API_URL}/user/", data=data)
        if userrep.status_code == 201:
            return redirect("Index")
        else:
            return render(request, "sign.html", {"error": userrep.json()})


# View to handle admin access
def access(request):
    if request.method == "POST":
        user = request.POST.get("User")
        pswd = request.POST.get("Pswd")
        if user == "admin" and pswd == "Admin@123":
            return redirect("AddApp")
        else:
            return render(
                request, "admin.html", {"error": "Invalid username and password"}
            )


# View to handle app updates
def update(request):
    if request.method == "POST":
        name = request.POST.get("name")
        link = request.POST.get("link")
        cat = request.POST.get("Category")
        subcat = request.POST.get("SubCategory")
        point = request.POST.get("point")
        img = request.FILES.get("img")
        print(name, link, cat, subcat, point, img)
        data = {
            "appName": name,
            "appLink": link,
            "appCat": cat,
            "appSubCat": subcat,
            "points": point,
        }
        files = {"appIcon": img}
        response = requests.post(f"{settings.API_URL}/app/", data=data, files=files)
        if response.status_code == 201:
            return redirect("AddApp")
        else:
            return render(request, "addapp.html", {"error": response.json()})


# View to handle user login
def login(request):
    if request.method == "POST":
        user = request.POST.get("User")
        pswd = request.POST.get("Pswd")
        response = requests.get(f"{settings.API_URL}/user/")
        for val in response.json():
            if val["email"] == user and val["password"] == pswd:
                return redirect("Home", usr=val["userid"])
        else:
            return render(
                request, "login.html", {"error": "Invalid username and password"}
            )
