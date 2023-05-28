
"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.shortcuts import render
# from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import get_object_or_404, render
# from django.urls import reverse

# from .models import Choice, Question


# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {"latest_question_list": latest_question_list}
#     return render(request, "polls/index.html", context)

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question": question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import JsonResponse
from django.db.models import Count
from django.db.models.functions import TruncMonth, ExtractMonth, TruncQuarter

from .models import Choice, Question, Play

# def graph(request):
#     return render(request, 'polls/graph.html')

# def play_count_by_month(request):
#     print("*"*100)
#     # def play_count_by_month(request):
#     data = (
#         Play.objects
#         .annotate(month=TruncMonth('date'))
#         .values('month')
#         .annotate(count_items=Count('id'))
#         .order_by('month')
#     )
#     # return JsonResponse(list(data), safe=False)
#     # data = Play.objects.all().annotate(month=TruncMonth('date')) #.values('month').annotate(
#         # count_items=Count('id')
#         # )
#     # data= Play.objects.all()    .annotate(month=ExtractMonth('date')).values('month').annotate(count_items=Count('id')) .values('month', 'count_items')  
    
#     print(data)
#     print("%"*100)
#     return JsonResponse(list(data), safe=False)


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
            :5
        ]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

from django.db.models import Count, Q
from django.shortcuts import render
from .models import Passenger

def ticket_class_view(request):
    """
    https://github.com/sibtc/django-highcharts-example
    https://simpleisbetterthancomplex.com/tutorial/2018/04/03/how-to-integrate-highcharts-js-with-django.html

    Example 1: Overall this design is bad as we use python to create javascript within a template (prone to error)
    """
    dataset = Passenger.objects \
        .values('ticket_class') \
        .annotate(survived_count=Count('ticket_class', filter=Q(survived=True)),
                  not_survived_count=Count('ticket_class', filter=Q(survived=False))) \
        .order_by('ticket_class')
    return render(request, 'polls/ticket_class.html', {'dataset': dataset})

import json
from django.db.models import Count, Q
from django.shortcuts import render
from .models import Passenger

def ticket_class_view_2(request):
    """
    https://github.com/sibtc/django-highcharts-example
    https://simpleisbetterthancomplex.com/tutorial/2018/04/03/how-to-integrate-highcharts-js-with-django.html

    Example 2: Decent design, however still suffers from using the templating language to create Java Script
    """
    dataset = Passenger.objects \
        .values('ticket_class') \
        .annotate(survived_count=Count('ticket_class', filter=Q(survived=True)),
                  not_survived_count=Count('ticket_class', filter=Q(survived=False))) \
        .order_by('ticket_class')

    categories = list()
    survived_series = list()
    not_survived_series = list()

    for entry in dataset:
        categories.append('%s Class' % entry['ticket_class'])
        survived_series.append(entry['survived_count'])
        not_survived_series.append(entry['not_survived_count'])

    return render(request, 'polls/ticket_class_2.html', {
        'categories': json.dumps(categories),
        'survived_series': json.dumps(survived_series),
        'not_survived_series': json.dumps(not_survived_series)
    })

import json
from django.db.models import Count, Q
from django.shortcuts import render
from .models import Passenger

def ticket_class_view_3(request):
    """
    https://github.com/sibtc/django-highcharts-example
    https://simpleisbetterthancomplex.com/tutorial/2018/04/03/how-to-integrate-highcharts-js-with-django.html

    Example 3: Even better, but not best design. Still interact with JS, albeit minimally
    """
    dataset = Passenger.objects \
        .values('ticket_class') \
        .annotate(survived_count=Count('ticket_class', filter=Q(survived=True)),
                  not_survived_count=Count('ticket_class', filter=Q(survived=False))) \
        .order_by('ticket_class')

    categories = list()
    survived_series_data = list()
    not_survived_series_data = list()

    for entry in dataset:
        categories.append('%s Class' % entry['ticket_class'])
        survived_series_data.append(entry['survived_count'])
        not_survived_series_data.append(entry['not_survived_count'])

    survived_series = {
        'name': 'Survived',
        'data': survived_series_data,
        'color': 'green'
    }

    not_survived_series = {
        'name': 'Survived',
        'data': not_survived_series_data,
        'color': 'red'
    }

    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'Titanic Survivors by Ticket Class'},
        'xAxis': {'categories': categories},
        'series': [survived_series, not_survived_series]
    }

    dump = json.dumps(chart)

    return render(request, 'polls/ticket_class_3.html', {'chart': dump})


