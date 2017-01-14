# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('direccion', models.CharField(blank=True, max_length=100, default='')),
                ('provincia', models.CharField(choices=[('habana', 'Habana'), ('matanzas', 'Matanzas')], max_length=100)),
                ('municipio', models.CharField(choices=[('marianao', 'Marianao'), ('playa', 'Playa')], max_length=100)),
                ('descripcion', models.TextField()),
                ('extras', models.TextField()),
                ('numero_cuartos', models.PositiveSmallIntegerField()),
                ('area_total', models.PositiveIntegerField()),
                ('tipo', models.CharField(choices=[('apartamento', 'Apartamento'), ('casa', 'Casa'), ('otro', 'Otro')], max_length=100)),
                ('owner', models.ForeignKey(related_name='inmuebles', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
