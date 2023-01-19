import django_filters
from .models import *
from django import forms

class SermonFilter(django_filters.FilterSet):
    Sermon_title = django_filters.CharFilter(field_name='Sermon_title', lookup_expr='icontains')
    Preacher = django_filters.CharFilter(field_name='Preacher', lookup_expr='icontains')
    Scripture = django_filters.CharFilter(field_name='Scripture', lookup_expr='icontains')
    # Month = django_filters.CharFilter(field_name='Date', lookup_expr='icontains')

    class Meta:
        model = Sermon
        fields = ['Sermon_title','Preacher', 'Scripture']

class FamilyFilter(django_filters.FilterSet):
    Name = django_filters.CharFilter(field_name='Name', lookup_expr='icontains')
    Leader = django_filters.CharFilter(field_name='Leader', lookup_expr='icontains')
    # Scripture = django_filters.CharFilter(field_name='Scripture', lookup_expr='icontains')
    # Month = django_filters.CharFilter(field_name='Date', lookup_expr='icontains')

    class Meta:
        model = Family
        fields = ['Name','Leader']

class TeamFilter(django_filters.FilterSet):
    Name = django_filters.CharFilter(field_name='Name', lookup_expr='icontains')
    Leader = django_filters.CharFilter(field_name='Leader', lookup_expr='icontains')
    # Scripture = django_filters.CharFilter(field_name='Scripture', lookup_expr='icontains')
    # Month = django_filters.CharFilter(field_name='Date', lookup_expr='icontains')

    class Meta:
        model = Team
        fields = ['Name','Leader']

class ActivityFilter(django_filters.FilterSet):
    Title = django_filters.CharFilter(field_name='Title', lookup_expr='icontains')
    Venue = django_filters.CharFilter(field_name='Venue', lookup_expr='icontains')
    # Scripture = django_filters.CharFilter(field_name='Scripture', lookup_expr='icontains')
    # Month = django_filters.CharFilter(field_name='Date', lookup_expr='icontains')

    class Meta:
        model = Activity
        fields = ['Title','Venue']