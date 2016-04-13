from django.conf.urls import url, patterns
from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^show/$', views.CreateProduct.as_view(template_name="catalog/add.html"), name='show'),
    url(r'^update/(?P<pk>\d+)/$', views.UpdateProduct.as_view(template_name="catalog/update.html"), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.DeleteProduct.as_view(template_name="catalog/delete.html"), name='delete'),


]
