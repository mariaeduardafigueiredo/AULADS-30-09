from django.urls import path
from . import views

urlpatterns = [
     path('cadastrar/', views.criar_usuarios, name='criar_usuarios'),
    path('', views.login_usuario, name='logar_usuarios'),
    path('logout/', views.logout_usuario, name='logout_usuario'),
    # path('adicionar/', views.criar_usuarios, name='criar_usuarios'),
    # path('deletar/<int:id>/', views.deletar_usuarios, name='deletar_usuarios'),
    # path('atualizar/<int:id>/', views.atualizar_usuarios, name='atualizar_usuarios'),
]