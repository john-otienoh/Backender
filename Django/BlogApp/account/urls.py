from django.urls import path
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
    path("logout/", views.logout_view, name="logout"),
    path(
        "reset-password",
        auth_views.PasswordResetView.as_view(
            template_name="account/password_reset.html"
        ),
        name="reset_password",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="account/password_reset_sent.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="account/password_reset_form.html"
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
]
