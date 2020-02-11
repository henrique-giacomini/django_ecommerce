from django.db import models

# Create your models here.

class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured():
        return elf.filter(featured=True, active=True)

# Classe que faz busca personalizada
class ProductManager(models.Manager):

    def get_queryset(self):
        return ProductQuerySet(self.model, using= self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self):
        return self.get_queryset().filter(featured=True)

    def get_by_id(self,id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

# Clsse que modela os produtos
class Product(models.Model):
    # Atributos dos produtos
    title       = models.CharField(max_length=120)
    description = models.TextField()
    price       = models.DecimalField(decimal_places=2, max_digits=20, default=100.00)
    image       = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.title
    objects = ProductManager()
