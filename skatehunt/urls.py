from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    # Admin:
    url(r'^$', 'skatehuntapp.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),


    # User Creation and Administration
    url(r'^register/$', 'skatehuntapp.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/'}, name='logout'),


    # Password Reset
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset',
        name='password_reset'),
    url(r'^password_reset/done/$',
        'django.contrib.auth.views.password_reset_done',
        name='password_reset_done'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete',
        name='password_reset_complete'),


    # Create Post
    url(r'^post/$', 'skatehuntapp.views.post', name='post'),


    # Vote Post
    # url(r'^vote/(?P<post_id>[0-9]+)/$', 'skatehuntapp.views.vote', name='vote')

)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
