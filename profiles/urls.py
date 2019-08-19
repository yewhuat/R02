from django.conf import settings
from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from .views import ProfileListView, ProfileDetailView
from .api.view import ProfileListAPIView
from . import views

urlpatterns = [
    url(r'^update/$', views.update_profile, name='update'),
    url(r'^detail/(?P<pk>\d+)$', ProfileDetailView.as_view(), name='detail'),
    url(r'^$', ProfileListView.as_view(), name='list'),
    #url(r'^detail/@(?P<username>[\w.@+-]+)/$', ProfileDetailView.as_view(), name='detail'),
    #url(r'', ProfileView.as_view(), name='profile_view'),
    url(r'^api/$', ProfileListAPIView.as_view(), name='api-list'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns+= (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))

#Class_name.objects.get(pk=self.kwargs.get('pk'))

# url(r'^$', ProfileView.as_view(), name='profile_view'),
# url(r'^profile/$', ProfileView.as_view(), name='profile_view'),
# url(r'^profile/update/$', views.update_profile, name='update'),
# url(r'^profile/list$', ProfileListView.as_view(), name='list'),
# url(r'^@(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name='profile-detail'),
