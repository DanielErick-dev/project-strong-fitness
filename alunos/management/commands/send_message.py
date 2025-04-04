from django.core.management.base import BaseCommand
from alunos.models import Aluno
from clients.callmebot_service import CallMeBot
from alunos.messages import MESSAGE_TEMPLATE


class Command(BaseCommand):
    def handle(self, *args, **options):
        pending_alunos = Aluno.objects.filter(status='P')
        if pending_alunos:
            lista_alunos = []
            for aluno in pending_alunos:
                lista_alunos.append(
                    f"ALUNO: *{aluno.name.title()} {aluno.lastname.title()}*\n"
                    f"DATA DO VENCIMENTO: *{aluno.expiration_date.strftime('%d/%m/%Y')}*\n"
                )
            mensagem_final = MESSAGE_TEMPLATE.format(
                lista_alunos='\n'.join(lista_alunos)
            )
            callmebot = CallMeBot()
            callmebot.send_message(mensagem_final)
            print('mensagem enviada com sucesso')
        else:
            print('não há alunos pendentes, portanto não houve envio de mensagem')
