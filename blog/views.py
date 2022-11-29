from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Post, Categoria
from .forms import PostForm , CategoriaForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Categoria.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryListView(request):
    cat_menu_list = Categoria.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-',' '))
    return render(request, 'categorias.html', {'cats':cats.title().replace('-',' '), 'category_posts':category_posts})

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
    def get_context_data(self, *args, **kwargs):
        cat_menu = Categoria.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post,id=self.kwargs['pk'])
        context['cat_menu'] = cat_menu
        return context
        
    
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class AddCategoryView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'add_post.html'

class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    