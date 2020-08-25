from django.contrib import admin
from django.urls import path, include
#画像保存ここから
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#画像保存ここまで

urlpatterns = [
    path('admin/', admin.site.urls),#migrate時に一旦コメントアウト()
    path('', include('todo.urls')),
    path('', include('register.urls')),
]

#画像保存ここから
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#画像保存ここまで