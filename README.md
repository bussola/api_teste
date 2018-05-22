# API REST ICLINICTEST

Esta é uma API desenvolvida utilizando [Django REST framework][djangorest]

----

# Requerimentos

* Python 3.6
* [Requirements.txt][requirements]

# Instalação

* Clone este repositório
* Instale os requerimentos necessários
* Pelo terminal, rode "python manage.py runserver"
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
```
Opções da lista -> 'consulta','retorno', 'horario bloqueado'


Depois de instalado, acesse "127.0.0.1:8000/docs/" `ou` [173.230.150.95/docs/][docs]



[requirements]:https://github.com/bussola/iclinic_teste/blob/master/requirements.txt
[djangorest]:https://github.com/encode/django-rest-framework
[docs]:http://173.230.150.95/docs/