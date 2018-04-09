from django.conf.urls import url
from api import views 

urlpatterns = [
    url(r'^api/v1/user/info/(?P<pk>\d+)/$',views.show.as_view()),
    url(r'^api/v1/user/gender/(?P<pk>\d+)/$',views.update.as_view())
]
