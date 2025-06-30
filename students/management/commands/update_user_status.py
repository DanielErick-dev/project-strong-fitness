from django.core.management.base import BaseCommand
from students.models import Aluno
from datetime import datetime, timedelta


class Command(BaseCommand):
    def handle(self, *args, **options):
        today = datetime.now().date()
        expiration_students = Aluno.objects.filter(
            expiration_date__lt=today,
            status='A'
        )
        for student in expiration_students:
            student.status = 'P'
            student.last_status_change = today
            student.save()
            self.stdout.write(f'Aluno {student.name} {student.lastname} atualizado para Pendente')
        limite_inatividade = today - timedelta(days=7)
        alunos_pendentes_antigos = Aluno.objects.filter(
            last_status_change__lte=limite_inatividade,
            status='P',
        )
        for aluno in alunos_pendentes_antigos:
            aluno.status = 'I'
            aluno.save()
            self.stdout.write(f'Aluno {aluno.name} {aluno.lastname} atualizado para Inativo')
