
from django.urls import path,include
from.import views
urlpatterns = [
   path('',views.index,name='index'),
    path('Details/<int:pk>',views.detail,name='detail')
]
