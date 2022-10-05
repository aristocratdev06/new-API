from django.urls import path
from .views import (
    home,
    krasovkaMakeApi,
    singleapi,
    PostJoylash,
    PostYangilash,
    PostDelete
)

app_name ="api"

urlpatterns = [
    path('', home, name="home"),
    path('new-api/', krasovkaMakeApi),
    path('new-api/<int:pk>/', singleapi),
    path("new-post/", PostJoylash, name="new_post"),
    path("update-post/<int:pk>",PostYangilash, name="new_post"),
    path("delete/<int:pk>/", PostDelete)
]
