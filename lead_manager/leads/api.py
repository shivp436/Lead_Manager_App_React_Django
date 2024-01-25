# Path: lead_manager/leads/api.py

from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

# Lead Viewset
# Allows us to create a CRUD API without specifying explicit methods for the functionality
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all() # This is the data that will be returned. Fetch all leads
    permission_classes = [
        permissions.AllowAny # Allow any user to access the data
    ]
    serializer_class = LeadSerializer
    