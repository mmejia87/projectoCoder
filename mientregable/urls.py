from django.contrib import admin
from django.urls import path
from familia.views import hola, verFamiliar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('holamundo/', hola),
    path('Familiar/',verFamiliar),
]
