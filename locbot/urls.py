from django.conf.urls import url
from django.conf.urls import include
from locbot import views
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

urlpatterns = [
	
    url(r'^find/$',views.use_api, name="search"),
    url(r'^$', views.home, name = "homepage"),
]

