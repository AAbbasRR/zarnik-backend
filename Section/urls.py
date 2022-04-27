from django.urls import path
from .views import *

app_name = 'section'
urlpatterns = [
    path('Sliders/', sliderviewall, name="Sliderlist"),
    path('Sliders/create', SliderCreate.as_view(), name="SliderCreate"),
    path('Sliders/update/<int:pk>', SliderUpdate.as_view(), name="SliderUpdate"),
    path('Sliders/delete/<int:pk>', SliderDelete.as_view(), name="SliderDelete"),

    path('Sections/', sectionviewall, name="Sectionlist"),
    path('Sections/update/<int:pk>', SectionUpdate.as_view(), name="SectionUpdate"),
]
