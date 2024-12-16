from django.urls import path
from .views import poll_list, complete_poll, export_results, delete_poll, delete_question, toggle_poll, delete_option

urlpatterns = [
    path('', poll_list, name='poll_list'),
    path('data/<int:poll_id>/', complete_poll, name='complete_poll'),
    path('data/<int:poll_id>/results', export_results, name='export_results'),
    path('data/<int:poll_id>/poll_delete', delete_poll, name='delete_poll'),
    path('data/<int:poll_id>/toggle_poll', toggle_poll, name='toggle_poll'),
    path('data/<int:question_id>/question_delete', delete_question, name='delete_question'),
    path('data/<int:option_id>/option_delete', delete_option, name='delete_option'),
]
