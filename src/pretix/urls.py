from django.conf import settings
from django.urls import include, re_path
from django.views.generic import RedirectView

import pretix.control.urls
import pretix.presale.urls
from pretix.base.views import js_helpers

from .base.views import cachedfiles, csp, health, js_catalog, metrics, redirect

base_patterns = [
    re_path(r'^download/(?P<id>[^/]+)/$', cachedfiles.DownloadView.as_view(),
            name='cachedfile.download'),
    re_path(r'^healthcheck/$', health.healthcheck,
            name='healthcheck'),
    re_path(r'^redirect/$', redirect.redir_view, name='redirect'),
    re_path(r'^jsi18n/(?P<lang>[a-zA-Z-_]+)/$', js_catalog.js_catalog, name='javascript-catalog'),
    re_path(r'^metrics$', metrics.serve_metrics,
            name='metrics'),
    re_path(r'^csp_report/$', csp.csp_report, name='csp.report'),
    re_path(r'^js_helpers/states/$', js_helpers.states, name='js_helpers.states'),
    re_path(r'^api/v1/', include(('pretix.api.urls', 'pretixapi'), namespace='api-v1')),
    re_path(r'^api/$', RedirectView.as_view(url='/api/v1/'), name='redirect-api-version')
]

control_patterns = [
    re_path(r'^control/', include((pretix.control.urls, 'control'))),
]

debug_patterns = []
if settings.DEBUG:
    try:
        import debug_toolbar

        debug_patterns.append(re_path(r'^__debug__/', include(debug_toolbar.urls)))
    except ImportError:
        pass

common_patterns = base_patterns + control_patterns + debug_patterns
