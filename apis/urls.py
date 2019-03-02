from django.urls import path

from .views import SelectionView

# polls.viewsのアクションメソッドを指定
# @see https://qiita.com/juniskw/items/535d89677d9640f6734f
urlpatterns = [
    path('title/', SelectionView.as_view(), name='post'),  # name->関数名
]