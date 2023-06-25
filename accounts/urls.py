from django.urls import path , include
from . import views
app_name = 'jop'
urlpatterns = [
    path('signin', views.signin , name='signin'),
    path('signup', views.signup , name='signup'),
    path('logout', views.logout , name='logout'),
    path('users', views.users , name='users'),
    path('profile/<str:pk>', views.profile , name='profile'),
    path('profile/edit/', views.profile_edit , name='profile_edit'),
]