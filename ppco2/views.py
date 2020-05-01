from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from .models import Calculation
from .forms import CfpForm1, CfpForm2, CfpForm3, CfpForm4, CfpForm5, CfpForm6, CfpForm7
from formtools.wizard.views import SessionWizardView
from collections import ChainMap
import json
from django.http.response import JsonResponse


class CfpWizard(SessionWizardView):
    form_list = [
        CfpForm1,
        CfpForm2,
        CfpForm3,
        CfpForm4,
        CfpForm5,
        CfpForm6,
        CfpForm7
    ]
    template_name = 'ppcfpcal.html'

    def get(self, request, *args, **kwargs):
        try:
            return self.render(self.get_form())
        except KeyError:
            return super().get(request, *args, **kwargs)

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        form_data_dict = dict(ChainMap(*form_data))
        cal = Calculation.objects.create(**form_data_dict)
        return redirect('ppco2:cal_result', pk=cal.pk)


def planet_chart(request):
    return render(request, 'analysis.html')


def planet_chart_data(request):
    data = {
        'a': Calculation.objects.filter(planets__lte=0.9).count(),
        'b': Calculation.objects.filter(planets__gt=0.9, planets__lte=1.3).count(),
        'c': Calculation.objects.filter(planets__gt=1.3, planets__lte=2.5).count(),
        'd': Calculation.objects.filter(planets__gt=2.5, planets__lte=4).count(),
        'e': Calculation.objects.filter(planets__gt=4, planets__lt=7).count(),
        'f': Calculation.objects.filter(planets__gt=7).count(),
    }
    total_submission = Calculation.objects.count()
    chart = {
        'chart': {'type': 'bar'},
        'title': {'text': 'Person-Planet Distribution'},
        'subtitle': {'text': f"Based on {total_submission} submissions"},
        'yAxis': {'title': {'text': 'Persons'}},
        'xAxis': {
            'categories': [
                '0.9 planet or less',
                '0.9~1.3 planets',
                '1.3~2.5 planets',
                '2.5~4 planets',
                '4~7 planets',
                '7 planets or more'
            ]
        },
        'series': [{
            'name': 'Persons',
            'data': [data[key] for key in data],
            'color': 'green'
        }],
    }
    return JsonResponse(chart)


def cal_result(request, pk):
    cal = get_object_or_404(Calculation, id=pk)
    total_submission = Calculation.objects.count()
    context = {
        'cal': cal,
        'total_submission': total_submission,
    }
    return render(request, 'result.html', context)
