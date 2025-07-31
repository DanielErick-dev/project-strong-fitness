from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static


def teste_view(request):
    """Uma view de teste que não faz absolutamente nada."""
    return HttpResponse("<h1>O bypass do middleware funcionou!</h1>")


urlpatterns = [
    path('teste/', teste_view, name='teste'),
    path('', lambda request: HttpResponse('<h1> funcionou essa merda </h1>')),
    path("admin/", admin.site.urls),
    # path("students/", include("students.urls")),
    path("", views.LoginView.as_view(), name='login'),
    path("logout/", views.LogoutView.as_view(), name='logout'),
    # path('teste/', lambda request: HttpResponse("<h1>A aplicação está respondendo!</h1>")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
