from django.forms import ModelForm
from .models import Calculation
from django import forms


class CfpForm(ModelForm):
    class Meta:
        model = Calculation
        fields = (
            'name', 'email', 'offset',
            'a1', 'a2', 'a3', 'a4', 'a5',
            'b1', 'b2', 'b3',
            'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8',
            'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'da', 'db',
            'e1', 'e2', 'e6', 'e3', 'e4', 'e5',
            'f4', 'f1', 'f2', 'f3', 'f5',
        )
        widgets = {'f4': forms.RadioSelect}


class CfpVueForm():
    steps = [
        {"id": 1, "label": "You", "icon": "user",
            "template": "ppcfpcal-1.html"},
        {"id": 2, "label": "Transportation", "icon": "bus",
            "template": "ppcfpcal-2.html"},
        {"id": 3, "label": "Clothing", "icon": "tshirt",
            "template": "ppcfpcal-3.html"},
        {"id": 4, "label": "Electronics", "icon": "laptop",
            "template": "ppcfpcal-4.html"},
        {"id": 5, "label": "Food", "icon": "utensils",
            "template": "ppcfpcal-5.html"},
        {"id": 6, "label": "Electricity", "icon": "plug",
            "template": "ppcfpcal-6.html"},
        {"id": 7, "label": "House", "icon": "home",
            "template": "ppcfpcal-7.html"},
    ]
