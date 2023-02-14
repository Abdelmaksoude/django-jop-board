from django.urls import path , include
from . import views
from . import api
app_name = 'jop'
urlpatterns = [
    path('', views.jop_list , name='jop_list'),
    path('add', views.add_jop , name='add_jop'),
    path('<str:slug>', views.jop_details , name='jop_details'),
    path('api/jops', api.jop_list_api , name='jop_list_api'),
    path('api/jops/<int:id>', api.jop_detail_api , name='jop_detail_api'),
    path('api/v2/jops', api.JopListApi.as_view() , name='jop_list_api'),
    path('api/v2/jops/<int:id>', api.JopDetail.as_view() , name='jop_list_api'),
]