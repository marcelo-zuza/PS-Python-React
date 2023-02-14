from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from rest_framework import viewsets
from .models import Produto
from .serializer import ProdutoSerializer
from .forms import CustomUsuarioCreateForm


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['produtos'] = Produto.objects.order_by('?').all()
        return context


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class CustomUsuarioCreateFormView(FormView):
    template_name = 'cadastro.html'
    form_class = CustomUsuarioCreateForm
    success_url = reverse_lazy('sucesso')

    def get_context_data(self, **kwargs):
        form = CustomUsuarioCreateForm
        context = {
            'form': form
        }
        if "form" not in kwargs:
            kwargs["form"] = self.get_form()
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)




