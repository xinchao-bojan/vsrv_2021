from django.urls import path, include

from main_app import views

urlpatterns = [
    path('motion/create/', views.CreateMotionData.as_view()),
    path('motion/room/<int:room_id>/', views.GetMotionDataByRoom.as_view()),
    path('rooms/all/', views.GetAllRooms.as_view()),
]