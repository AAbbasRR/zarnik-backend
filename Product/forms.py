from django import forms
from Login.models import User
from .models import Products


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields['email'].disabled = True

    class Meta:
        model = User
        fields = ["email", "last_name", "first_name"]


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].disabled = True
        self.fields['name'].help_text = "نام محصول غیر قابل تغییر می باشد"

    class Meta:
        model = Products
        fields = ["name", "subtitle", "content", "ProductSize", "ProductWeight", "ProductQuality", "MotherPacking", "ProductWhoSell"]
