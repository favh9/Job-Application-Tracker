from . import models
from rest_framework import serializers

class ApplicationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.JobApplication
        fields = '__all__'