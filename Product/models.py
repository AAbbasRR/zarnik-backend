from django.db import models


class ProductManager(models.Manager):
    def find_by_name(self, name):
        return self.filter(name=name).first()


class Products(models.Model):
    STATUS_CHOICES = (
        ('S', 'تک'),
        ('M', 'عمده'),
        ('S_M', 'تک و عمده'),

    )
    name = models.CharField(max_length=50, verbose_name='کلید نام محصول', unique=True)
    title = models.CharField(max_length=50, null=True, blank=True, verbose_name='نام محصول')
    subtitle = models.CharField(max_length=75, null=True, blank=True, verbose_name='توضیح کوتاه')
    content = models.TextField(null=True, blank=True, verbose_name='توضیحات')
    ProductSize = models.CharField(max_length=50, null=True, blank=True, verbose_name='اندازه بسته بندی')
    ProductWeight = models.CharField(max_length=50, null=True, blank=True, verbose_name='وزن بسته بندی')
    ProductQuality = models.CharField(max_length=25, null=True, blank=True, verbose_name='کیفیت محصول')
    MotherPacking = models.CharField(max_length=50, null=True, blank=True, verbose_name='بسته بندی مادر')
    ProductWhoSell = models.CharField(max_length=20, null=True, blank=True, choices=STATUS_CHOICES, default='S', verbose_name='نحوه فروش')

    objects = ProductManager()

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = ' محصولات'
