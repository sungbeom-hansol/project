from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', views.start, name = 'start'),
  	url(r'^graph', views.graph, name = 'graph'),
	

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
