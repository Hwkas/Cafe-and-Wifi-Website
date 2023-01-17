from django.forms import Form, ModelForm, MultipleChoiceField, CheckboxSelectMultiple
from .models import *


class CafeFrom(ModelForm):
    class Meta:
        model = CafeModel
        fields = "__all__"
        