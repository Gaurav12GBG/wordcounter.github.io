"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from.import views
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "WordCounter Admin"
admin.site.site_title = "WordCounter Admin Panel"
admin.site.index_title = "Welcome WordCounter Admin Panel"

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('viewHistory', views.viewHistory, name="viewHistory"),
    path('update_content/<int:id>', views.update_content, name="update_content"),
    path('delete_content/<int:id>', views.delete_content, name="delete_content"),
    path('analyze', views.analyze, name="analyze"),
    path('logout', views.handleLogout, name="handlelogout"),
    path('profile', views.profile, name="profile"),
    path('edit_profile', views.edit_profile, name="edit_profile"),
    path('login1/', views.login1, name="login1"),
    path('signup1', views.signup1, name="signup1"),
    path('change_password', views.change_password, name="change_password"),
  
    

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 


