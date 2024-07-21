from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .views import (
    home,
    profile,
    point,
    task,
    access,
    administrator,
    addapp,
    update,
    details,
    index,
    login,
    signin,
    adduser,
    passdata,
)


# Define the URL patterns for the taskapp views
urlpatterns = [
    path("", index, name="Index"),  # Home page route
    path("home/<int:usr>", home, name="Home"),  # Home page route with user ID
    path(
        "profile/<int:usr>", profile, name="Profile"
    ),  # Profile page route with user ID
    path("point/<int:usr>", point, name="Point"),  # Points page route with user ID
    path("task/<int:usr>", task, name="Task"),  # Task page route with user ID
    path("access/", access, name="Access"),  # Admin access route
    path("appadmin/", administrator, name="AppAdmin"),  # Admin page route
    path("addapp/", addapp, name="AddApp"),  # Add app page route
    path("update/", update, name="Update"),  # Update app route
    path(
        "details/<int:id>/<int:usr>", details, name="Detail"
    ),  # App details page route with app ID and user ID
    path("login/", login, name="Login"),  # Login page route
    path("signin/", signin, name="Signin"),  # Signin page route
    path("adduser/", adduser, name="Adduser"),  # Add user route
    path(
        "passdata/<int:id>/<int:usr>", passdata, name="Passdata"
    ),  # Pass data route with app ID and user ID
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)  # Serve media files during development
