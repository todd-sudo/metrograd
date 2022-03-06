from django.urls import path

from .views import (
    TenantTaskListView,
    TenantTaskDetailView,
    TenantTaskCreateView,
    TenantTaskDestroyView,
)


urlpatterns = [
    path(
        "tenant/<str:user__username>/tasks",
        TenantTaskListView.as_view(),
        name="tenant"
    ),
    path(
        "tenant/<str:user__username>/",
        TenantTaskDetailView.as_view(),
        name="task"
    ),
    path("tenant/<str:user__username>/create-task/", TenantTaskCreateView.as_view(), name="task_create"),
    path("tenant/<str:user__username>/delete-task/", TenantTaskDestroyView.as_view(), name="task_delete"),

]

