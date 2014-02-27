from django.conf.urls import patterns, url
from gofish import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.user_login, name='login'),
    url(r'^logout/', views.user_logout, name='logout'),
    url(r'^register/', views.register, name='register'),
    # main game screen where playing action takes place
    url(r'^game/', views.game, name='game'),
    # a shopping screen where we can buy baits and new boats
    url(r'^shop/', views.shop, name='shop'),
    # a screen with rankings of all the players
    url(r'^rankings/', views.rankings, name='rankings'),
    # a screen showing the trophies of a particular user
    url(r'^trophies/', views.trophies, name='trophies'),

    # API calls will return json in all cases
    # FIX: I think there should be different syntax here...

    # create a new game, return all the necessary information
    # so that we can display it (lake, weather, time...)
    url(r'^api/newgame/', views.newgame, name='newgame'),
    # move to a different location. returns time taken
    url(r'^api/move/', views.move, name='move'),
    # fish in the current location. Returns what was caught
    url(r'^api/fish/', views.fish, name='fish'),
    # change the bait, choosing from the collection we have
    url(r'^api/change/bait/', views.changebait, name='changebait'),
    # buy the bait, to add in our collection
    url(r'^api/buy/bait/', views.buybait, name='buybait'),
    # update the boat
    url(r'^api/buy/boat/', views.buyboat, name='buyboat'),
    # finish the game, sell the fish, get the trophies
    url(r'^api/finish/', views.finish, name='finish')
)
