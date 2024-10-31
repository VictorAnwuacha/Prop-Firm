from django.urls import path
from . import views

app_name = "conversation"

urlpatterns = [
    path("", views.home, name="home"),
    path("new/<int:item_pk>/", views.new_conversation, name="new"),
    path("inbox/", views.inbox, name="inbox"),
    path("detail/<int:pk>/", views.detail_inbox, name="detail"),

]
