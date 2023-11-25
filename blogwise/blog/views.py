from django.shortcuts import render, get_object_or_404
from .models import Post,Category,User
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from .forms import PostForm,EditForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect   
from django.db.models import Q

class SearchView(ListView):
    model = Post
    template_name = "search.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("search")
        object_list = Post.objects.filter(Q(title__icontains=query)|Q(snippet__icontains=query)|Q(title_tag__icontains=query)|Q(category__icontains=query)|Q(body__icontains=query))
        return object_list
    
    def get_context_data(self,*args,**kwargs):
        posts=Post.objects.all()
        cat_menu=Category.objects.all()
        context=super(SearchView,self).get_context_data(*args,**kwargs)
        context["cat_menu"]=cat_menu
        context["posts"]=posts
        return context
     
def CategoryView(request,cats):
    category_posts=Post.objects.filter(category=cats.replace('-',' '))
    cat_menu=Category.objects.all()
    posts=Post.objects.all()
    return render(request,'categories.html',{'cats':cats.title().replace('-',' '),'posts':posts,'category_posts':category_posts,'cat_menu':cat_menu})

def LatestView(request):
    cat_menu=Category.objects.all()
    posts=Post.objects.all()
    latest_post=Post.objects.all().order_by('-id')[:6]
    return render(request,'latest.html',{'latest_post':latest_post,'cat_menu':cat_menu,'posts':posts})

def CategoryListView(request):
    cat_menu=Category.objects.all()
    return render(request,'category_list.html',{'cat_menu':cat_menu})

def LikeView(request,pk):
    post=get_object_or_404(Post,id=request.POST.get('post_id'))
    liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('article-detail',args=[str(pk)]))

class HomeView(ListView):
    model=Post
    template_name='home.html'
    cats=Category.objects.all()
    ordering=["-id"]

    def get_context_data(self,*args,**kwargs):
        latest_post=Post.objects.all().order_by('-id')
        users=User.objects.all()
        cat_menu=Category.objects.all()
        context=super(HomeView,self).get_context_data(*args,**kwargs)
        context["cat_menu"]=cat_menu
        context["users"]=users
        context["latest_post"]=latest_post
        return context

class ArticleDetailView(DetailView):
    model=Post
    template_name='article_details.html'

    def get_context_data(self,*args,**kwargs):
        cat_menu=Category.objects.all()
        posts=Post.objects.all()
        context=super(ArticleDetailView,self).get_context_data(*args,**kwargs)
        likes_id=get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes=likes_id.total_likes()
        liked=False
        if likes_id.likes.filter(id=self.request.user.id).exists():
            liked=True
        context["cat_menu"]=cat_menu
        context["posts"]=posts
        context["total_likes"]=total_likes
        context["liked"]=liked
        return context

class AddPostView(CreateView):
    model=Post
    form_class=PostForm
    template_name='add_post.html'
    #fields='__all__'
    def get_context_data(self,*args,**kwargs):
        context=super(AddPostView,self).get_context_data(*args,**kwargs)
        cat_menu=Category.objects.all()
        context["cat_menu"]=cat_menu
        return context


class AddCategoryView(CreateView):
    model=Category
    template_name='add_category.html'
    fields='__all__'

class UpdatePostView(UpdateView):
    model=Post
    form_class=EditForm
    template_name='update_post.html'
    #fields=['title','title_tag','body']
    def get_context_data(self,*args,**kwargs):
        context=super(UpdatePostView,self).get_context_data(*args,**kwargs)
        cat_menu=Category.objects.all()
        context["cat_menu"]=cat_menu
        return context

class DeletePostView(DeleteView):
    model=Post
    template_name='delete_post.html'
    #fields=['title','title_tag','body']
    success_url=reverse_lazy('home')