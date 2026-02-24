from django.db import models


class Segments(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name='Nome do Segmento'
    )
    description = models.TextField(
        verbose_name='Descrição do Segmento',
        blank=True,
        null=True,
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name='Data de Criação'
    )
    modified = models.DateField(
        auto_now=True,
        verbose_name='Data de Modificação'
    )

    class Meta:

        ordering = ['name',]

    def __str__(self) -> str:
        return self.name
