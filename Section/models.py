from django.db import models


class SectionsManager(models.Manager):
    def find_by_name(self, name):
        return self.filter(name=name).first()


class Sections(models.Model):
    name = models.CharField(max_length=75, null=True, blank=True, verbose_name="نام")
    title = models.CharField(max_length=50, null=True, blank=True, verbose_name="عنوان")
    subtitle = models.CharField(max_length=50, null=True, blank=True, verbose_name="زیرعنوان")
    content = models.TextField(null=True, blank=True, verbose_name="توضیحات")
    location = models.CharField(max_length=100, blank=True, null=True, verbose_name="مکان قرارگیری")

    objects = SectionsManager()

    class Meta:
        verbose_name = 'ّبخش سایت'
        verbose_name_plural = 'بخش های سایت'


class SliderManager(models.Manager):
    def find_by_name(self, title):
        return self.filter(title=title).first()


def image_slider(instance, filename):
    return f'slider/{instance.title}_logo.{filename.split(".")[-1]}'


class Slider(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name="عنوان")
    subtitle = models.CharField(max_length=150, null=True, blank=True, verbose_name="زیرعنوان")
    content = models.TextField(null=True, blank=True, verbose_name="توضیحات")
    image = models.ImageField(upload_to=image_slider, null=True, blank=True, verbose_name="عکس اسلایدر")

    objects = SliderManager()

    class Meta:
        verbose_name = "اسلایدر"
        verbose_name_plural = "اسلایدرها"
