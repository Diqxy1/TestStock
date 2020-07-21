from django.db import models

from apps.categories.models import Category

# Create your models here.
class Product(models.Model):
    name = models.CharField('Nome', max_length=80)
    description = models.TextField('Descrição', null=True)
    price = models.DecimalField('Preço', max_digits=5, decimal_places=2)
    amount = models.DecimalField('Quantidade', max_digits=5, decimal_places=0)
    category = models.ForeignKey(Category, verbose_name='Categoria', null=True, on_delete=models.SET_NULL)
    create_at = models.DateTimeField('Data de criação', auto_now_add=True)
    updated_at = models.DateTimeField('Data de atualização', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    @property
    def abstract(self):
        return self.description[:30] + '....'

    @property
    def abstract_price(self):
        return 'R${}'.format(self.price)
