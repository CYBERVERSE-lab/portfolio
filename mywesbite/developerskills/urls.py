from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
# ]

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('card/<int:card_id>/', views.sub_page, name='sub_page'),
]