from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve
from django.urls import path
from book_app.views import *
from accounts.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^ download / (P < path > .*)/$', serve,
        {'document_root': settings.MEDIA_ROOT}),
    path('', index, name='index'),
    path('add/', add, name='add'),
    path('detail/<int:id>/', detail, name='detail'),
    path('update/<int:id>/', edit, name='edit'),
    path('delete/<int:id>/', delete, name='delete'),
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
