from django.conf.urls import url
from . import views
from bendita.views import subscribe


app_name = 'iclinicapp'
urlpatterns = [
    url(r'^$', views.pagina_inicial, name='pagina_inicial'),
    # url(r'^index$', views.pagina_inicial, name='pagina_inicial'),
    # url(r'^about$', views.pagina_about, name='pagina_about'),
    # url(r'^products$', views.pagina_products, name='pagina_products'),
    # url(r'^store$', views.pagina_store, name='pagina_store'),
    # url(r'^subscribe/', views.subscribe, name = "subscribe"),
    
    # url(r'^teste$', views.teste, name='teste'),

]
