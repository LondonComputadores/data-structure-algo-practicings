from django.urls import path

from .views import (
    ListVendedores,
    SearchVendedor,
    SearchVendedoresPaginada,
    CreateVendedor,
    UpdateVendedor,
    DestroyVendedor,
    ListTipoVendedor,
    ListSupervisores
)

urlpatterns = [
    path('cadastrar/', CreateVendedor.as_view()),
    path('atualizar/', UpdateVendedor.as_view()),
    path('apagar/id_unn=<int:id_unn>/id_emp=<int:id_emp>/id_ven=<int:id_ven>/', DestroyVendedor.as_view()),
    path('tipos/', ListTipoVendedor.as_view()),
    path('supervisores/id_unn=<int:id_unn>/id_emp=<int:id_emp>/', ListSupervisores.as_view()),
    path('listar/id_unn=<int:id_unn>/id_emp=<int:id_emp>/', ListVendedores.as_view()),
    path('pesquisar/', SearchVendedor.as_view()),
]
