from django.urls import path

from . import views

# Namespace the url
# Name spacing allows the use of the {% url %} template tag across multiple apps
# See .html files where polls: tags the use of detail in the url template
app_name = "polls"

urlpatterns = [
    
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]