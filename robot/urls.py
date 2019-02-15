from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views
  
app_name = 'robot'

urlpatterns = [ 
    url(r'^input', views.RobotInputView.as_view()),
    url(r'^confirm', views.RobotConfirmView.as_view()),
    url(r'^complete', views.RobotCompleteView.as_view()),
    url(r'^', views.RobotTopView.as_view()),
    # url(r'^error', views.RobotTopView.as_view()), TODO for error
]