"""metashark URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

from university.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('', excel, name='excel'),
    path('direction/', DirectionAPIViewCreate.as_view(), name="directions_view"),
    path('direction/<int:pk>/', DirectionAPIUpdateDestroy.as_view(), name="directions_update_destroy"),
    path('subject/', SubjectAPIView.as_view(), name="subject_view"),
    path('subject/create/', SubjectAPICreate.as_view(), name="subject_create"),
    path('subject/<int:pk>/', SubjectAPIUpdateDestroy.as_view(), name="subject_update_destroy"),
    path('student/', StudentAPIView.as_view(), name="student_view"),
    path('student/create/', StudentAPICreate.as_view(), name="student_create"),
    path('student/<int:pk>/', StudentAPIUpdateDestroy.as_view(), name="student_update_destroy"),
    path('group/', GroupAPIView.as_view(), name="group_view"),
    path('group/create/', GroupAPICreate.as_view(), name="group_create"),
    path('group/<int:pk>/', GroupAPIUpdateDestroy.as_view(), name="group_update_destroy"),
]
