import django.forms
from django_filters import FilterSet, ModelChoiceFilter, DateFilter
from django.forms import DateInput
from .models import *


class NewsFilter(FilterSet):
    teg = ModelChoiceFilter(
        field_name='postCategory',
        queryset=Category.objects.all(),
        label='Teg/Articles',
        empty_label='Любое',
    )

    data_in = DateFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        widget=django.forms.DateInput(
            attrs={'type': 'date'},
        ),
        label='Дата',
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],

        }


class ArticleFilter(FilterSet):
    class Meta:
        model = Category
        fields = '__all__'
