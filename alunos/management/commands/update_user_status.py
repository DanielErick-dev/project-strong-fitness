from django.core.management.base import BaseCommand
from alunos.models import Aluno
from datetime import datetime, timedelta


class Command(BaseCommand):
    def handle(self, *args, **options):
        today = datetime.now().date()
        alunos_vencidos = Aluno.objects.filter(
            expiration_date__lt=today,
            status='A'
        )
        for aluno in alunos_vencidos:
            aluno.status = 'P'
            aluno.last_status_change = today
            aluno.save()
            self.stdout.write(f'Aluno {aluno.name} {aluno.lastname} atualizado para Pendente')
        limite_inatividade = today - timedelta(days=7)
        alunos_pendentes_antigos = Aluno.objects.filter(
            last_status_change__lte=limite_inatividade,
            status='P',
        )
        for aluno in alunos_pendentes_antigos:
            aluno.status = 'I'
            aluno.save()
            self.stdout.write(f'Aluno {aluno.name} {aluno.lastname} atualizado para Inativo')
