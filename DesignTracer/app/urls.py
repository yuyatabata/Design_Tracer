from django.urls import path
from . import views
from DesignTracer import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

app_name = "app"
urlpatterns = [
    path('',views.index, name='index'),
    path('users/<int:pk>/',views.users_detail, name='users_detail'),
    path('login/',auth_views.LoginView.as_view(template_name="app/login.html"), name="login"),
    path('logout/',auth_views.LoginView.as_view(), name="logout"),
    path('signup/', views.signup, name='signup'),
    path('images/<int:pk>/', views.images_detail, name="images_detail"),
    path('images/<int:pk>/delete/', views.images_delete, name="images_delete"),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
