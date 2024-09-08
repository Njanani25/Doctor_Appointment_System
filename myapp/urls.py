from django.urls import path
from myapp import views

urlpatterns = [ 
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('main/',views.main,name='main'),
    path('appointment/',views.appointment,name='appointment'),
    path('book/<int:id>',views.book,name='book'),
]
