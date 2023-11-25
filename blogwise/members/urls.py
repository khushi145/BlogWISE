from django.urls import path
from .views import UserRegistrationView,UserEditView,PasswordsChangeView,ShowProfileView,EditProfileView,CreateProfileView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name="register"),
    path('edit_profile/', UserEditView.as_view(), name="edit_profile"),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_password.html')),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
    path('<int:pk>/profile', ShowProfileView.as_view(), name="show_profile"),
    path('<int:pk>/edit_profile_page', EditProfileView.as_view(), name="edit_profile_page"),
    path('create_profile_page', CreateProfileView.as_view(), name="create_profile_page"),
]
