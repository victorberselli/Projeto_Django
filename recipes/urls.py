from django.urls import path
from recipes.views import Home, Contato, Sobre
    
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', Home),
    path('contato/', Contato),
    path('sobre/', Sobre),
]