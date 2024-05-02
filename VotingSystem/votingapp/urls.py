from . import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home page'),
    # path('Admin',views.admin,name='admin page')
    path('Add_Vote', views.add_voter, name='Add_Voting page'),
    path('Count_Vote', views.count_party_members, name='Count page'),
]
