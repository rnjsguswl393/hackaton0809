from django.contrib import admin
from django.urls import path
import myapp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',myapp.views.home,name="home"), 
    path('signup/', myapp.views.signup, name="signup"),
    path('login/', myapp.views.login, name="login"),
    path('logout/', myapp.views.logout, name="logout"),
    path('search/', myapp.views.search, name='search'),
    path('register/', myapp.views.register, name="register"),
    path('detail/', myapp.views.detail, name="detail"),
    path('pick/', myapp.views.pick, name="pick"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
