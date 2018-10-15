from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import PostForm
from .models import FormModel


def index(request):
    posts = FormModel.objects.all()
    context = {'posts': posts}
    return render(request, 'forms_app/post_detail.html', context)


def post_detail(request, pk):
    post = get_object_or_404(FormModel, pk=pk)
    return render(request, 'forms_app/post_detail.html', {'post': post})


def post_new(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.published_date = timezone.now()
        post.save()
        return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm()
    return render(request,'forms_app/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(FormModel, pk=pk)
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.published_date = timezone.now()
        post.save()
        return redirect("post_detail", pk=post.pk)
    else:
        post = FormModel.objects.get(pk=pk)
        form = PostForm(instance=post)
    return render(request,'forms_app/post_edit.html', {'form': form})