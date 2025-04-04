from django.contrib import admin
from .models import Aluno


class AlunoAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'cpf', 'phone_number', 'status', 'date_of_birth', 'expiration_date', )
    search_fields = ('name', 'cpf', )


admin.site.register(Aluno, AlunoAdmin)
