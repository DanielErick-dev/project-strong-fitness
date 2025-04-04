from django.urls import path
from . import views

urlpatterns = [
    path("", views.GetAlunos.as_view(), name='get_alunos'),
    path("create/", views.CreateAlunos.as_view(), name='create_alunos'),
    path("detail/<int:pk>/", views.DetailAlunos.as_view(), name='detail_alunos'),
    path("delete/<int:pk>/", views.DeleteAlunos.as_view(), name='delete_alunos'),
    path("update/<int:pk>/", views.UpdateAlunos.as_view(), name='update_alunos'),
    path("atualize/<int:pk>/", views.atualize_alunos, name='atualize_alunos'),
    path("pending/", views.GetPendingAlunos.as_view(), name='pending_alunos'),
    path("inactive/", views.GetInactiveAlunos.as_view(), name='inactive_alunos')
]
