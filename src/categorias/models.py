from django.db import models


class Category(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name='Nome da categoria'
    )
    description = models.TextField(
        verbose_name='Descrição da categoria',
        blank=True,
        null=True
    )
    created_at = models.DateField(
        verbose_name='Data de criação',
        auto_now_add=True
    )
    modified = models.DateField(
        verbose_name='Data de Modificação',
        auto_now=True
    )

    class Meta:

        ordering = ['name',]

    def __str__(self) -> str:

        return self.name
