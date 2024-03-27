from django.urls import include, re_path

from .views import IndexView

urlpatterns = [
    re_path(r'^control/event/(?P<organizer>[^/]+)/(?P<event>[^/]+)/webcheckin/$',
            IndexView.as_view(), name='index'),
]
