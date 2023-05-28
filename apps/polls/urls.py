from django.urls import path, re_path

from . import views
from . models import Passenger

# Namespace the url
# Name spacing allows the use of the {% url %} template tag across multiple apps
# See .html files where polls: tags the use of detail in the url template
app_name = "polls"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path('ticket-class/', views.ticket_class_view, name='ticket_class'),
    path('ticket-class-2/', views.ticket_class_view_2, name='ticket_class_2'),
    path('ticket-class-3/', views.ticket_class_view_3, name='ticket_class_3'),    
    path('json-example/', views.json_example, name='json_example'),
    path('json-example/data/', views.chart_data, name='chart_data'),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    # path("graph/", views.graph, name='graph'),
    path("table-dt_basic/", views.view_datatable, name='table-dt_basic'),
    path("table-dt_basic-2/", views.PersonListView.as_view(), name='table-dt_basic-2'),
    path("table-dt_basic-3/", views.TablesView.as_view(), name='table-dt_basic-3'),
    path('tables/table_2/export/', views.TablesView.as_view()),    
    # re_path('^api/play_count_by_month', views.play_count_by_month, name='play_count_by_month'),
]