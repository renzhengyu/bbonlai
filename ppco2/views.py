from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from .models import Calculation
from .forms import CfpVueForm, CfpForm
import json
from django.http.response import JsonResponse


def carbonfp(a):
    return (
        a['a1'] * 0.18 +            # plane
        a['a2'] * 0.06 +            # train
        a['a3'] * 0.09 +            # bus
        a['a4'] * 0.30 +            # car
        a['a5'] * 0.26 +            # moto
        a['b1'] * 4.72 +            # small items
        a['b2'] * 11.80 +           # medium items
        a['b3'] * 47.19 +           # large items
        a['c1'] * 15 / a['c2'] +    # very small appliances / their users
        a['c3'] * 30 / a['c4'] +    # small appliances / their users
        a['c5'] * 300 / a['c6'] +   # medium appliances / their users
        a['c7'] * 1500 / a['c8'] +  # large appliances / their users
        a['d1'] * 0.027 * 52 +      # beef
        a['d2'] * 0.012 * 52 +      # port
        a['d3'] * 0.0069 * 52 +     # chicken
        a['d4'] * 0.01 * 52 +       # fish
        a['d5'] * 0.0135 * 52 +     # cheese
        a['d6'] * 0.002 * 52 +      # dairy
        a['d7'] * 0.2 * 52 +        # eggs
        a['d8'] * 0.001 * 52 +      # grains and veg
        a['d9'] * 9.3 / 100 +       # <500km
        a['da'] * 93 / 100 +        # <5000km
        a['db'] * 223.2 / 100 +     # >= 5000km
        a['e1'] * 0.05 * (a['e2'] * 4000/a['e6'])/100 +
        a['e2'] * (4000/a['e6']) * 250 * ((100-a['e1'])/100)*12 / a['e3'] +
        a['e4'] * a['e2'] / a['e5'] +
        a['f4'] * a['f3'] / (a['f1'] + a['f2']) / a['f5']
    )/1000 - a['offset']            # kg => ton, deduct offset


def planets(carbonfp):
    return carbonfp/3


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


def cfp_vue(request):
    if request.method == 'POST':
        print(request.POST)
        form = CfpForm(request.POST)
        if form.is_valid():
            cfp = carbonfp(form.cleaned_data)
            cal = Calculation(**form.cleaned_data)
            cal.cfp = cfp
            cal.planets = planets(cfp)
            cal.save()
            total_submission = Calculation.objects.count()
            context = {
                'cfp': cal.cfp,
                'form_data': form.cleaned_data,
                'planets': cal.planets,
                'pk': cal.pk,
                'total_submission': total_submission,
            }
            return render(request, 'result.html', context)
    else:
        form = CfpForm()
        vue_form = CfpVueForm()
        context = {
            'form': form,
            "vue_form": vue_form,
        }
    return render(request, 'ppcfpcal.html', context)


def cal_result(request, pk):
    cal = get_object_or_404(Calculation, id=pk)
    total_submission = Calculation.objects.count()
    context = {
        'cal': cal,
        'total_submission': total_submission,
    }
    return render(request, 'result.html', context)
