from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

app_name = "account"

urlpatterns = [
    path("register/", views.signup_page, name="register"),
    path(
        "activate/<slug:uidb64>/<slug:token>/",
        views.activate_account_page,
        name="activate",
    ),
    path("login/", views.login_page, name="login"),
    path('profile/', views.profile, name='profile'),
    path("logout/", views.logout_view, name="logout"),
    
    # Password reset URLs - FIXED
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="account/password_reset.html",
            email_template_name="account/password_reset_email.html",
            success_url=reverse_lazy('account:password_reset_done')
        ),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="account/password_reset_sent.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="account/password_reset_form.html",
            success_url=reverse_lazy('account:password_reset_complete')
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="account/password_reset_done.html"
        ),
        name="password_reset_complete",
    ),
    
    # Password change URLs
    path(
        'password-change/',
        auth_views.PasswordChangeView.as_view(
            template_name="account/password_change_form.html",
            success_url=reverse_lazy('account:password_change_done')
        ),
        name='password_change'
    ),
    path(
        'password-change/done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name="account/password_change_done.html"
        ),
        name='password_change_done'
    ),
]
