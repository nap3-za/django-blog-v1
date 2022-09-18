from django.shortcuts import render
from .models import Post
from .forms import AddPostForm, EditPostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.

#def HomeView(request, *args, **kwargs):

#    context = {}
#    return render(request, "blog_app/home.html", context)


class HomeView(ListView):
    model = Post
    template_name = "blog_app/html/home.html"
    ordering = ['-id']
    

class PostView(DetailView):
    model = Post
    template_name = "blog_app/html/post.html"
    

class AddPostView(CreateView):
    model = Post
    form_class = AddPostForm
    template_name = "blog_app/html/add-post.html"


class EditPostView(UpdateView):
    model= Post
    form_class = EditPostForm
    template_name = "blog_app/html/update.html"


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog_app/html/delete.html'
    success_url = 'http://127.0.0.1:8000/posts/'    
    
