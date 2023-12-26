from django.urls import path
from .views import Index, Task_edit, Task_delete, Task_Create


urlpatterns = [
    path("", Index, name="list"),
    path("create/", Task_Create, name="create"),
    path("update/<int:pk>/", Task_edit, name="edit"),
    path("delete/<int:pk>/", Task_delete, name="delete"),
]
