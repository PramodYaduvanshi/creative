from django.urls import path
from api import views

urlpatterns = [
    path('data/', views.data_view, name='data'),
    path('trigger-batch-job/', views.trigger_job, name='trigger-job'),
    path('data-with-expiry/', views.data_session_expiry, name='data-session-expiry'),
]


