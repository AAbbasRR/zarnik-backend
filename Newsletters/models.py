from django.db import models


class NewSletter(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True, verbose_name="نام و نام خانوادگی")
    email = models.EmailField(unique=True, blank=False, null=False, verbose_name="ایمیل")

    class Meta:
        verbose_name = "کاربر خبرنامه"
        verbose_name_plural = "کاربران خبرنامه"
