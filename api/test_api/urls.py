from django.urls import path
from . import views
#from .views import

urlpatterns = [
    path('test_form/', views.test_form_collection, name="all"),
]
