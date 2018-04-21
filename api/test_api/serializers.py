from rest_framework import serializers
from .models import Test_form

class Test_formSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test_form
        fields = ("first_name", "last_name", "email")
