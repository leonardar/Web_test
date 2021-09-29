from django.urls import path, include
from web_table.views import TableListView

ap_name = 'web_table'
urlpatterns = [
    path('', TableListView.as_view(), name='table_list'),
]
