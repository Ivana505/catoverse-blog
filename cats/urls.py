from . import views
from .views import EditCommentView
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('<slug:slug>', views.PostComment.as_view(), name='post_comment'),
    path('obesity/', views.NutritionPageView.as_view(), name='obesity'),
    path('funny-cats/', views.FunnyPageView.as_view(), name='funny'),
    path('trimming-a-cats-claws/', views.FunnyPageView.as_view(), name='health'),
    path('<slug:slug>/edit-blog-post/', views.EditCommentView.as_view(), name='edit-blog-post'),

]
