from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm,EditProfileForm,PasswordChangingForm,ProfilePageForm
from blog.models import Profile,Post,Category

class CreateProfileView(generic.CreateView):
    model=Profile
    form_class=ProfilePageForm
    template_name='registration/create_profile_page.html'

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    def get_context_data(self,*args,**kwargs):
        posts=Post.objects.all()
        cat_menu=Category.objects.all()
        context=super(CreateProfileView,self).get_context_data(*args,**kwargs)
        context["posts"]=posts
        context["cat_menu"]=cat_menu
        return context

class EditProfileView(generic.UpdateView):
    model=Profile
    template_name='registration/edit_profile_page.html'
    fields=['bio','profile_pic','linkedin_url','instagram_url','twitter_url']
    success_url=reverse_lazy('home')
    def get_context_data(self,*args,**kwargs):
        posts=Post.objects.all()
        cat_menu=Category.objects.all()
        context=super(EditProfileView,self).get_context_data(*args,**kwargs)
        context["posts"]=posts
        context["cat_menu"]=cat_menu
        return context

class ShowProfileView(generic.DetailView):
    model=Profile
    template_name='registration/user_profile.html'
    def get_context_data(self,*args,**kwargs):
        posts=Post.objects.all()
        cat_menu=Category.objects.all()
        context=super(ShowProfileView,self).get_context_data(*args,**kwargs)
        page_user=get_object_or_404(Profile,id=self.kwargs['pk'])
        context["page_user"]=page_user
        context["posts"]=posts
        context["cat_menu"]=cat_menu
        return context

class PasswordsChangeView(PasswordChangeView):
    form_class=PasswordChangingForm
    success_url=reverse_lazy('login')
    def get_context_data(self,*args,**kwargs):
        posts=Post.objects.all()
        cat_menu=Category.objects.all()
        context=super(PasswordChangeView,self).get_context_data(*args,**kwargs)
        context["posts"]=posts
        context["cat_menu"]=cat_menu
        return context

class UserRegistrationView(generic.CreateView):
    form_class=SignUpForm
    template_name='registration/registration.html'
    success_url=reverse_lazy('login')
    def get_context_data(self,*args,**kwargs):
        posts=Post.objects.all()
        cat_menu=Category.objects.all()
        context=super(UserRegistrationView,self).get_context_data(*args,**kwargs)
        context["posts"]=posts
        context["cat_menu"]=cat_menu
        return context

class UserEditView(generic.UpdateView):
    form_class=EditProfileForm
    template_name='registration/edit_profile.html'
    success_url=reverse_lazy('home')

    def get_context_data(self,*args,**kwargs):
        posts=Post.objects.all()
        cat_menu=Category.objects.all()
        context=super(UserEditView,self).get_context_data(*args,**kwargs)
        context["posts"]=posts
        context["cat_menu"]=cat_menu
        return context

    def get_object(self):
        return self.request.user