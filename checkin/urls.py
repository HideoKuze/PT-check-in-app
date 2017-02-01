from django.conf.urls import url
from . import views

urlpatterns = [url(r'^sign_in', views.sign_in, name='sign_in'),
url(r'^sign_up', views.sign_up, name='sign_up'),
url(r'^client_roster',views.client_roster, name='client_roster')
]
