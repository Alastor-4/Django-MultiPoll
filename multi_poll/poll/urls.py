from django.urls import path
from .views import poll_list, complete_poll, export_results

urlpatterns = [
    path('', poll_list, name='poll_list'),
    path('poll/<int:poll_id>/', complete_poll, name='complete_poll'),
    path('poll/<int:poll_id>/results', export_results, name='export_results')
]
