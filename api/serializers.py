from django.utils.translation import ugettext_lazy as _
from django.core.validators import EmailValidator

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from Setting.models import ThemeSetting
from Section.models import Sections, Slider
from Product.models import Products
from Newsletters.models import NewSletter


class ProductsSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class ThemeSettingSerialiser(serializers.ModelSerializer):
    class Meta:
        model = ThemeSetting
        fields = '__all__'


class SectionSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Sections
        fields = '__all__'


class SliderSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'


class NewSletterCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewSletter
        fields = (
            "name",
            "email"
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].required = True
        self.fields['email'].error_messages['required'] = _("ارسال ایمیل اجباری است")
        self.fields['email'].error_messages['blank'] = _("ایمیل نباید خالی باشد")
        self.fields['email'].validators = [
            UniqueValidator(queryset=NewSletter.objects.all(), message='این ایمیل قبلا ثبت شده است'),
            EmailValidator(message=_("لطفا آدرس ایمیل معتبر وارد کنید"))
        ]

    def create(self, validated_data):
        NewSletter.objects.create(**validated_data)
        return True
