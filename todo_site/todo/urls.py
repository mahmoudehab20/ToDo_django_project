from django.urls import path
from . import views

urlpatterns = [
    path('todo/',views.index,name="todo"),
    path('del/<str:itemID>',views.remove,name="del")
]
