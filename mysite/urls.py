"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls, name='admin'),
    path('api/galileu/procedimento_pericial/<int:id>/', views.procedimento_pericial, name='procedimento_pericial'),
    path('api/word/gerar_arquivo_word_laudo/', views.gerar_arquivo_word_laudo, name='gerar_arquivo_word_laudo'),
    path('login/', views.logininternal, name='login'),
    path('logout/', views.logoutinternal, name='logout'),
    path('modelo/laudo/criar/', views.create_modelo, name='minha_pagina'),
    path('modelo/laudo/salvar', views.create_modelo, name='salvar_modelo'),
    path('modelo/vestigio/criar/<int:type>/', views.create_modelo_vestigio, name='criar_modelo_vestigio'),
    path('modelo/vestigio/salvar/<int:type>/', views.create_modelo_vestigio, name='salvar_modelo_vestigio'),
    path('modelo/laudo/listagem', views.listagem, name='listagem_laudo_modelo'),
    path('modelo/vestigio/listagem', views.listagemVestigio, name='listagem_vestigio_modelo'),
    path('modelo/laudo/editar/<int:modelo_id>/', views.editar_modelo, name='editar_modelo'),
    path('modelo/laudo/visualizar/<int:modelo_id>/', views.visualizar_modelo, name='visualizar_modelo'),
    path('modelo/laudo/deletar/<int:modelo_id>/', views.deletar_modelo, name='deletar_modelo'),
    path('modelo/vestigio/editar/<int:modelo_id>/', views.editar_modelo_vestigio, name='editar_modelo_vestigio'),
    path('modelo/vestigio/visualizar/<int:modelo_id>/', views.visualizar_modelo_vestigio, name='visualizar_modelo_vestigio'),
    path('modelo/vestigio/deletar/<int:modelo_id>/', views.deletar_modelo_vestigio, name='deletar_modelo_vestigio'),
    path('gerar/laudo/', views.gerar_laudo, name='gerar_laudo'),
    path('gerar/modelo/formatado/<int:galileu_id>/<int:modelo_id>', views.gerar_modelo_formatado, name='gerar_modelo_formatado'),
    path('chamado/listagem', views.listagem_chamado, name='chamados'),
    path('chamado/criar/',views.gerar_chamado,name='criar_chamado'),
    path('chamado/<int:chamado_id>/', views.analisar_chamado, name='analisar_chamado'),
    path('chamado/responder/<int:chamado_id>/', views.responder_chamado, name='responder_chamado'),
    path('chamado/fechar/<int:chamado_id>/', views.fechar_chamado, name='fechar_chamado'),
    path('configuracoes/', views.configuracao, name='configuracao'),
    path('configuracao/superuser/add/<int:user_id>/', views.adicionar_superuser, name='adicionar_superuser'),
    path('configuracao/superuser/remove/<int:user_id>/', views.remover_superuser, name='remover_superuser'),
    path('configuracao/staff/add/<int:user_id>/', views.adicionar_staff, name='adicionar_staff'),
    path('configuracao/staff/remove/<int:user_id>/', views.remover_staff, name='remover_staff'),
]