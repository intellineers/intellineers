from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    # url(r'^$', views.intermediateView, name="intermediateView"),
    # url(r'^base$', views.basetemplate, name="basetemplate"),
    url(r'[.]*', views.basetemplate, name="basetemplate"),
]
