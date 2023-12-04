"""
URL configuration for employee project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from work.views import Employee,BookView,Booklist,PersonView,Personlist,BookDetails,MobileView,Mobilelist,StudentView,Studentlist,StudentDetails,Student_Delete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee',Employee.as_view()),
    path('book',BookView.as_view()),
    path('books/all',Booklist.as_view()),
    path('person/',PersonView.as_view()),
    path('person/all',Personlist.as_view()),
    path('details/<int:pk>',BookDetails.as_view()),
    path('mobile/',MobileView.as_view()),
    path('mlist/',Mobilelist.as_view()),
    path('student/',StudentView.as_view()),
    path('slist/',Studentlist.as_view(),name='student-al'),
    path('sdetails/<int:pk>',StudentDetails.as_view(),name='student-det'),
    path('Student/<int:pk>/remove',Student_Delete.as_view(),name='student-del')
]
