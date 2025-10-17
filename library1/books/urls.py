"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from tkinter.font import names

from django.contrib import admin
from django.urls import path
from books import views
from django.conf.urls.static import static
from django.conf import settings

app_name="books"
urlpatterns = [

    # path('',views.home,name="home"),
    path('',views.Home.as_view(),name="home"),
    path('add/',views.addbooks.as_view(),name="addbooks"),
    path('view/',views.viewbooks.as_view(),name="viewbooks"),
    path('bookdetail/<int:i>',views.bookdetail.as_view(),name="bookdetail"),
    path('editbook/<int:i>',views.editbook.as_view(),name="editbook"),
    path('deletebook/<int:i>',views.deletebook.as_view(),name="deletebook"),
    path('search/',views.search.as_view(),name="search"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
