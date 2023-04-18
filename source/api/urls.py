from django.urls import path

from api.views.tasks_api_view import TaskSimpleView, TaskUpdateView, TaskDeleteSimpleView

from api.views.project_api_view import ProjectSimpleView, ProjectUpdateView, ProjectDeleteSimpleView

urlpatterns =[
    path('tasks/detail/<int:pk>', TaskSimpleView.as_view(), name="tasks_detail"),
    path('tasks/resources/<int:pk>', TaskUpdateView.as_view(), name="tasks_update"),
    path('tasks/delete/<int:pk>', TaskDeleteSimpleView.as_view(), name="tasks_delete"),
    path('project/detail/<int:pk>', ProjectSimpleView.as_view(), name="project_detail"),
    path('project/resources/<int:pk>', ProjectUpdateView.as_view(), name="project_update"),
    path('project/delete/<int:pk>', ProjectDeleteSimpleView.as_view(), name="project_delete"),
]
