from rest_framework.serializers import ModelSerializer

from .models import Tenant, Task


class TaskListSerializer(ModelSerializer):

    class Meta:
        model = Task
        fields = [
            "inn",
            "id",
        ]


class TaskDetailSerializer(ModelSerializer):

    class Meta:
        model = Task
        fields = "__all__"


class TenantListTaskSerializer(ModelSerializer):
    tasks = TaskListSerializer(many=True, read_only=True)

    class Meta:
        model = Tenant
        exclude = ["user"]


class TenantDetailTaskSerializer(ModelSerializer):
    tasks = TaskDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Tenant
        exclude = ["user"]