def json_example(request):
    """
    https://simpleisbetterthancomplex.com/tutorial/2018/04/03/how-to-integrate-highcharts-js-with-django.html
https://github.com/sibtc/django-highcharts-example
    
    Example 4 function 1: Best, The idea here is to render the chart using an asynchronous call, returning a JsonResponse from the server.
    """
    return render(request, 'polls/json_example.html')

def chart_data(request):
    """
    https://simpleisbetterthancomplex.com/tutorial/2018/04/03/how-to-integrate-highcharts-js-with-django.html
    https://github.com/sibtc/django-highcharts-example

    Example 4 function 1: Best, The idea here is to render the chart using an asynchronous call, returning a JsonResponse from the server.
    """    
    dataset = Passenger.objects \
        .values('embarked') \
        .exclude(embarked='') \
        .annotate(total=Count('embarked')) \
        .order_by('embarked')

    port_display_name = dict()
    for port_tuple in Passenger.PORT_CHOICES:
        port_display_name[port_tuple[0]] = port_tuple[1]

    chart = {
        'chart': {'type': 'pie'},
        'title': {'text': 'Titanic Survivors by Ticket Class'},
        'series': [{
            'name': 'Embarkation Port',
            'data': list(map(lambda row: {'name': port_display_name[row['embarked']], 'y': row['total']}, dataset))
        }]
    }

    return JsonResponse(chart)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template import loader
from django.urls import reverse

from apps import COMMON
from apps.authentication.models import CustomUser


# @login_required(login_url="/login/")
# def index(request):
#     if CustomUser.objects.get(username=request.user.username).status == COMMON.USER_SUSPENDED:
#         logout(request)
#         return redirect(reverse(f'login') + f'?message=Suspended account. Please contact support.', )
#     context = {'segment': 'index'}

#     html_template = loader.get_template('home/index.html')
#     return HttpResponse(html_template.render(context, request))

def view_datatable(request):
    # html_template = loader.get_template('polls/table-dt_basic.html')
    # return HttpResponse(html_template.render({}, request))
    return render(request, "polls/table-dt_basic.html")

from django_tables2 import SingleTableView

from .models import Person
from .tables import PersonTable


class PersonListView(SingleTableView):
    model = Person
    table_class = PersonTable
    template_name = 'polls/table-dt_basic-2.html'


# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
from django.views.generic import TemplateView
from .models import Person, Passenger
from .tables import PersonTable, PassengerTable
from django_tables2 import RequestConfig
from django_tables2.export.export import TableExport
class TablesView(TemplateView):
    template_name = 'polls/table-dt_basic-3.html'

        


    def get_context_data(self, **kwargs):   
        context = super().get_context_data(**kwargs)     
        # Create Model2 table and export links/buttons

        # Generate export links for Model2 table
        model2_export_link_csv = '/path/to/export/model2/csv/'

        passenger_table = PassengerTable(Passenger.objects.all())
        RequestConfig(self.request).configure(passenger_table)  # Enable pagination and sorting
       

        context['model2_export_link_csv'] = model2_export_link_csv
        context['table_1'] = PersonTable(Person.objects.all())
        context['table_2'] = passenger_table
        return context
# from django_tables2 import SingleTableView
# from .models import Person, Passenger
# from .tables import PersonTable, PassengerTable

# class MultiTableView(SingleTableView):
#     model = Passenger
#     table_class = PassengerTable
#     template_name = 'polls/table-dt_basic-3.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # context['table_1'] = PersonTable(Person.objects.all())
#         context['table_2'] = PassengerTable(Passenger.objects.all())
#         return context