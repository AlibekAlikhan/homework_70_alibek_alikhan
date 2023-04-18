from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from webapp.models import Project

from api.serializers import ProjectSerializer


class ProjectSimpleView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            objects = get_object_or_404(Project, pk=kwargs.get("pk"))
        except ObjectDoesNotExist:
            Response({"error": "введите существующий pk"})
        serializer = ProjectSerializer(objects)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProjectUpdateView(APIView):

    def put(self, request, *args, **kwargs):
        data = json.loads(request.body)
        objects = get_object_or_404(Project, pk=kwargs.get("pk"))
        serializer = ProjectSerializer(objects, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            response = Response({'errors': serializer.errors})
            response.status_code = 400
            return response


class ProjectDeleteSimpleView(APIView):
    def delete(self, request, *args, **kwargs):
        try:
            objects = get_object_or_404(Project, pk=kwargs.get("pk"))
            objects.delete()
        except ObjectDoesNotExist:
            Response({"error": "введите существующий pk"})
        return Response({f"delte - {kwargs.get('pk')}" : "мягкое удаление успешно выполнелось"})