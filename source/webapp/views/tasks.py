from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from webapp.forms import ArticleForm

from webapp.models import Task

from webapp.models import Teg


class ArticleView(TemplateView):
    template_name = "tasks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context


class ArticleCreateView(TemplateView):
    template_name = "task_create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ArticleForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('detail_view', pk=article.pk)
        return render(request, 'task_create.html', context={'form': form})


class ArticleUpdateView(TemplateView):
    template_name = "task_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        context['form'] = ArticleForm(instance=context['task'])
        return context

    def post(self, request, *args, **kwargs):
        article = get_object_or_404(Task, pk=kwargs['pk'])
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('detail_view', pk=article.pk)
        return render(request, 'task_update.html', context={'form': form, 'task': article})


class ArticleDetailView(TemplateView):
    template_name = "detail_task.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context


class ArticleDeletedView(TemplateView):
    template_name = "delete_confirm.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context


class ArticleDeleteConfirmView(TemplateView):
    def post(self, request, *args, **kwargs):
        article = get_object_or_404(Task, pk=kwargs['pk'])
        article.delete()
        return redirect("index_article")
