from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup')
]
         
