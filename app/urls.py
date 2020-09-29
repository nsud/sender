from django.urls import path, include, re_path
from app.views import add_email, ListMessage, ListEmail

app_name = 'app'
urlpatterns = [
    path('create/', add_email, name='create_email'),
    path('list/', ListMessage.as_view(), name='email_list'),
]