from django.urls import path, re_path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    #path('events/', views.all_events, name='show-events'),
    # path('<int:year>/<str:month>/', views.index, name='index'),
    #re_path(r'^(?P<year>[0-9]{4})/(?P<month>0?[1-9]|1[0-2])/', views.index, name='index'),
    path('credentials/', views.get_credentials, name='get_all_credentials'),
    path('credentials/<str:referent>', views.get_credential_detail, name='get-credential-detail'),
    path('credentials/delete/<str:referent>', views.delete_credential, name='delete-credential'),
    path('credentials/revoked/<str:referent>', views.check_revoked, name='delete-credential'),
]