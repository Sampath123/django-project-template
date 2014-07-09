from django.conf.urls import patterns, include, url
from django.contrib import admin
from todoapp import views

admin.autodiscover()
urlpatterns = patterns('',
     url(r'^admin/', include(admin.site.urls)),
     url(r'^/tasks$', views.get_all_tasks, name='all_task'),
     url(r'^/tasks/private$', views.get_private_tasks, name='private_task'),
     url(r'^/tasks/public$', views.get_public_tasks, name='public_task'),
     url(r'^/users/(?P<name>\w+)/tasks$', views.get_user_tasks,
          name='user_task')

)
