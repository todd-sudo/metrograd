from django.db.models import Prefetch
from rest_framework.authentication import SessionAuthentication, \
    BasicAuthentication
from rest_framework.generics import (
    DestroyAPIView,
    RetrieveAPIView,
    CreateAPIView

)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Task, Tenant
from .serializers import (
    TenantListTaskSerializer,
    TenantDetailTaskSerializer,
    TaskDetailSerializer,
)


class TenantTaskCreateView(CreateAPIView):
    """ Создание заявки пользователя
    """
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer


class TenantTaskListView(RetrieveAPIView):
    """ Вывод списка заявок пользователя
    """
    serializer_class = TenantListTaskSerializer
    lookup_field = "user__username"
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Tenant.objects.filter(
            user__username=self.kwargs[self.lookup_field]
        ).prefetch_related("tasks")
        print(queryset)
        return queryset


class TenantTaskDetailView(RetrieveAPIView):
    """ Детальный вывод заявки пользователя
        http://127.0.0.1:8000/tenant/test_user/create-task/?task_id=2
    """
    serializer_class = TenantDetailTaskSerializer
    lookup_field = "user__username"

    def get_queryset(self, *args, **kwargs):
        task_id = self.request.query_params.get("task_id")
        queryset = Tenant.objects.filter(
            user__username=self.kwargs[self.lookup_field]
        ).prefetch_related(Prefetch("tasks", Task.objects.filter(id=task_id)))

        return queryset


class TenantTaskDestroyView(DestroyAPIView):
    """ Удаление заявки пользователя
    http://127.0.0.1:8000/tenant/test_user/delete-task/?task_id=2
    """
    serializer_class = TenantDetailTaskSerializer
    lookup_field = "user__username"

    def get_queryset(self):
        task_id = self.request.query_params.get("task_id")
        queryset = Tenant.objects.filter(
            user__username=self.kwargs[self.lookup_field]
        ).prefetch_related(Prefetch("tasks", Task.objects.filter(id=task_id)))

        return queryset
