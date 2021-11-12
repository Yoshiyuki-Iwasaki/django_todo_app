from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # ←一覧
    path('<int:id>/delete/', views.delete, name='delete'),  # ←削除機能用
    path('todo/<str:category>/', views.todo_category, name='todo_category'),  # ←カテゴリ
]
