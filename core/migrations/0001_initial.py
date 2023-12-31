# Generated by Django 4.1.3 on 2023-09-20 06:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Area",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=200, unique=True)),
                (
                    "descripcion",
                    models.CharField(blank=True, max_length=300, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Estado",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=200, unique=True)),
                (
                    "descripcion",
                    models.CharField(blank=True, max_length=300, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Usuario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rut", models.CharField(max_length=100, unique=True)),
                ("telefono", models.CharField(blank=True, max_length=100, null=True)),
                ("fecha_nacimiento", models.DateField()),
                (
                    "role",
                    models.CharField(
                        choices=[("admin", "Administrador"), ("cliente", "Cliente")],
                        max_length=20,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Requerimiento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("codigo", models.CharField(max_length=100, unique=True)),
                ("fecha_registro", models.DateTimeField(auto_now_add=True)),
                ("descripcion", models.CharField(max_length=500)),
                (
                    "observaciones",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                (
                    "area",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="requerimientos",
                        to="core.area",
                    ),
                ),
                (
                    "estado",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="requerimientos",
                        to="core.estado",
                    ),
                ),
                (
                    "usuario_asignado",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="requerimientos_asignado",
                        to="core.usuario",
                    ),
                ),
                (
                    "usuario_reporta",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="requerimientos_reporta",
                        to="core.usuario",
                    ),
                ),
            ],
        ),
    ]
