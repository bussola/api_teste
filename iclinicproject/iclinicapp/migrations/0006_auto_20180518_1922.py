# Generated by Django 2.0.5 on 2018-05-18 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iclinicapp', '0005_auto_20180518_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='procedimento',
            field=models.CharField(choices=[('consulta', 'CONSULTA'), ('retorno', 'RETORNO'), ('horario bloqueado', 'HORARIO BLOQUEADO')], default='consulta', max_length=17),
        ),
    ]
