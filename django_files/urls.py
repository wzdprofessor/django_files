from django.contrib import admin
from django.urls import path,reverse,re_path
from django.views.static import serve
from myapp import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('media/<path>',serve,{'document_root':settings.MEDIA_ROOT}),
    path('test/',views.test11),
    path('oss/',views.oss,name='oss'),
]
