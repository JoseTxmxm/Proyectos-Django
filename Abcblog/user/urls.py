from django.urls import path # type: ignore
from user import views # type: ignore
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView # type: ignore


urlpatterns = [
    path('login/', views.Login_View.as_view(), name='login'),
    path('add/', views.SignUpView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('edit/', views.UserUpdateView.as_view(), name='edit_profile'),
    path('delete/', views.UserDeleteView.as_view(), name='delete_user'),
    
    path('profile/<int:pk>',views.ViewProfile.as_view(),name='view_profile'),
    
    path('password/', views.PasswordsChangeView.as_view(), name='change_password'),

    path('password_reset/', PasswordResetView.as_view(
        template_name = 'password/password_reset.html'
    ), name='password_reset'),

    path('password_reset_/done/', PasswordResetDoneView.as_view(
        template_name = 'password/password_reset_done.html'
    ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name = 'password/password_reset_confirm.html'
    ), name='password_reset_confirm'),

    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    ]