from django.forms import ModelForm
from .models import Calculation
from django import forms


class CfpForm1(ModelForm):
    class Meta:
        model = Calculation
        fields = ('name', 'email',)


class CfpForm2(ModelForm):
    class Meta:
        model = Calculation
        fields = ('a1', 'a2', 'a3', 'a4', 'a5')


class CfpForm3(ModelForm):
    class Meta:
        model = Calculation
        fields = ('b1', 'b2', 'b3')


class CfpForm4(ModelForm):
    class Meta:
        model = Calculation
        fields = ('c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8')


class CfpForm5(ModelForm):
    class Meta:
        model = Calculation
        fields = ('d1', 'd2', 'd3', 'd4', 'd5',
                  'd6', 'd7', 'd8', 'd9', 'da', 'db')
        # widgets = {
        #     'd9': forms.RadioSelect,
        #     'da': forms.RadioSelect,
        #     'db': forms.RadioSelect,
        # }


class CfpForm6(ModelForm):
    class Meta:
        model = Calculation
        fields = ('e1', 'e2', 'e6', 'e3', 'e4', 'e5')
        # widgets = {'e1': forms.RadioSelect}


class CfpForm7(ModelForm):
    class Meta:
        model = Calculation
        fields = ('f4', 'f1', 'f2', 'f3', 'f5')
        widgets = {'f4': forms.RadioSelect}
