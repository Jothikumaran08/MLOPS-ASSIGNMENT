from rest_framework import serializers
from .models import InputData

class InputDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputData
        fields = ['input1', 'input2', 'input3', 'input4']
