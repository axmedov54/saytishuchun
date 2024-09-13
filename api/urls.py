from .views import PostListViews, PostCreateViuew, CreateViuew, ListCreateView, DeleteViews, CRUDview
from django.urls import path

urlpatterns = [
    path('', PostListViews.as_view(), name='apilist'),
    path('post/<int:pk>', PostCreateViuew.as_view(), name='post'),
    path('created/', CreateViuew.as_view(), name='create'),
    path('list/', ListCreateView.as_view(), name='list'),
    path('delete/<int:pk>/', DeleteViews.as_view()),
    path('api/<int:pk>/',CRUDview.as_view())
]