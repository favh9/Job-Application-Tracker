from rest_framework import viewsets
from .models import JobApplication
from .serializers import ApplicationSerializer


class ApplicationModelViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = ApplicationSerializer
        
        
        


