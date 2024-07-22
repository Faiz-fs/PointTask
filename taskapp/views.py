from django.shortcuts import render, redirect
import httpx
from django.conf import settings

# Create your views here.

# View to render the login page
def index(request):
    return render(request, "login.html")

# View to render the home page with user and app data
async def home(request, usr):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{settings.API_URL}/app/", timeout=30.0)
            userrep = await client.get(f"{settings.API_URL}/user/{usr}", timeout=30.0)
            return render(
                request, "home.html", {"data": response.json(), "userdata": userrep.json()}
            )
        except httpx.ReadTimeout:
            return render(request, "error.html", {"message": "Request timed out."})

# View to render the user profile page
async def profile(request, usr):
    async with httpx.AsyncClient() as client:
        try:
            userrep = await client.get(f"{settings.API_URL}/user/{usr}", timeout=30.0)
            return render(request, "profile.html", {"userdata": userrep.json()})
        except httpx.ReadTimeout:
            return render(request, "error.html", {"message": "Request timed out."})

# View to render the user points page
async def point(request, usr):
    async with httpx.AsyncClient() as client:
        try:
            userrep = await client.get(f"{settings.API_URL}/user/{usr}", timeout=30.0)
            return render(request, "point.html", {"userdata": userrep.json()})
        except httpx.ReadTimeout:
            return render(request, "error.html", {"message": "Request timed out."})

# View to render the task page with user tasks
async def task(request, usr):
    async with httpx.AsyncClient() as client:
        try:
            userrep = await client.get(f"{settings.API_URL}/user/{usr}", timeout=30.0)
            taskdata = await client.get(f"{settings.API_URL}/quest/", timeout=30.0)
            appdata = await client.get(f"{settings.API_URL}/app/", timeout=30.0)
            app = []
            data = []
            for val in taskdata.json():
                if val["userid"] == usr:
                    app.append(val["appid"])
            for val in appdata.json():
                if val["appid"] in app:
                    data.append(val)
            return render(request, "task.html", {"userdata": userrep.json(), "taskdata": data})
        except httpx.ReadTimeout:
            return render(request, "error.html", {"message": "Request timed out."})

# View to render the admin login page
def administrator(request):
    return render(request, "admin.html")

# View to render the add app page
def addapp(request):
    return render(request, "addapp.html")

# View to render the app details page
async def details(request, id, usr):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{settings.API_URL}/app/{id}", timeout=30.0)
            userrep = await client.get(f"{settings.API_URL}/user/{usr}", timeout=30.0)
            return render(
                request, "details.html", {"data": response.json(), "userdata": userrep.json()}
            )
        except httpx.ReadTimeout:
            return render(request, "error.html", {"message": "Request timed out."})

# View to pass data to another page
async def passdata(request, id, usr):
    if request.method == "POST":
        img = request.FILES.get("img")
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(f"{settings.API_URL}/app/{id}", timeout=30.0)
                userrep = await client.get(f"{settings.API_URL}/user/{usr}", timeout=30.0)
                usrdata = userrep.json()
                appdata = response.json()
                usrdata["points"] += appdata["points"]
                print(usrdata)
                taskdata = {"appid": id, "userid": usr, "taskname": appdata["appName"]}
                taskfile = {"appIcon": img}
                userpost = await client.put(f"{settings.API_URL}/user/{usr}", data=usrdata, timeout=30.0)
                taskpost = await client.post(
                    f"{settings.API_URL}/quest/", data=taskdata, files=taskfile, timeout=30.0
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
            except httpx.ReadTimeout:
                return render(request, "error.html", {"message": "Request timed out."})

# View to handle user sign-up
def signin(request):
    return render(request, "sign.html")

# View to handle adding a new user
async def adduser(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        data = {"name": name, "email": email, "password": password, "points": 50}
        async with httpx.AsyncClient() as client:
            try:
                userrep = await client.post(f"{settings.API_URL}/user/", data=data, timeout=30.0)
                if userrep.status_code == 201:
                    return redirect("Index")
                else:
                    return render(request, "sign.html", {"error": userrep.json()})
            except httpx.ReadTimeout:
                return render(request, "error.html", {"message": "Request timed out."})

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
async def update(request):
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
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(f"{settings.API_URL}/app/", data=data, files=files, timeout=30.0)
                if response.status_code == 201:
                    return redirect("AddApp")
                else:
                    return render(request, "addapp.html", {"error": response.json()})
            except httpx.ReadTimeout:
                return render(request, "error.html", {"message": "Request timed out."})

# View to handle user login
async def login(request):
    if request.method == "POST":
        user = request.POST.get("User")
        pswd = request.POST.get("Pswd")
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(f"{settings.API_URL}/user/", timeout=30.0)
                for val in response.json():
                    if val["email"] == user and val["password"] == pswd:
                        return redirect("Home", usr=val["userid"])
                else:
                    return render(
                        request, "login.html", {"error": "Invalid username and password"}
                    )
            except httpx.ReadTimeout:
                return render(request, "error.html", {"message": "Request timed out."})
