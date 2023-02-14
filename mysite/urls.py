from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import IndexView, ProdutoViewSet, CustomUsuarioCreateFormView
router = SimpleRouter()
router.register('produto', ProdutoViewSet)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contas/', include('django.contrib.auth.urls')),
    path('cadastro/', CustomUsuarioCreateFormView.as_view(), name='cadastro'),

]
