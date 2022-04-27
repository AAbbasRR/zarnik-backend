from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from Product.models import Products
from Setting.models import ThemeSetting
from Section.models import Sections, Slider
from .serializers import ProductsSerialiser, ThemeSettingSerialiser, SectionSerialiser, SliderSerialiser, NewSletterCreateSerializer


class ProductsListView(ListAPIView):
    permission_classes = [AllowAny, ]
    queryset = Products.objects.all()
    serializer_class = ProductsSerialiser


class ThemeSettingListView(ListAPIView):
    permission_classes = [AllowAny, ]
    queryset = ThemeSetting.objects.all()
    serializer_class = ThemeSettingSerialiser


class SectionListView(ListAPIView):
    permission_classes = [AllowAny, ]
    queryset = Sections.objects.all()
    serializer_class = SectionSerialiser


class SliderListView(ListAPIView):
    permission_classes = [AllowAny, ]
    queryset = Slider.objects.all()
    serializer_class = SliderSerialiser


class NewSletterCreateView(CreateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = NewSletterCreateSerializer

    def post(self, request, *args, **kwargs):
        ser = self.get_serializer(data=self.request.data)
        if ser.is_valid():
            ser.save()
            return Response({
                "status": True,
                "message": "اطلاعات شما در خبرنامه ثبت شد"
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "status": False,
                "message": ser.errors[list(ser.errors)[0]][0]
            }, status=status.HTTP_400_BAD_REQUEST)
