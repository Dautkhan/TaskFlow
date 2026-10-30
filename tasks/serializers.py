from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task # Task указывает с какой моделью работает сериализатор
        fields = [
            "id",
            "title",
            "description",
            "status",
            "priority",
            "created_at",
        ]


        read_only_fields = ["id", "created_at"]