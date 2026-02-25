from django.db import models

from categorias.models import Category


class Product(models.Model):

    name = models.CharField(
        max_length=150,
        verbose_name='Nome do Produto',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='fk_produto_categoria',
        verbose_name='Categoria do Produto',
    )
    unit_price = models.DecimalField(
        verbose_name='Preço Unitário do Produto',
        max_digits=7,
        decimal_places=2,
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

        ordering = ['name', 'category']

    def __str__(self) -> str:

        return f'{self.name} - {self.unit_price}'
