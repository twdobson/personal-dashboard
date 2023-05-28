import django_tables2 as tables
from django.utils.html import format_html
from .models import Person, Passenger
from django.utils.safestring import mark_safe

class PersonTable(tables.Table):
    image = tables.Column(empty_values=(), verbose_name="Image")

    class Meta:
        model = Person
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "image")

    def render_name(self, value):
        badge_html = '<span class="badge bg-primary">Badge</span>'
        return mark_safe('{} {}'.format(badge_html, value))  

    def render_image(self, value):
        
        value = '/static/assets/images/logo-thumb.png'
        return format_html('<img src="{}" width="50" height="50">', value)
    
class PassengerTable(tables.Table):
    
    class Meta:
        model = Passenger
        template_name = "django_tables2/bootstrap.html"    
        per_page = 10
    
