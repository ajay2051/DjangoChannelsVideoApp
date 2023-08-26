from django.urls import path

from . import views

urlpatterns = [
    path("lobby/", views.lobby, name="lobby"),
    path("room/", views.room, name="room"),
    path("get_token/", views.get_token, name="get-token"),
    path("create_member/", views.createUser, name="create-member"),
    path("get_member/", views.getMember, name="get-member"),
    path("delete_member/", views.deleteMember, name="delete-member"),
    path("generate_unique_code/", views.generateUniqueCode, name='generate-code')
]
