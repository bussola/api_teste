from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# LEXERS = [item for item in get_all_lexers() if item[1]]
# LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

PROC_CHOICES = (
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
	procedimento = models.CharField(max_length=17, choices=PROC_CHOICES, default='consulta')

	owner = models.ForeignKey('auth.User', related_name='agendamento', on_delete=models.CASCADE, blank=True, null=True)
	highlighted = models.TextField()

	class Meta:
		ordering = ('created',)


	# def save(self, *args, **kwargs):
	# 	"""
	# 	Use the `pygments` library to create a highlighted HTML
	# 	representation of the code snippet.
	# 	"""
	# 	# lexer = get_lexer_by_name(self.language)
	# 	# linenos = 'table' if self.linenos else False
	# 	# options = {'title': self.title} if self.title else {}
	# 	# formatter = HtmlFormatter(style=self.style, linenos=linenos,
	# 	#                           full=True, **options)
	# 	# self.highlighted = highlight(self.code, lexer, formatter)
	# 	super(Snippet, self).save(*args, **kwargs)