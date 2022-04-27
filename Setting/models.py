from django.db import models


class ThemeSettingManager(models.Manager):
    def find_by_name(self, name):
        return self.filter(name=name).first()


class ThemeSetting(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True, verbose_name="عنوان")
    value = models.CharField(max_length=50, null=True, blank=True, verbose_name="مقدار")
    name = models.CharField(max_length=75, null=True, blank=True, verbose_name="نام")

    objects = ThemeSettingManager()

    class Meta:
        verbose_name = 'آپشن بخش ها'
        verbose_name_plural = 'آپشن های بخش ها'
