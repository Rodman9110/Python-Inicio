from urllib.parse import urlparse
import django


from django.urls import path
from .views import BlogListView

app_name="blog"


urlpatterns = [
    path('',BlogListView.as_view(),name='home')

]
