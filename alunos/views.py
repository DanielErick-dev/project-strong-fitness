from django.views import generic
from .models import Aluno
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from django.urls import reverse_lazy
from django.utils import timezone
from django.db.models import Q
from unidecode import unidecode
from django.shortcuts import redirect


class GetAlunos(LoginRequiredMixin, generic.ListView):
    model = Aluno
    template_name = 'alunos.html'
    context_object_name = 'alunos'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name', '').strip()
        cpf = self.request.GET.get('cpf', '').strip()
        norm_name = unidecode(name).lower().replace(' ', '') if name else None
        norm_cpf = cpf.replace('-', '').replace('.', '') if cpf else None
        filters = Q()
        if norm_name:
            filters &= Q(name__icontains=norm_name) | Q(lastname__icontains=norm_name)
        if norm_cpf:
            filters &= Q(cpf__icontains=norm_cpf)
        return queryset.filter(filters).exclude(status='I')


class CreateAlunos(LoginRequiredMixin, generic.CreateView):
    model = Aluno
    template_name = 'create_alunos.html'
    form_class = forms.AlunosForm
    success_url = reverse_lazy('get_alunos')


class DetailAlunos(LoginRequiredMixin, generic.DetailView):
    model = Aluno
    template_name = 'detail_alunos.html'


class DeleteAlunos(LoginRequiredMixin, generic.DeleteView):
    model = Aluno
    template_name = 'delete_alunos.html'
    success_url = reverse_lazy('get_alunos')


class UpdateAlunos(LoginRequiredMixin, generic.UpdateView):
    model = Aluno
    template_name = 'update_alunos.html'
    success_url = reverse_lazy('get_alunos')
    form_class = forms.AlunosForm


def atualize_alunos(request, pk):
    aluno = Aluno.objects.get(pk=pk)
    aluno.expiration_date = timezone.now().date() + timezone.timedelta(days=31)
    aluno.status = 'A'
    aluno.save()
    return redirect('get_alunos')


class GetPendingAlunos(LoginRequiredMixin, generic.ListView):
    model = Aluno
    template_name = 'pending_alunos.html'
    context_object_name = 'pending_alunos'
    paginate_by = 10

    def get_queryset(self):
        pending_alunos = Aluno.objects.filter(status='P').order_by('last_status_change')
        return pending_alunos


class GetInactiveAlunos(LoginRequiredMixin, generic.ListView):
    model = Aluno
    template_name = 'inactive_alunos.html'
    context_object_name = 'inactive_alunos'
    paginate_by = 10

    def get_queryset(self):
        inactive_alunos = Aluno.objects.filter(status='I')
        return inactive_alunos

