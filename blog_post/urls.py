from django.conf.urls import url

from blog_post import views

urlpatterns = [
    url(r'^post-list/', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.view_post, name='view-post'),
]


