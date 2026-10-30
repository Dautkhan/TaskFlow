
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from rest_framework.decorators import permission_classes

@api_view(["GET"])
def health_check(request):
    return Response(
        {
            "status": "ok",
            "service": "TaskFlow API",
        },
        status=status.HTTP_200_OK,
    )


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def task_list(request):
    if request.method == "GET":
        tasks = Task.objects.filter(owner=request.user)

        # Filter by status
        task_status = request.query_params.get("status")
        if task_status:
            tasks = tasks.filter(status=task_status)

        # Filter by priority
        priority = request.query_params.get("priority")
        if priority:
            tasks = tasks.filter(priority=priority)

        # Search by title or description
        search = request.query_params.get("search")
        if search:
            tasks = tasks.filter(
                Q(title__icontains=search)
                | Q(description__icontains=search)
            )

        # Sorting
        ordering = request.query_params.get(
            "ordering",
            "-created_at",
        )

        allowed_ordering = [
            "created_at",
            "-created_at",
            "title",
            "-title",
        ]

        if ordering in allowed_ordering:
            tasks = tasks.order_by(ordering)
        else:
            tasks = tasks.order_by("-created_at")

        paginator = PageNumberPagination() # создаем пагинатор
        paginator.page_size = 5 # показывает по 5 задач
        # выбирает задачи для текущей страницы
        result_page = paginator.paginate_queryset(tasks, request)
        serializer = TaskSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    # Create a new task
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST,
    )


@api_view(["GET", "PUT", "PATCH", "DELETE"])
@permission_classes([IsAuthenticated])
def task_detail(request, pk):
    task = get_object_or_404(
        Task,
        pk = pk,
        owner = request.user
    )

    # Get one task
    if request.method == "GET":
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    # Delete a task
    if request.method == "DELETE":
        task.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )

    # Update a task completely
    if request.method == "PUT":
        serializer = TaskSerializer(
            task,
            data=request.data,
        )

    # Update selected fields
    elif request.method == "PATCH":
        serializer = TaskSerializer(
            task,
            data=request.data,
            partial=True,
        )

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST,
    )
