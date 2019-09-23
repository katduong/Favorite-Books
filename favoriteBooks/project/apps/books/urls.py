from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addBook$', views.add, name='addBook'),
    url(r'^(?P<bookId>\d+)$', views.showBook, name="showBook"),
    url(r'^(?P<bookId>\d+)/addFavorite$', views.addFavorite, name="addFavorite"),
    url(r'^(?P<bookId>\d+)/unfavorite$', views.unFavorite, name="unFavorite"),
    url(r'^(?P<bookId>\d+)/delete$', views.deleteBook, name="delete"),
    url(r'^(?P<bookId>\d+)/update$', views.updateBook, name="update"),
    url(r'^(?P<bookId>\d+)/addFavoriteHome', views.addFavoriteHome)
    # url(r'^postMessage$', views.postMessage, name="postMessage"),
    # url(r'^postComment$', views.postComment, name="postComment"),
    # url(r'^deleteMessage/(?P<id>\d+)$', views.deleteMessage, name="deleteMess")

]
