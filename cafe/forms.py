from django.forms import Form, ModelForm, MultipleChoiceField, CheckboxSelectMultiple
from .models import *


class CafeFrom(ModelForm):
    class Meta:
        model = Cafe
        fields = "__all__"