from . import views
from .views import Comment, DeletePostView, DeleteCommentView
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('add_post/', views.add_post, name='add_post'),
    path('delete_post/<slug:slug>', DeletePostView.as_view(), name='delete_post'),
    path('delete_comment/<slug:slug>', DeleteCommentView.as_view(), name='delete_comment'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('<slug:slug>', views.PostComment.as_view(), name='post_comment'),
    path('obesity/', views.NutritionPageView.as_view(), name='obesity'),
    path('funny-cats/', views.FunnyPageView.as_view(), name='funny'),
    path(
        'trimming-a-cats-claws/',
        views.FunnyPageView.as_view(), name='health'),
]
