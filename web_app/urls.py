from django.urls import path
from django.views.generic import TemplateView

# from web_app.views import web_app_view

urlpatterns = [
    path('web/', TemplateView.as_view(template_name="login_web.html")),
]
