
from django.contrib import admin
from django.urls import path, include
from .views import home, welcome, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('aluno/', include('aluno.urls')) ,
    path('professor/', include('professor.urls')) ,
    path('welcome/', welcome, name='welcome'),
    path('login/', login, name='login'),

]
