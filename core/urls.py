from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("admin/", admin.site.urls),
    path("students/", include("students.urls")),
    path("", views.LoginView.as_view(), name='login'),
    path("logout/", views.LogoutView.as_view(), name='logout'),
    path('teste/', lambda request: HttpResponse("<h1>A aplicação está respondendo!</h1>")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
