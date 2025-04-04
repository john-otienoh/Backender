from django.urls import include, path, re_path
from django.contrib.auth import views as auth_views

from .views import home, profile, RegisterView, recipe_list, recipe_detail
from .views import CustomLoginView, ResetPasswordView, ChangePasswordView
from .forms import LoginForm

# app_name = 'account'
urlpatterns = [
     path('', home, name='users-home'),
     path('register/', RegisterView.as_view(), name='users-register'),
     path('profile/', profile, name='users-profile'),
     path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='Recipes/registration/login.html',
                                           authentication_form=LoginForm), name='login'),

     path('logout/', auth_views.LogoutView.as_view(template_name='Recipes/registration/logout.html'), name='logout'),

     path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),

     path('password-reset-confirm/<uidb64>/<token>/',
          auth_views.PasswordResetConfirmView.as_view(template_name='Recipes/registration/password_reset_confirm.html'),
          name='password_reset_confirm'),

     path('password-reset-complete/',
          auth_views.PasswordResetCompleteView.as_view(template_name='Recipes/registration/password_reset_complete.html'),
          name='password_reset_complete'),

     path('password-change/', ChangePasswordView.as_view(), name='password_change'),
#    path( 'social-auth/',include('social_django.urls', namespace='social') ),
     path('<int:day>/<slug:recipe>/', recipe_detail, name='recipe-detail')
]
