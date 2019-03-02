from django.urls import path

from . import views

# polls.viewsのアクションメソッドを指定
# @see https://qiita.com/juniskw/items/535d89677d9640f6734f
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:money_id>/', views.detail, name='detail'),
    path('<int:money_id>/', views.edit, name='edit'),
    path('<int:money_id>/', views.delete, name='del'),
]