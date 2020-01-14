from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views
from django.conf import settings # new
from django.urls import path, include # new
from django.contrib.staticfiles.urls import static
from django.conf.urls.static import static # new
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('', include('blog.urls')),
     path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')) # Django JET dashboard URLS
    
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)