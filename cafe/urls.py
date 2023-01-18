from django.urls import path


from .views import *

urlpatterns = [
    path("", view=home, name="home"),
    path("add-cafe", view=add_cafe, name="add-cafe"),
]
