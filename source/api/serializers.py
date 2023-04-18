from rest_framework import serializers

from webapp.models import Task

from webapp.models import Project


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id", "status", "teg", "text", "detail_text", "project", "create_at", "iis_deleted")
        read_only = ("id", "project", "create_at")


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "start_at", "end_at", "name", "text_project", "iis_deleted", "deleted_project_at")
        read_only = ("id", "deleted_project_at")
