from django.urls import path
from . import views
app_name="feedback"

urlpatterns = [
    path('', views.FeedbackFormView.as_view(), name="form"),
]