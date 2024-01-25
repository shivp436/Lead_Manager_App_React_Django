from rest_framework import routers
from .api import LeadViewSet

router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads')
# similar to app.use('/api/leads', require('./routes/api/leads'))
# syntax: router.register('route', viewset, 'name')

urlpatterns = router.urls