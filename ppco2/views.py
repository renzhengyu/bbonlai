from django.shortcuts import render
from django.db.models import Q, Count
from .models import Calculation
from .forms import CfpForm1, CfpForm2, CfpForm3, CfpForm4, CfpForm5, CfpForm6, CfpForm7
from formtools.wizard.views import SessionWizardView, CookieWizardView
from collections import ChainMap
import json
from django.http.response import JsonResponse




def carbonfp(answers):
    return (
        answers['a1'] * 0.18 +
        answers['a2'] * 0.06 +
        answers['a3'] * 0.09 +
        answers['a4'] * 0.30 +
        answers['a5'] * 0.26 +
        answers['b1'] * 4.72 +
        answers['b2'] * 11.80 +
        answers['b3'] * 47.19 +
        answers['c1'] * 15 / answers['c2'] +
        answers['c3'] * 30 / answers['c4'] +
        answers['c5'] * 300 / answers['c6'] +
        answers['c7'] * 1500 / answers['c8'] +
        answers['d1'] * 0.027 * 52 +
        answers['d2'] * 0.012 * 52 +
        answers['d3'] * 0.0069 * 52 +
        answers['d4'] * 0.01 * 52 +
        answers['d5'] * 0.0135 * 52 +
        answers['d6'] * 0.002 * 52 +
        answers['d7'] * 0.2 * 52 +
        answers['d8'] * 0.001 * 52 +
        answers['d9'] * 9.3 / 100 +
        answers['da'] * 93 / 100 +
        answers['db'] * 223.2 / 100 +
        answers['e1'] +  # need review
        answers['e2'] * 12 * (4000 / 800) * 0.422 / answers['e3'] +
        answers['e4'] +
        answers['e5'] +
        answers['f1'] +
        answers['f2'] +
        answers['f3'] +
        answers['f4'] +
        answers['f5']
    )/1000


def planets(carbonfp):
    return carbonfp/3


class CfpWizard(SessionWizardView):
    form_list = [CfpForm1, CfpForm2, CfpForm3,
                 CfpForm4, CfpForm5, CfpForm6, CfpForm7]
    template_name = 'ppcfpcal.html'

    def get(self, request, *args, **kwargs):
        try:
            return self.render(self.get_form())
        except KeyError:
            return super().get(request, *args, **kwargs)

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        form_data_dict = dict(ChainMap(*form_data))
        cfp = carbonfp(form_data_dict)
        cal = Calculation(**form_data_dict)
        cal.cfp = cfp
        cal.planets = planets(cfp)
        cal.save()
        total_submission = Calculation.objects.count()

        context = {
            'cfp': cfp,
            'form_data': form_data_dict,
            'planets': planets(cfp),
            'pk': cal.pk,
            'total_submission': total_submission,
        }
        return render(self.request, 'result.html', context)

def planet_chart(request):
    return render(request, 'analysis.html')


def planet_chart_data(request):
    data = {
        'lte1': Calculation.objects.filter(planets__lte=1).count(),
        'lte2': Calculation.objects.filter(planets__gt=1, planets__lte=2).count(),
        'lte3': Calculation.objects.filter(planets__gt=2, planets__lte=3).count(),
        'lte4': Calculation.objects.filter(planets__gt=3, planets__lte=4).count(),
        'lte5': Calculation.objects.filter(planets__gt=4, planets__lte=5).count(),
        'lte6': Calculation.objects.filter(planets__gt=5, planets__lte=6).count(),
        'lte7': Calculation.objects.filter(planets__gt=6, planets__lte=7).count(),
        'lte8': Calculation.objects.filter(planets__gt=7, planets__lte=8).count(),
        'lte9': Calculation.objects.filter(planets__gt=8, planets__lte=9).count(),
        'lte10': Calculation.objects.filter(planets__gt=9, planets__lte=10).count(),
        'gt10': Calculation.objects.filter(planets__gt=10).count(),
    }

    total_submission = Calculation.objects.count()

    chart = {
        'chart': {'type': 'bar'},
        'title': {'text': 'Person-Planet Distribution'},
        'subtitle': {'text': f"Based on {total_submission} submissions"},
        'yAxis': {'title': {'text': 'Persons'}},
        'xAxis': {'categories': [
            '1 planet or less', 
            '1~2 planets',
            '2~3 planets',
            '3~4 planets',
            '4~5 planets', 
            '5~6 planets', 
            '6~7 planets', 
            '7~8 planets', 
            '8~9 planets', 
            '9~10 planets', 
            '>10 planets']},
        'series': [{
            'name': 'Persons',
            'data': [data[key] for key in data],
            'color': 'green'
        }],
    }

    return JsonResponse(chart)