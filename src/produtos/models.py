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
    )

    class Meta:

        ordering = ['name', 'category']

    def __str__(self) -> str:

        return f'{self.name} - {self.unit_price}'