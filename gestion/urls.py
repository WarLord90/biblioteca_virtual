from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.lista_libros, name='lista_libros'),
    path('login/', auth_views.LoginView.as_view(template_name='gestion/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    path('libro/<int:pk>/', views.detalle_libro, name='detalle_libro'),
    path('mis-prestamos/', views.mis_prestamos, name='mis_prestamos'),
    path('devolver/<int:pk>/', views.devolver_prestamo, name='devolver_prestamo'),
    path('prestamos-todos/', views.prestamos_todos, name='prestamos_todos'),

]
