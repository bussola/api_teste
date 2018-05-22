# API REST ICLINICTEST

Esta é uma API desenvolvida utilizando [Django REST framework][djangorest]

----

# Requerimentos

* Python 3.6
* [Requirements.txt][requirements]

# Instalação

* Clone este repositório
* Instale os requerimentos necessários -> `"pip install -r requirements.txt"`
* Configure o seu banco de dados no arquivo [settings.py][set]
* Para rodar os testes -> `"python manage.py test iclinicapp"` 
* Pelo terminal, rode `"python manage.py runserver"`
* Pelo browser, acesse "127.0.0.1:8000/docs/" para a documentação

* "***********" OU "***********"

* Acesse [173.230.150.95/docs/][docs]

----

# Documentação

Esta API representa um sistema de agendamento

* Informações do agendamento:

```python
{
  "data": "aaaa-mm-dd",
  "hora_inicio": "hh:mm:AM",
  "hora_final": "hh:mm:AM",
  "paciente": "string",
  "procedimento": "lista"
}
Opções da lista "->" 'consulta', 'retorno' ou 'horario bloqueado'
```


Depois de instalado, acesse "127.0.0.1:8000/docs/" `OU` [173.230.150.95/docs/][docs] para detalhes de http

Para fins de testes, todas as permissões dos usuários estão liberadas

----

# Obvservações
O projeto [173.230.150.95/docs/][docs] foi desenvolvido utilizando [Django][django], [Nginx][nginx], [Gunicorn][gunicorn] e [Postgres][postgres]

Na documentação "/docs" foi utilizado [swagger][swagger].


* Como para logar em [173.230.150.95/docs/][docs]:

Acesse [173.230.150.95][docs1] e clique em `"Log in"`

Usuário: iclinic

Senha: senha123

----

# Testes

Os testes estão em [iclinicproject/iclinicapp/tests/test_agenda.py][test]

Para rodar os testes -> `python manage.py test iclinicapp` 


[requirements]:https://github.com/bussola/iclinic_teste/blob/master/requirements.txt
[djangorest]:https://github.com/encode/django-rest-framework
[docs]:http://173.230.150.95/docs/
[docs1]:http://173.230.150.95
[set]:https://github.com/bussola/iclinic_teste/blob/master/iclinicproject/iclinicproject/settings.py#L80
[test]:https://github.com/bussola/iclinic_teste/blob/master/iclinicproject/iclinicapp/tests/test_agenda.py
[django]:https://www.djangoproject.com/
[nginx]:https://www.nginx.com/
[gunicorn]:http://gunicorn.org/
[postgres]:https://www.postgresql.org/
[swagger]:https://swagger.io/