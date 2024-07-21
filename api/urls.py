from django.urls import path, include
from .views import (
    UserListCreate,
    UserRetrieveUpdateDelete,
    AppDetailsListCreate,
    AppDetailsRetrieveUpdateDelete,
    TaskDetailListCreate,
    TaskDetailRetrieveUpdateDelete,
)

# Define the URL patterns for the API endpoints
urlpatterns = [
    path("user/", UserListCreate.as_view(), name="UserCreate"),  # Endpoint to list and create users
    path("user/<int:pk>", UserRetrieveUpdateDelete.as_view(), name="UserModify"), # Endpoint to retrieve, update, and delete a specific user
    path("app/", AppDetailsListCreate.as_view(), name="AppDetailsCreate"), # Endpoint to list and create app details
    path(
        "app/<int:pk>",
        AppDetailsRetrieveUpdateDelete.as_view(),
        name="AppDetailsModify",
    ), # Endpoint to retrieve, update, and delete a specific app detail
    path("quest/", TaskDetailListCreate.as_view(), name="TaskDetailCreate"), # Endpoint to list and create task details
    path(
        "quest/<int:pk>",
        TaskDetailRetrieveUpdateDelete.as_view(),
        name="TaskDetailModify",
    ), # Endpoint to retrieve, update, and delete a specific task detail
]
