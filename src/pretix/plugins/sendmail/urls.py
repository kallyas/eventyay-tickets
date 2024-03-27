from django.urls import include, re_path

from . import views

urlpatterns = [
    re_path(r'^control/event/(?P<organizer>[^/]+)/(?P<event>[^/]+)/sendmail/$', views.SenderView.as_view(),
        name='send'),
    re_path(r'^control/event/(?P<organizer>[^/]+)/(?P<event>[^/]+)/sendmail/history/', views.EmailHistoryView.as_view(), name='history')
]
