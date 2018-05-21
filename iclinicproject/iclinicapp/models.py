from django.db import models


CHOICES = (
    ('consulta','CONSULTA'),
    ('retorno', 'RETORNO'),
    ('horario bloqueado','HORARIO BLOQUEADO'),
)

class Agenda(models.Model):
	created = models.DateTimeField(auto_now_add=True)

	data = models.DateField(blank=True)
	hora_inicio = models.TimeField(blank=True)
	hora_final = models.TimeField(blank=True)
	paciente = models.CharField(max_length=100, blank=True, default='')
	procedimento = models.CharField(max_length=17, choices=CHOICES, default='consulta')

	owner = models.ForeignKey('auth.User', related_name='agendamento', on_delete=models.CASCADE, blank=True, null=True)

	class Meta:
		ordering = ('created',)
