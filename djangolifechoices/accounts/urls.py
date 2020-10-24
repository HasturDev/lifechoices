from django.urls import path
from . import views

app_accounts = 'accounts'

urlpattern = [
    #plan views
    path('', views.plan_list, name='plan_list'),
    path('<int:year>/<int:month>/<int:day>/', views.plan_detail, name='plan_detail')
]