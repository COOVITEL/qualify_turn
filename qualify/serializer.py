""" This module contein serializer classes"""
from rest_framework import serializers
from .models import Quality


class QualitySerializer(serializers.ModelSerializer):
    """ This class serializer all object to Quality"""
    class Meta:
        model = Quality
        fields = '__all__'
